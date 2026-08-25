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

Dependencies are declared in `pyproject.toml` for uv/pip and
`envs/environment.yaml` for conda. Reproducible installations use:

- `uv.lock` with `uv sync`
- `requirements.lock` with `pip install -r requirements.lock`
- `envs/<platform>.lock.yaml` with `conda env create -f envs/<platform>.lock.yaml`

Changes to the dependency specifications trigger an automated lockfile update
pull request. Pushes to `main` build and deploy the website through GitHub
Actions. Participant-facing installation instructions are in `bham/setup.md`.

## Credits

This workshop is created using the open
source [Jupyter Book project](https://jupyterbook.org/).

## License

Code and notebooks are licensed under MIT (see `LICENSE`); textual content is CC-BY-4.0.
