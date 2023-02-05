#!/bin/bash
set -e

if [[ "$1" = "serve" ]]; then
    shift 1
    printenv
    ls /opt/ml/model
    torch-model-archiver --model-name intel_scene \
        --version 1.0 \
        --serialized-file "/opt/ml/model/model.scripted.pt" \
        --handler "intel_scene_handler.py" \
        --extra-files "index_to_name.json"
    mv intel_scene.mar model-store/
    export ENABLE_TORCH_PROFILER=true
    torchserve --start --model-store model-store --models scene_model=intel_scene.mar --ts-config config.properties
else
    "$@"
fi

# prevent docker exit
tail -f /dev/null

torch-model-archiver --model-name intel_scene --version 1.0 --serialized-file "/opt/ml/model/delete/model.scripted.pt" --handler "/opt/ml/model/intel_scene_handler.py" --extra-files "index_to_name.json"

    mv intel_scene.mar model-store/
    export ENABLE_TORCH_PROFILER=true
    torchserve --start --model-store model-store --models scene_model=intel_scene.mar --ts-config config.properties
