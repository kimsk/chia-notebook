# Build
```sh
docker build -t karlkim/chia-notebook .
```

# Run

```PowerShell
docker run -it --rm -p 8888:8888 -v ${HOME}/kimsk/chia-concepts:/home/jovyan -v ${env:CHIA_ROOT}:/home/jovyan/.chia-external karlkim/chia-notebook
```

## Run and Grant jovyan passwordless sudo rights.
```PowerShell
docker run -it --rm -e GRANT_SUDO=yes --user root -p 8888:8888 -v ${HOME}/kimsk/chia-concepts:/home/jovyan -v ${env:CHIA_ROOT}:/home/jovyan/.chia-external karlkim/chia-notebook
```

## curl

```sh
curl --insecure --cert ~/.chia/testnet/config/ssl/full_node/private_full_node.crt --key ~/.chia/testnet/config/ssl/full_node/private_full_node.key -d '{}' -H "Content-Type: application/json" -X POST https://host.docker.internal:8555/get_network_info
```

## Misc
```sh
$ jupyter kernelspec list
Available kernels:
  python3    /opt/conda/share/jupyter/kernels/python3
```

## Automatically Loading Needed Chia Libraries
```sh
.ipython/profile_default/startup via 🐍 v3.10.8
❯ lsd -l
.rw-r--r-- karlkim staff 1.3 KB Mon Oct 31 23:32:58 2022  00-load_chia.py
.rw-r--r-- karlkim staff 371 B  Thu Aug  4 10:21:47 2022  README
```
```python
# chia libraries
from blspy import (PrivateKey, AugSchemeMPL, G1Element, G2Element)

from chia.consensus.default_constants import DEFAULT_CONSTANTS
from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.program import Program
from chia.types.coin_spend import CoinSpend
from chia.types.condition_opcodes import ConditionOpcode
from chia.types.spend_bundle import SpendBundle
from chia.util.hash import std_hash
from chia.wallet.puzzles import p2_delegated_puzzle_or_hidden_puzzle

from chia.wallet.puzzles.p2_delegated_puzzle_or_hidden_puzzle import (
    DEFAULT_HIDDEN_PUZZLE_HASH,
    calculate_synthetic_secret_key,
    puzzle_for_pk,
    puzzle_for_conditions,
    solution_for_conditions,
)

from clvm.casts import int_to_bytes
from clvm_tools.clvmc import compile_clvm_text
from clvm_tools.binutils import disassemble

from chia.rpc.full_node_rpc_client import FullNodeRpcClient
from chia.util.config import load_config
from chia.util.default_root import DEFAULT_ROOT_PATH
from chia.util.ints import uint16

config = load_config(DEFAULT_ROOT_PATH, "config.yaml")
selected_network = config["selected_network"]
genesis_challenge = config["network_overrides"]["constants"][selected_network]["GENESIS_CHALLENGE"]

self_hostname = config["self_hostname"] # localhost
full_node_rpc_port = config["full_node"]["rpc_port"] # 8555
```

# References
- [What is the password for using "sudo apt-get install" command?](https://github.com/jupyter/docker-stacks/issues/949)
- [Using .NET notebooks with Jupyter Notebook / JupyterLab](https://github.com/dotnet/interactive/blob/main/docs/NotebookswithJupyter.md#using-net-notebooks-with-jupyter-notebook--jupyterlab)
- [How to Automatically Import Your Favorite Libraries into IPython or a Jupyter Notebook](https://towardsdatascience.com/how-to-automatically-import-your-favorite-libraries-into-ipython-or-a-jupyter-notebook-9c69d89aa343)
- [Common Jupyter Lab Keyboard Shortcuts](https://gist.github.com/discdiver/9e00618756d120a8c9fa344ac1c375ac)
