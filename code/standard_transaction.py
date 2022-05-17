from blspy import (PrivateKey, AugSchemeMPL, G1Element, G2Element)

from chia.consensus.default_constants import DEFAULT_CONSTANTS
from chia.types.blockchain_format.program import Program
from chia.types.coin_record import Coin
from chia.types.coin_spend import CoinSpend

from chia.wallet.puzzles import (
    p2_delegated_puzzle_or_hidden_puzzle
)

def get_normal_spend_signature(sk: PrivateKey, message):
    synthetic_sk: PrivateKey = p2_delegated_puzzle_or_hidden_puzzle.calculate_synthetic_secret_key(
        sk,
        p2_delegated_puzzle_or_hidden_puzzle.DEFAULT_HIDDEN_PUZZLE_HASH
    )
    sig = AugSchemeMPL.sign(synthetic_sk, message)
    return sig

def get_normal_coin_spend_and_sig(sk: PrivateKey, coin: Coin, conditions):
    puzzle_reveal = p2_delegated_puzzle_or_hidden_puzzle.puzzle_for_pk(sk.get_g1())
    delegated_puzzle: Program = p2_delegated_puzzle_or_hidden_puzzle.puzzle_for_conditions(conditions) 
    solution = p2_delegated_puzzle_or_hidden_puzzle.solution_for_conditions(conditions)

    coin_spend = CoinSpend(
            coin,
            puzzle_reveal,
            solution,
        )

    message = delegated_puzzle.get_tree_hash() + coin.name() + DEFAULT_CONSTANTS.AGG_SIG_ME_ADDITIONAL_DATA
    sig = get_normal_spend_signature(sk, message)

    return coin_spend, sig
