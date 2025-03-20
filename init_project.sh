#!/usr/bin/env bash

set -e


# allow for using system packages
poetry config virtualenvs.options.system-site-packages true

# Create symbolic links to files
ln -sf src/f1tenth_system/docs/ros_start/Makefile ../../Makefile
ln -sf src/f1tenth_system/docs/ros_start/README.md ../../README.md
ln -sf src/f1tenth_system/pyproject.toml ../../pyproject.toml
ln -sf src/f1tenth_system/.install.stamp ../../.install.stamp

# install poetry environment
make install