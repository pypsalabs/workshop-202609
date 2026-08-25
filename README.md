# PyPSA Workshop Birmingham (September 2026)

Workshop materials for learning energy system modelling with
[PyPSA](https://pypsa.org).

The materials are published as a [Jupyter Book 2](https://jupyterbook.org)
(MyST) website via GitHub Pages.

## Usage

### Building the book

If you'd like to develop and/or build the book, you should:

1. Clone this repository
2. Run `uv sync`
3. (Optional) Edit the book's source files located in the `bham/` directory
4. Run `uv run jupyter book start` for a live preview, or
   `uv run jupyter-book build --html --execute` for a full build

A fully-rendered HTML version of the book will be built in `_build/html/`.

### Deployment

The book is built and deployed to GitHub Pages automatically on every push to
`main` (see `.github/workflows/deploy.yml`). Ensure the repository's GitHub
Pages settings are set to deploy with **GitHub Actions**.

### Environments

The direct dependencies are declared in `pyproject.toml` (pip/uv world) and
`envs/environment.yaml` (conda world). All pinned lockfiles are generated
automatically by `.github/workflows/update-pinned-env.yaml`, which opens a
pull request whenever the loose specifications change:

- `uv.lock` — used by `uv sync` (CI and uv users)
- `requirements.lock` — for plain pip users (`pip install -r requirements.lock`)
- `envs/{linux-64,osx-64,osx-arm64,win-64}.lock.yaml` — pinned per-platform
  conda environments (`conda env create -f envs/<platform>.lock.yaml`)

Participant-facing installation instructions live in `bham/setup.md`.

## Credits

This workshop is created using the open
source [Jupyter Book project](https://jupyterbook.org/).

## License

Code and notebooks are licensed under MIT (see `LICENSE`); textual content is CC-BY-4.0.
