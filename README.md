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
[00-load_chia.py](00-load_chia.py)
```sh
.ipython/profile_default/startup via 🐍 v3.10.8
❯ lsd -l
lrwxr-xr-x karlkim staff  50 B Tue Nov  1 22:36:03 2022  00-load_chia.py ⇒ /Users/karlkim/kimsk/chia-notebook/00-load_chia.py
.rw-r--r-- karlkim staff 371 B Thu Aug  4 10:21:47 2022  README
```

# References
- [What is the password for using "sudo apt-get install" command?](https://github.com/jupyter/docker-stacks/issues/949)
- [Using .NET notebooks with Jupyter Notebook / JupyterLab](https://github.com/dotnet/interactive/blob/main/docs/NotebookswithJupyter.md#using-net-notebooks-with-jupyter-notebook--jupyterlab)
- [How to Automatically Import Your Favorite Libraries into IPython or a Jupyter Notebook](https://towardsdatascience.com/how-to-automatically-import-your-favorite-libraries-into-ipython-or-a-jupyter-notebook-9c69d89aa343)
- [Common Jupyter Lab Keyboard Shortcuts](https://gist.github.com/discdiver/9e00618756d120a8c9fa344ac1c375ac)
