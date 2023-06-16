set -e

cd $(dirname -- "$0"; )
cd ../..

cd src
python3 main.py $1
