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
```sh
docker run -it --rm -e GRANT_SUDO=yes --user root -p 8888:8888 -v ${HOME}/kimsk/chia-concepts:/home/jovyan -v ${HOME}/.chia/testnet:/home/jovyan/.chia/testnet karlkim/chia-notebook
```

## curl

```sh
curl --insecure --cert ~/.chia/testnet/config/ssl/full_node/private_full_node.crt --key ~/.chia/testnet/config/ssl/full_node/private_full_node.key -d '{}' -H "Content-Type: application/json" -X POST https://host.docker.internal:8555/get_network_info
```
