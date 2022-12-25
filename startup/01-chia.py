from blspy import (PrivateKey, AugSchemeMPL, G1Element, G2Element)

from chia.consensus.default_constants import DEFAULT_CONSTANTS
from chia.rpc.full_node_rpc_client import FullNodeRpcClient
from chia.rpc.rpc_client import RpcClient
from chia.rpc.wallet_rpc_client import WalletRpcClient
from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.program import Program, INFINITE_COST
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.types.coin_record import CoinRecord
from chia.types.coin_spend import CoinSpend
from chia.types.condition_opcodes import ConditionOpcode
from chia.types.full_block import FullBlock
from chia.types.spend_bundle import SpendBundle
from chia.util.bech32m import decode_puzzle_hash, encode_puzzle_hash
from chia.util.byte_types import hexstr_to_bytes
from chia.util.config import load_config
from chia.util.default_root import DEFAULT_ROOT_PATH
from chia.util.hash import std_hash
from chia.util.ints import uint16, uint32, uint64
from chia.util.json_util import dict_to_json_str
from chia.wallet.puzzles import p2_delegated_puzzle_or_hidden_puzzle
from chia.wallet.puzzles.p2_delegated_puzzle_or_hidden_puzzle import (
    calculate_synthetic_offset,
    calculate_synthetic_public_key,
    calculate_synthetic_secret_key,
    DEFAULT_HIDDEN_PUZZLE_HASH,
    puzzle_for_conditions,
    puzzle_for_pk,
    puzzle_hash_for_synthetic_public_key,
    solution_for_conditions
)

from clvm_tools.binutils import assemble, disassemble
from clvm_tools.clvmc import compile_clvm_text
from clvm.casts import int_to_bytes