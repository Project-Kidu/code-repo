FROM pytorch/torchserve

USER root
COPY build_artifacts/dockerd-entrypoint.sh /home/model-server/dockerd-entrypoint.sh
RUN chmod +x /home/model-server/dockerd-entrypoint.sh

COPY build_artifacts/config.properties /home/model-server/config.properties
COPY build_artifacts/index_to_name.json /home/model-server/index_to_name.json
COPY build_artifacts/intel_scene_handler.py /home/model-server/intel_scene_handler.py

ENTRYPOINT ["/home/model-server/dockerd-entrypoint.sh"]
CMD ["serve"]
