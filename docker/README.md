# Single-user notebook image

The image JupyterHub spawns for each workshop participant on the Elestio VM. It
bakes the pixi `image` environment (`pixi.lock`) plus `jupyterhub-singleuser`, and
the workshop notebooks themselves. Docker copies the notebooks into each fresh
per-user volume on first login, so a participant's workspace starts with the
notebooks and PyPSA + HiGHS ready, no install and no clone step.

Build from the repo root (context must be the root so `pixi.toml`/`pixi.lock`
are in scope):

```sh
docker build -f docker/Dockerfile -t workshop-notebook .
```

CI (`.github/workflows/build-notebook-image.yml`) builds and pushes it to
`ghcr.io/pypsalabs/workshop-notebook` on every change to `docker/**`,
`pixi.toml`, or `pixi.lock`. The Elestio spawner pulls it via the
`DOCKER_NOTEBOOK_IMAGE` env var.
