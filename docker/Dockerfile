# Single-user notebook image for the Elestio JupyterHub (DockerSpawner).
# Built from the pixi `image` environment (pixi.lock). Build context = repo root:
#   docker build -f docker/Dockerfile -t workshop-notebook .
# CI (.github/workflows/build-notebook-image.yml) is the authoritative build.

FROM ghcr.io/prefix-dev/pixi:0.69.0 AS build
WORKDIR /app
COPY pixi.toml pixi.lock ./
RUN pixi install --locked -e image
# Pure activation script (sets PATH + conda/proj/gdal env vars for the geo stack).
RUN pixi shell-hook -e image -s bash > /activate.sh
# Entrypoint: activate the pixi env, auto-load the workshop materials into the
# user's workspace (clone on first login, non-destructive merge after), then run
# the spawner's command. `|| true` so a GitHub hiccup never blocks server start.
RUN cp /activate.sh /entrypoint.sh && printf '%s\n' \
    'gitpuller https://github.com/pypsalabs/workshop-202609 main /home/jovyan/work/workshop-202609 || true' \
    'exec "$@"' >> /entrypoint.sh

FROM debian:bookworm-slim AS runtime
# The pixi env prefix must stay at the same absolute path as in the build stage
# (the shell-hook bakes it in).
COPY --from=build /app/.pixi/envs/image /app/.pixi/envs/image
COPY --from=build /entrypoint.sh /entrypoint.sh
# Activate the env for login shells too (e.g. a JupyterLab terminal).
COPY --from=build /activate.sh /etc/profile.d/pixi.sh
COPY docker/jupyter_server_config.py /etc/jupyter/jupyter_server_config.py
RUN useradd -m -u 1000 -s /bin/bash jovyan \
    && mkdir -p /home/jovyan/work \
    && chown -R jovyan:jovyan /home/jovyan
# PATH fallback for non-login shells; profile.d handles full activation for login shells.
ENV PATH=/app/.pixi/envs/image/bin:$PATH
ENV JUPYTER_CONFIG_DIR=/etc/jupyter
WORKDIR /home/jovyan/work
# No fixed USER: the Elestio spawner forces user=0; allow_root handles it.
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["jupyterhub-singleuser"]
