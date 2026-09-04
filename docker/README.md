# Single-user notebook image

The image JupyterHub spawns for each workshop participant on the Elestio VM. It
bakes the pixi `image` environment (`pixi.lock`) plus `jupyterhub-singleuser` and
`nbgitpuller`, so participants get PyPSA + HiGHS with no install step.

Build from the repo root (context must be the root so `pixi.toml`/`pixi.lock`
are in scope):

```sh
docker build -f docker/Dockerfile -t workshop-notebook .
```

CI (`.github/workflows/build-notebook-image.yml`) builds and pushes it to
`ghcr.io/pypsalabs/workshop-202609-notebook` on every change to `docker/**`,
`pixi.toml`, or `pixi.lock`. The Elestio spawner pulls it via the
`DOCKER_NOTEBOOK_IMAGE` env var.
