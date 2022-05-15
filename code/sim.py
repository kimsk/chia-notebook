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
    await network.close()
    network = None

def get_normal_coin_spend(wallet: Wallet, coin, conditions):

    delegated_puzzle_solution = Program.to((1, conditions))
    synthetic_sk: PrivateKey = p2_delegated_puzzle_or_hidden_puzzle.calculate_synthetic_secret_key(
        wallet.sk_,
        p2_delegated_puzzle_or_hidden_puzzle.DEFAULT_HIDDEN_PUZZLE_HASH
    )
    synthetic_pk = synthetic_sk.get_g1()

    solution = Program.to([[], delegated_puzzle_solution, []])

    coin_spend = CoinSpend(
            coin.as_coin(),
            wallet.puzzle, # p2_delegated_puzzle_or_hidden_puzzle
            solution,
        )

    sig_msg = delegated_puzzle_solution.get_tree_hash() + coin.name() + DEFAULT_CONSTANTS.AGG_SIG_ME_ADDITIONAL_DATA
    sig = AugSchemeMPL.sign(synthetic_sk, sig_msg)

    return coin_spend, sig_msg, sig, synthetic_pk

def get_signature(wallet: Wallet, message):
    sk = wallet.sk_
    synthetic_sk: PrivateKey = p2_delegated_puzzle_or_hidden_puzzle.calculate_synthetic_secret_key(
        sk,
        p2_delegated_puzzle_or_hidden_puzzle.DEFAULT_HIDDEN_PUZZLE_HASH
    )
    sig = AugSchemeMPL.sign(synthetic_sk, message)
    return sig