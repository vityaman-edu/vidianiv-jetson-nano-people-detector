#!/usr/bin/env bash
set -e
SCRIPT_DIRECTORY=`dirname "$0"`
cd $SCRIPT_DIRECTORY/..

PACKAGE_DIST_PATH="vidianiv_people_recognizer*.whl"

echo "[prototype/recognizer] build: Building the package..."

python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install dist/$PACKAGE_DIST_PATH

echo "[prototype/recognizer] build: Package distribution is ready."