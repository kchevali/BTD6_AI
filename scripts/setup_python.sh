#!/bin/bash

env_dir=$PWD/python_env
export python_exe=$env_dir/bin/python3
if [[ ! -d "$env_dir" ]]; then
    echo Installing virtual python...
    python3 -m venv $env_dir
    $python_exe -m pip install -r $PWD/requirements.txt
    echo Virtual python installation complete
fi