#!/usr/bin/env bash
set -e
SCRIPT_DIRECTORY=`dirname "$0"`
cd $SCRIPT_DIRECTORY/..

PACKAGE_DIST_PATH="vidianiv_people_recognizer*.whl"

echo "[prototype/recognizer] build: Building the package..."

pip3 install setuptools
pip3 install wheel
python3 setup.py bdist_wheel sdist
pip3 install .

echo "[prototype/recognizer] build: Package distribution is ready."