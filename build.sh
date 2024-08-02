#!/bin/bash
set -e
set -x
git diff
./devenv_exec python show-version.py
./devenv_exec python -m build
