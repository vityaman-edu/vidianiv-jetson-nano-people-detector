#!/usr/bin/env bash
set -e 

SCRIPT_DIRECTORY=`dirname "$0"`
cd $SCRIPT_DIRECTORY/..

echo "[prototype/recognizer] envsetup: Setting up python environment"

python -m venv venv

echo "[prototype/recognizer] envsetup: py venv is ready"
