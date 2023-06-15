# Jetson Nano Service Guide

## Setting Up

1. Log into your Jetson Nano

```bash
vidianiv@192.168.1.43
```

2. Create `dev` directory end go there
   
```bash
cd ~
mkdir dev
cd dev
```

3. Get `Jetson Inference` sources.
   
```bash
git clone https://github.com/dusty-nv/jetson-inference.git
```

4. Get `VIDIANIV` project monorepo and name directory `vidianiv`.
   
```bash
git clone https://gitlab.se.ifmo.ru/vidianiv/projects.git vidianiv
```

5. Set up environment variables.

```bash
source vidianiv/prototype/jetson-service/ci/jetson/envsetup
printenv | egrep "JETSON"
```

6. Run `jetson-service`.

```bash
bash $JETSON_SERVICE_HOME/ci/jetson/start.sh
```
