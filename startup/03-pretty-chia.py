# rich
# https://www.willmcgugan.com/blog/tech/post/rich-adds-support-for-jupyter-notebooks/
from rich import box
from rich import pretty
from rich.console import Console
from rich import inspect
from rich.jupyter import print
from rich.syntax import Syntax
from rich.table import Table
from rich.tree import Tree
import rich
pretty.install()

from chia.consensus.default_constants import DEFAULT_CONSTANTS
from chia.types.blockchain_format.program import Program
from chia.types.coin_spend import CoinSpend
from chia.types.condition_opcodes import ConditionOpcode
from chia.util.hash import std_hash

def print_clsp(clsp: str, line_numbers=True):
    console = Console()
    syntax = Syntax(clsp, "clojure", line_numbers=line_numbers, word_wrap=True)
    console.print(syntax)


def print_program(program: Program):
    p = disassemble(program)
    console = Console()
    syntax = Syntax(p, "clojure", line_numbers=False, word_wrap=True)
    console.print(syntax)


def print_puzzle(puzzle: Program, tail=0):
    p = disassemble(puzzle)
    if tail == 0:
        print(p)
    else:
        print(f"...{p[(tail * -1):]}")


def get_conditions(puzzle: Program, solution: Program):
    cost, r = puzzle.run_with_cost(DEFAULT_CONSTANTS.MAX_BLOCK_COST_CLVM, solution)
    conditions = r.as_python()
    return conditions


def print_condition(condition):
    console = Console()
    opcode = ConditionOpcode.from_bytes(condition[0])
    condition_args = ""
    for a in condition[1:]:
        condition_args += f" {disassemble(Program.to(a))}"

    console.print(
        Syntax(
            f"({opcode.name} {condition_args})",
            "clojure",
            word_wrap=True,
        )
    )


def print_conditions(puzzle: Program, solution: Program):
    conditions = get_conditions(puzzle, solution)
    for c in conditions:
        print_condition(c)

def print_coin_spends(coin_spends):
    console = Console()

    for cs in coin_spends:
        coin_id = cs.coin.name()
        console.print(f'\n\n===<{coin_id.hex()}>===')
        console.print(cs.coin.to_json_dict())
        conditions = get_conditions(cs.puzzle_reveal.to_program(), cs.solution.to_program())
        for c in conditions:
            print_condition(c)
            opcode = ConditionOpcode.from_bytes(c[0])
            if opcode == ConditionOpcode.CREATE_PUZZLE_ANNOUNCEMENT:
                announcement = std_hash(
                    cs.coin.puzzle_hash
                    + c[1]
                )
                console.print(f'---<{announcement.hex()}>---')
            if opcode == ConditionOpcode.CREATE_COIN_ANNOUNCEMENT:
                announcement = std_hash(
                    coin_id
                    + c[1]
                )
                console.print(f'---<{announcement.hex()}>---')