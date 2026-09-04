# PyPSA Workshop Birmingham (September 2026)

Materials for a hands-on energy system modelling workshop at the
[University of Birmingham](https://www.birmingham.ac.uk/), externally hosted by
the [Supergen Energy Networks Hub](https://supergenen.org/) and delivered by
[PyPSA Labs](https://pypsalabs.org/) staff. See the
[workshop listing and agenda](https://pypsalabs.org/services/training).

The materials are published as a [Jupyter Book 2](https://jupyterbook.org)
(MyST) website at
[pypsalabs.github.io/workshop-202609](https://pypsalabs.github.io/workshop-202609/).

## Usage

### Develop locally

Install [`uv`](https://docs.astral.sh/uv/), clone the repository, and run:

```sh
uv sync
uv run jupyter book start
```

This serves a local live preview. Workshop sources are in `bham/`. To execute all notebooks and create the deployable site in
`_build/html/`, run:

```sh
uv run jupyter-book build --html --execute
```

### Environments and deployment

Dependencies are declared in `pyproject.toml` for uv/pip and `pixi.toml` for
pixi (conda-forge). Reproducible installations use:

- `uv.lock` with `uv sync`
- `requirements.lock` with `pip install -r requirements.lock`
- `pixi.lock` with `pixi install` (run `pixi update` to refresh it)

Pushes to `main` build and deploy the website through GitHub Actions. A separate
workflow (`.github/workflows/build-notebook-image.yml`) builds the single-user
notebook image for the workshop JupyterHub from the pixi `image` environment and
pushes it to GHCR. Lockfiles are generated locally and committed when
dependencies change. Participant-facing installation instructions are in
`bham/setup.md`.

## Credits

Some of the workshop materials are adapted from Fabian Neumann's fantastic
[Data Science for Energy System Modelling](https://fneum.github.io/data-science-for-esm/)
course at TU Berlin.

The workshop also draws on examples and explanations from the
[PyPSA documentation](https://docs.pypsa.org/).

This workshop is created using the open-source
[Jupyter Book project](https://jupyterbook.org/).

## License

Code and notebooks are licensed under MIT (see `LICENSE`); textual content is CC-BY-4.0.
