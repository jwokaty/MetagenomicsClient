# MetagenomicsClient

API client for curated metagenomics

https://hub.docker.com/repository/docker/waldronlab/metagenomicsclient

```bash
docker run --rm --init -it  --user=$(id -u):$(id -g)   --volume "$HOME:$HOME"   --volume="/etc/group:/etc/group:ro"   --volume="/etc/passwd:/etc/passwd:ro"   --volume="/etc/shadow:/etc/shadow:ro"    --volume="/etc/sudoers.d:/etc/sudoers.d:ro"  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"   --workdir="`pwd`"   waldronlab/metagenomicsclient bash

openapi-python-client generate --url https://cmgd-telemetry-whnnxetv4q-uc.a.run.app/openapi.json
```
