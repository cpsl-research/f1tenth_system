# F1Tenth System Project


## Getting started

This is the top level for `f1tenth-system` project. The `Makefile` has useful commands for getting started. Any command with the prefix `run_` assumes that the project has already been built and the executables source.
- `make clean` -- remove the `build/`, `log/`, `install/` folders
- `make build` -- builds the ROS2 project with `colcon` and sources the paths (assuming `zsh` for the shell)
- `make run_manual` -- Runs the manual-only mode (i.e., no option for autonomous mode)
- `make run_wiggle` -- Runs the wiggle open-loop control mode (i.e. the S-curve)


## Troubleshooting

Report any issues to Spencer!