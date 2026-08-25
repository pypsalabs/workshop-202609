# Local Installation (optional)

You do not need a local installation if you are using Google Colab. For a local setup, first get a copy of the workshop repository by running:

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

## Option B: Using `conda`

If you already use [Anaconda or
miniconda](https://www.anaconda.com/docs/getting-started/getting-started), you
can create the workshop environment from one of the provided **pinned** lock
files. These list exact package versions so that everyone has the same
environment, and they depend on your operating system.

In the root folder of the workshop repository, run the command matching your
system:

For **Windows**:

```sh
conda env create -f envs/win-64.lock.yaml
```

For **macOS** (Intel/AMD):

```sh
conda env create -f envs/osx-64.lock.yaml
```

For **macOS** (Apple Silicon):

```sh
conda env create -f envs/osx-arm64.lock.yaml
```

For **Linux**:

```sh
conda env create -f envs/linux-64.lock.yaml
```

:::{note}
This process may take some time. If the environment cannot be created from the
pinned file, try the unpinned
[`envs/environment.yaml`](https://github.com/pypsalabs/workshop-202609/blob/main/envs/environment.yaml)
instead.
:::

Then **activate** the environment and start Jupyter Lab:

```sh
conda activate workshop-202609
jupyter lab
```

:::{warning}
The activation step has to be repeated whenever you open a new terminal; it is
not persistent across terminal sessions.
:::
