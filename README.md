<h1 align="center">
    <img src="./images/apptainer_logo.png" width="200" height="200" alt="Apptainer Logo">
    <br>
    <br>
    Apptainer
</h1>

<p align="center">
    <b>This is the snap package for Apptainer</b>, 
    an open-source container system for High-Performance Computing.
</p>

> The upstream Apptainer repository can be
> located [here](https://github.com/apptainer/apptainer)

## Installation

### Install from the Snap Store

> The Apptainer snap package has not been released to the Snap Store yet.

### Building the snap yourself

Use the following commands to build the Apptainer snap package locally.
It is assumed that you already have `snapd` installed on your system. If not, you
can find instructions for installing `snapd` on your system 
[here](https://snapcraft.io/docs/installing-snapd):

1. Install `tox` and `snapcraft` on your system

```commandline
sudo apt install tox
sudo snap install snapcraft --channel=edge --classic
```

2. Clone the repository

```commandline
git clone https://github.com/canonical/apptainer
```

3. Use `tox` to build the snap

```commandline
tox -e snap
```

4. Install

```commandline
tox -e install
```

## Usage

The Apptainer snap is intended to be one-for-one compatible with the upstream Apptainer;
therefore, you can refer to the [official Apptainer documentation](https://apptainer.org/docs/user/main/)
for usage information.

