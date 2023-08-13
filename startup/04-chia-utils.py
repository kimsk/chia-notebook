from typing import List

from chia.types.announcement import Announcement
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.types.coin_spend import CoinSpend

ZERO_32 = bytes32([0] * 32)


def read_file(file_path):
    with open(file_path) as file:
        content = file.read()
        return content


def write_file(content, file_path):
    with open(file_path, "w") as file:
        file.write(content)


def show_config():
    print(f"chia_root: {chia_root}")
    print(f"self_hostname: {self_hostname}")
    print(f"full_node_rpc_port: {full_node_rpc_port}")
    print(f"wallet_rpc_port: {wallet_rpc_port}")
    print(f"selected_network: {selected_network}")
    print(f"genesis_challenge: {genesis_challenge}")
    print(f"address prefix: {address_prefix}")


def show_spend_bundle(sp):
    print(sp.aggregated_signature)
    for cs in sp.coin_spends:
        print(cs.coin.name().hex())
        print(cs.coin.to_json_dict())
        # print_program(cs.puzzle_reveal.to_program())
        print_program(cs.solution.to_program())

        if cs.coin.parent_coin_info != bytes32([0] * 32):
            print_conditions(cs.puzzle_reveal.to_program(), cs.solution.to_program())


def show_offer_spend_bundle(o):
    show_spend_bundle(o.to_spend_bundle())


def show_offer_valid_spend(o):
    show_spend_bundle(o.to_valid_spend())


def get_puzzle_announcements(coin_spends: List[CoinSpend]) -> List[Announcement]:
    notarized_coin_spends = filter(
        lambda cs: cs.coin.parent_coin_info == ZERO_32, coin_spends
    )
    puzzle_announcements = []
    for cs in notarized_coin_spends:
        puzzle_hash = cs.coin.puzzle_hash
        solution = cs.solution.to_program()
        for notarized_coin_payment in solution.as_iter():
            message: bytes32 = notarized_coin_payment.get_tree_hash()
            puzzle_announcement = Announcement(puzzle_hash, message)
            puzzle_announcements.append(puzzle_announcement)
    return puzzle_announcements


### RPC


#### Legacy
async def get_coin_record_by_name(full_node_client, name: bytes32):
    return await full_node_client.get_coin_record_by_name(name)


async def get_coin_records_by_parent_id(full_node_client, parent_id: bytes32):
    return await full_node_client.get_coin_records_by_parent_ids([parent_id])


async def get_coin_records_by_puzzle_hash(full_node_client, puzzle_hash: bytes32):
    return await full_node_client.get_coin_records_by_puzzle_hash(puzzle_hash)


async def get_coin_records_by_hint(full_node_client, hint: bytes32):
    return await full_node_client.get_coin_records_by_hint(hint)


async def get_coin_spend(full_node_client, coin_id: bytes32, spent_height):
    return await full_node_client.get_puzzle_and_solution(coin_id, spent_height)


async def get_coins_in_block(full_node_client, height):
    block_records = await full_node_client.get_block_records(height, height + 1)
    header_hash = bytes32.from_hexstr(block_records[0]["header_hash"])
    result = await full_node_client.get_additions_and_removals(header_hash)
    return result


#### Using client.fetch
async def fetch_rpc(client, rpc, request={}):
    response = await client.fetch(rpc, request)
    return response


import os
import pathlib
from chia.util.config import load_config

testnet_root = pathlib.Path(os.path.expanduser("~/.chia/testnet10"))
mainnet_root = pathlib.Path(os.path.expanduser("~/.chia/mainnet"))


def get_chia_notebook_config(chia_root: Path):
    chia_config = load_config(chia_root, "config.yaml")
    self_hostname = chia_config["self_hostname"]

    full_node_rpc_port = chia_config["full_node"]["rpc_port"]
    wallet_rpc_port = chia_config["wallet"]["rpc_port"]

    selected_network = chia_config["selected_network"]

    genesis_challenge = bytes32.from_hexstr(
        chia_config["network_overrides"]["constants"][selected_network][
            "GENESIS_CHALLENGE"
        ]
    )
    address_prefix = chia_config["network_overrides"]["config"][selected_network][
        "address_prefix"
    ]
    return {
        "chia_root": chia_root,
        "chia_config": chia_config,
        "self_hostname": self_hostname,
        "full_node_rpc_port": full_node_rpc_port,
        "wallet_rpc_port": wallet_rpc_port,
        "selected_network": selected_network,
        "genesis_challenge": genesis_challenge,
        "address_prefix": address_prefix,
    }


def get_full_node_fetch(config):
    return with_full_node_rpc_client(
        config["self_hostname"],
        config["full_node_rpc_port"],
        config["chia_root"],
        config["chia_config"],
    )(fetch_rpc)


def get_wallet_fetch(config):
    return with_wallet_rpc_client(
        config["self_hostname"],
        config["wallet_rpc_port"],
        config["chia_root"],
        config["chia_config"],
    )(fetch_rpc)


### Example
"""
config = get_chia_notebook_config(testnet_root)
full_node_fetch = get_full_node_fetch(config)
wallet_fetch = get_wallet_fetch(config)
assert (await full_node_fetch('healthz'))['success']
assert (await wallet_fetch('healthz'))['success']
"""
