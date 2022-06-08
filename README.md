# Build
```sh
docker build -t karlkim/chia-notebook .
```

# Run
```sh
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan -v "${HOME}/.chia/testnet":/home/jovyan/.chia/testnet karlkim/chia-notebook
```

```sh
docker run -it --rm -p 8888:8888 -v ${HOME}/kimsk/chia-concepts:/home/jovyan -v ${HOME}/.chia/testnet:/home/jovyan/.chia/testnet karlkim/chia-notebook
```

## Run and Grant jovyan passwordless sudo rights.
```h
docker run -it --rm -e GRANT_SUDO=yes --user root -p 8888:8888 -v ${HOME}/kimsk/chia-concepts:/home/jovyan -v ${HOME}/.chia/testnet:/home/jovyan/.chia/testnet karlkim/chia-notebook
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

# References
- [What is the password for using "sudo apt-get install" command?](https://github.com/jupyter/docker-stacks/issues/949)
- [Using .NET notebooks with Jupyter Notebook / JupyterLab](https://github.com/dotnet/interactive/blob/main/docs/NotebookswithJupyter.md#using-net-notebooks-with-jupyter-notebook--jupyterlab)