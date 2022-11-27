#!/bin/bash
source scripts/setup_python.sh

log_dir=logs
[ -d $log_dir ] || mkdir $log_dir
timestamp=$(date +"%y_%m_%d_%H_%M_%S")
source_path=src/whereami.py
echo running $snippet
$python_exe $source_path 2>&1 | tee $log_dir/run_$timestamp.log
echo run terminated