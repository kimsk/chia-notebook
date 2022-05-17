from blspy import (PrivateKey, AugSchemeMPL, G1Element, G2Element)

from cdv.test import Network, Wallet
from chia.consensus.default_constants import DEFAULT_CONSTANTS
from chia.types.blockchain_format.program import Program
from chia.types.coin_spend import CoinSpend
from chia.types.spend_bundle import SpendBundle

from chia.wallet.puzzles import (
    p2_delegated_puzzle_or_hidden_puzzle
)

network: Network = None

async def get_network_async():
    global network
    if network == None:
        network = await Network.create()
        await network.farm_block()
    return network

async def close_network_async():
    global network
    if network != None:
        await network.close()
    network = None
