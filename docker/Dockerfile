# Single-user notebook image for the Elestio JupyterHub (DockerSpawner).
# Built from the pixi `image` environment (pixi.lock). Build context = repo root:
#   docker build -f docker/Dockerfile -t workshop-notebook .
# CI (.github/workflows/build-notebook-image.yml) is the authoritative build.

FROM ghcr.io/prefix-dev/pixi:0.69.0 AS build
WORKDIR /app
COPY pixi.toml pixi.lock ./
RUN pixi install --locked -e image
# Entrypoint: activate the pixi env, auto-load the workshop materials into the
# user's workspace (clone on first login, non-destructive merge after), then run
# the spawner's command. `|| true` so a GitHub hiccup never blocks server start.
RUN pixi shell-hook -e image -s bash > /entrypoint.sh && printf '%s\n' \
    'gitpuller https://github.com/pypsalabs/workshop-202609 main /home/jovyan/work/workshop-202609 || true' \
    'exec "$@"' >> /entrypoint.sh

FROM debian:bookworm-slim AS runtime
# The pixi env prefix must stay at the same absolute path as in the build stage
# (the shell-hook bakes it in).
COPY --from=build /app/.pixi/envs/image /app/.pixi/envs/image
COPY --from=build /entrypoint.sh /entrypoint.sh
COPY docker/jupyter_server_config.py /etc/jupyter/jupyter_server_config.py
RUN useradd -m -u 1000 -s /bin/bash jovyan \
    && mkdir -p /home/jovyan/work \
    && chown -R jovyan:jovyan /home/jovyan
ENV JUPYTER_CONFIG_DIR=/etc/jupyter
WORKDIR /home/jovyan/work
# No fixed USER: the Elestio spawner forces user=0; allow_root handles it.
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["jupyterhub-singleuser"]
