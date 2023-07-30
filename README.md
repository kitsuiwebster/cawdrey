# Cawdrew

## Purpose

This script is designed to generate all possible permutations of a user-defined set of characters, within a user-defined length range. The purpose of this script could be to create a list of all possible words, which can be used for purposes such as password cracking, testing, or similar applications where such a comprehensive list might be useful.

## Prerequisites

### Python

Ensure you have Python 3.6 or higher installed. You can download Python from the official site: [Download Python](https://www.python.org/downloads/)

### Pip

Windows:

`python get-pip.py`

Debian/Ubuntu:

`sudo apt install python3-pip`

Fedora:

`sudo dnf install python3-pip`

CentOS:

`sudo yum install python3-pip`

Arch Linux:

`sudo pacman -S python-pip`

## Installing Dependencies

You need to install `yaspin`, a terminal spinner library for Python. Open your terminal and run:

```bash
pip install yaspin
```

## Install and run the script

```bash
git clone https://gitlab.com/kitsuiwebster/cawdrey.git
```

```bash
cd cawdrey
```

Windows:

`python cwadrew.py`

Linux: 

`python3 cawdrew.py`


**Note**: Generating words with large lengths and/or charsets can take a considerable amount of time and disk space. Be aware of this before starting the operation.
