# F1Tenth System Project


## Building the ROS project

1. Configure your project to be able to use the system packages with `uv venv --system-site-packages`. This must be set BEFORE the project is installed.
1. Install the virtual environment with `uv sync`
1. Activate the virtual environemnt with `sourace .venv/bin/activate`
1. `cd` back to the project workspace (where you can see the `src` folder)
1. Build the project with `python -m colcon build --symlink-install`
1. Source the project with `source install/setup.bash` or `source install/setup.zsh`
1. Run your launch file, e.g., `ros2 launch f1tenth_system <launch file here>`, for example: `ros2 launch f1tenth_system bringup_base_launch.py`


## Getting started

This is the top level for `f1tenth-system` project. The `Makefile` has useful commands for getting started. Any command with the prefix `run_` assumes that the project has already been built and the executables source.
- `make clean` -- remove the `build/`, `log/`, `install/` folders
- `make build` -- builds the ROS2 project with `colcon` and sources the paths (assuming `zsh` for the shell)
- `make run_manual` -- Runs the manual-only mode (i.e., no option for autonomous mode)
- `make run_wiggle` -- Runs the wiggle open-loop control mode (i.e. the S-curve)


## Troubleshooting

Report any issues to Spencer!