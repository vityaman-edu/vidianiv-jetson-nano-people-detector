set -e

cd $(dirname -- "$0"; )
cd ../..

JETSON_SERVICE_HOME=$(pwd)
echo -e "JETSON_SERVICE_HOME = $JETSON_SERVICE_HOME \n"

cd $JETSON_INFERENCE_HOME
docker/run.sh \
    -v $JETSON_SERVICE_HOME:/jetson-service \
    -r bash /jetson-service/ci/project/run.sh
