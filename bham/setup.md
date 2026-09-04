# Local Installation (optional)

You do not need a local installation if you are using the workshop JupyterHub or Google Colab. For a local setup, first get a copy of the workshop repository by running:

```sh
git clone https://github.com/pypsalabs/workshop-202609.git
```

or by downloading the repository as a ZIP file (look for a green "Code" button
at https://github.com/pypsalabs/workshop-202609) and extracting it to a local
folder.

Then pick **one** of the two options below.

## Option A: Using `uv` (recommended)

Install `uv` following its [installation
instructions](https://docs.astral.sh/uv/getting-started/installation/) for your
operating system, and verify that it works:

```sh
uv --version
```

Then, in the root folder of the workshop repository (where the `pyproject.toml`
and `uv.lock` files are located), install all required packages and set up the
environment with a single command:

```sh
uv sync
```

Once this is done, you can start a Jupyter Lab session in your browser with
this environment:

```sh
uv run jupyter lab
```

## Option B: Using `pixi`

Install [`pixi`](https://pixi.sh) following its [installation
instructions](https://pixi.sh/latest/installation/), and verify that it works:

```sh
pixi --version
```

Then, in the root folder of the workshop repository (where the `pixi.toml` and
`pixi.lock` files are located), install the environment from the committed lock
file. This gives everyone the same **pinned** package versions for their
operating system:

```sh
pixi install
```

Once this is done, start a Jupyter Lab session in this environment:

```sh
pixi run jupyter lab
```

:::{note}
No activation step is needed. `pixi run` always uses the project environment, so
it works the same in every new terminal.
:::
