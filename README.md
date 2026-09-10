# my-research-project

This project demonstrates a simple research goal -- fetching CRSP.MSF data with control over daterange -- and provides the necessary support structure in order to run on the WRDS Cloud.

## Project components:

- `get_msf.py` - core Python program to wrap wrds module `raw_sql()` call to fetch CRSP.MSF constrained by start and end date.
- `get_msf.sh` - Bash wrapper script, submitted to Grid Engine with `qsub`, which then submits actual code file `get_msf.py`
- `requirements.txt` - Python package requirements to run `get_msf.py`, created with `python3 -m pip freeze`, can be easily installed with `python3 -m pip install -r requirements.txt`

## Usage

1. Once you have created a GitHub account, and set up your WRDS Cloud environment to be able to communicate with GitHub, clone this repo to your WRDS Cloud home directory with `git clone git@github.com:andf1/my-research-project.git` (or use HTTPS if desired)
2. Change directory to your cloned repo: `cd my-research-project`
3. Run this code: `qsub get_msf.sh`
