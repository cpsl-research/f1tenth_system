NAME := f1tenth
POETRY := $(shell command -v poetry 2> /dev/null)
SHELL := /bin/zsh
.DEFAULT_GOAL := help


.PHONY: help
help:
		@echo "Please use 'make <target>' where <target> is one of"
		@echo ""
		@echo "  clean       remove all temporary files"
		@echo "  activate    activates the poetry environment"
		@echo "  build       build the project with colcon"
		@echo ""
		@echo "Check the Makefile to know exactly what each target is doing."


.PHONY: clean
clean:
	rm -rf build/ install/ log/


.PHONY: activate
activate:
	# NOTE: assumes you are at the top level of the ROS project
	cd src/f1tenth_system && poetry shell


.PHONY: build
build:
	python -m colcon build --symlink-install
	source install/setup.zsh


.PHONY: run_manual
run_manual:
	ros2 launch f1tenth_stack bringup_base_launch.py


.PHONY: run_wiggle
run_wiggle:
	ros2 launch f1tenth_stack bringup_auto_wiggle_launch.py