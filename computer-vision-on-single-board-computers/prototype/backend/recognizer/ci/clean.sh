#!/usr/bin/env bash
set -e
SCRIPT_DIRECTORY=`dirname "$0"`
cd $SCRIPT_DIRECTORY/..

echo "[prototype/recognizer] clean: Running task 'Clean'..."

echo "[prototype/recognizer] clean: removing '.ipynb_checkpoints'..."
rm -rf notebook/.ipynb_checkpoints
rm -rf notebook/res/.ipynb_checkpoints

echo "[prototype/recognizer] clean: removing downloads..."
rm -rf notebook/res/yolov3.cfg
rm -rf notebook/res/yolov3.txt
rm -rf notebook/res/yolov3.weights
rm -rf notebook/res/haarcascade_frontalface_default.xml

rm -rf notebook/datasets
rm -rf notebook/runs
rm -rf notebook/bus.jpg
rm -rf notebook/yolov8n.pt

echo "[prototype/recognizer] clean: remove dist"
rm -rf dist

echo "[prototype/recognizer] clean: remove venv"
rm -rf venv

echo "[prototype/recognizer] clean: Task 'Clean' done."
