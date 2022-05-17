from chia.util.config import load_config
from chia.util.default_root import DEFAULT_ROOT_PATH
from chia.rpc.full_node_rpc_client import FullNodeRpcClient
from chia.util.ints import uint16

# config/config.yaml
config = load_config(DEFAULT_ROOT_PATH, "config.yaml")
config["self_hostname"] = "host.docker.internal"
selected_network = config["selected_network"]
genesis_challenge = config["farmer"]["network_overrides"]["constants"][selected_network]["GENESIS_CHALLENGE"]

self_hostname = config["self_hostname"] # localhost
full_node_rpc_port = config["full_node"]["rpc_port"] # 8555

async def get_blockchain_state_async():
    try:
        full_node_client = await FullNodeRpcClient.create(
                self_hostname, uint16(full_node_rpc_port), DEFAULT_ROOT_PATH, config
            )
        state = await full_node_client.get_blockchain_state()
        return state
    finally:
        full_node_client.close()
        await full_node_client.await_closed()