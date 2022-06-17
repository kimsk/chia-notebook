#! /usr/bin/pwsh

Write-Host $env:CHIA_ROOT

chia init
chia configure -t true

rm -rf "$($env:CHIA_ROOT)/db"
ln -s "$HOME/full_node_db" "$($env:CHIA_ROOT)/db"

# https://github.com/Chia-Network/chia-blockchain/issues/1535
# ipV6 not enabled
$configFile = "$($env:CHIA_ROOT)/config/config.yaml"
$configYaml = Get-Content $configFile
$configYaml -replace "localhost", "127.0.0.1"
| Out-File -Force $configFile

# /bin/bash
start-notebook.sh
