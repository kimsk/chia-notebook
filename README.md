# Build
```sh
docker build -t karlkim/chia-notebook .
```

# Run

```PowerShell
docker run -it --rm -p 8888:8888 -v ${HOME}/kimsk/chia-concepts:/home/jovyan -v ${env:CHIA_ROOT}:/home/jovyan/.chia-external karlkim/chia-notebook
```

```PowerShell
docker run -it --rm -p 8888:8888 -v ${HOME}/kimsk/chia-concepts:/home/jovyan -v /mnt/e/testnet/db:/home/jovyan/full_node_db karlkim/chia-notebook
```

```PowerShell
docker run -it --rm -e GRANT_SUDO=yes --user root --expose=8444 -p 8888:8888 -v ${HOME}/kimsk/chia-concepts:/home/jovyan -v /mnt/e/testnet/db:/home/jovyan/full_node_db karlkim/chia-notebook
```

## Run and Grant jovyan passwordless sudo rights.
```PowerShell
docker run -it --rm -e GRANT_SUDO=yes --user root -p 8888:8888 -v ${HOME}/kimsk/chia-concepts:/home/jovyan -v ${env:CHIA_ROOT}:/home/jovyan/.chia-external karlkim/chia-notebook
```

## curl

```sh
curl --insecure --cert /.chia/config/ssl/full_node/private_full_node.crt --key /.chia/config/ssl/full_node/private_full_node.key -d '{}' -H "Content-Type: application/json" -X POST https://host.docker.internal:8555/get_network_info
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
- [Jupyter Server Options](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#common-features)