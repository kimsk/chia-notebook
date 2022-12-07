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

async def get_synced_wallet_client(fingerprint) -> WalletRpcClient:
    wallet_client = await get_wallet_client()
    await wallet_client.log_in(fingerprint)
    fingerprint = await wallet_client.get_logged_in_fingerprint()

    sync_status = False
    while not sync_status:
        sync_status = await wallet_client.get_synced()
        time.sleep(5)

    return wallet_client

async def close_rpc_client(client: RpcClient):
    client.close()
    await client.await_closed()

# kimsk/chia-concepts
sys.path.insert(0, "/Users/karlkim/kimsk/chia-concepts/shared")
from utils import (load_program, print_program, print_clsp, print_puzzle, print_json)
import singleton_utils
import wallet_utils
