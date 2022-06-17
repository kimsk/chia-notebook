#! /usr/bin/pwsh

# "/.chia"
Write-Host $env:CHIA_ROOT

Install-Module powershell-yaml -Force

$chia = "/.chia"

$externalChia = "$HOME/.chia-external"

ln -s ${externalChia}/db $chia/db
ln -s ${externalChia}/wallet $chia/wallet
ln -s ${externalChia}/config/ssl $chia/config/ssl

cp $externalChia/config/config.yaml $chia/config

$config = 
    Get-Content $chia/config/config.yaml
    | ConvertFrom-Yaml

# change docker localhost
$config.self_hostname = "host.docker.internal"

$config
| ConvertTo-Yaml
| Out-File $chia/config/config.yaml

/bin/bash
# start-notebook.sh
