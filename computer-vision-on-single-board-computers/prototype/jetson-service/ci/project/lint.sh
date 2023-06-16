set -e

cd $(dirname -- "$0"; )
cd ../..

python3 -m mypy src --config-file project.toml
