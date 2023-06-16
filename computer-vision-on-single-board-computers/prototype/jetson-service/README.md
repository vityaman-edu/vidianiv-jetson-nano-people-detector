# Prototype of program that runs on Jetson Nano

|          |                            |
| -------- | -------------------------- |
| Designer | Dmitry Belyakov (@kimiega) |
| Designer | Victor Smirnov  (@vitya)   |

## Requirements

Run inside `jetson-inference` docker container.

```bash
python3 -m pip install mypy
```

## Build & Run

```bash
bash ci/project/run.sh --output=rtp://192.168.1.40:1234
```

[Prototype](../../README.md)
