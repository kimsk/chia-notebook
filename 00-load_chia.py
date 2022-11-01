# others
import json
import sys

# chia
from blspy import (PrivateKey, AugSchemeMPL, G1Element, G2Element)

from chia.consensus.default_constants import DEFAULT_CONSTANTS
from chia.rpc.full_node_rpc_client import FullNodeRpcClient
from chia.rpc.rpc_client import RpcClient
from chia.rpc.wallet_rpc_client import WalletRpcClient
from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.program import Program
from chia.types.coin_spend import CoinSpend
from chia.types.condition_opcodes import ConditionOpcode
from chia.types.spend_bundle import SpendBundle
from chia.util.bech32m import decode_puzzle_hash, encode_puzzle_hash
from chia.util.config import load_config
from chia.util.default_root import DEFAULT_ROOT_PATH
from chia.util.hash import std_hash
from chia.util.ints import uint16
from chia.wallet.puzzles import p2_delegated_puzzle_or_hidden_puzzle
from chia.wallet.puzzles.p2_delegated_puzzle_or_hidden_puzzle import (
    DEFAULT_HIDDEN_PUZZLE_HASH,
    calculate_synthetic_secret_key,
    puzzle_for_pk,
    puzzle_for_conditions,
    solution_for_conditions,
)

from clvm_tools.binutils import disassemble
from clvm_tools.clvmc import compile_clvm_text
from clvm.casts import int_to_bytes

config = load_config(DEFAULT_ROOT_PATH, "config.yaml")
selected_network = config["selected_network"]
genesis_challenge = config["network_overrides"]["constants"][selected_network]["GENESIS_CHALLENGE"]

self_hostname = config["self_hostname"]
full_node_rpc_port = config["full_node"]["rpc_port"]
wallet_rpc_port = config["wallet"]["rpc_port"]


async def get_full_node_client() -> FullNodeRpcClient:
    full_node_client = await FullNodeRpcClient.create(
        self_hostname, uint16(full_node_rpc_port), DEFAULT_ROOT_PATH, config
    )
    return full_node_client

async def get_wallet_client() -> WalletRpcClient:
    wallet_client = await WalletRpcClient.create(
        self_hostname, uint16(wallet_rpc_port), DEFAULT_ROOT_PATH, config
    )
    return wallet_client

async def close_rpc_client(client: RpcClient):
    client.close()
    await client.await_closed()

# kimsk/chia-concepts
sys.path.insert(0, "/Users/karlkim/kimsk/chia-concepts/shared")
from utils import (load_program, print_program, print_puzzle, print_json)
import singleton_utils
