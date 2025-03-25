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

check-poetry:
	@if [ $(shell which poetry | grep poetry | wc -l) -gt 0 ]; then \
		echo "Poetry is installed."; \
	else \
		echo "Poetry is not installed. Please install it."; \
		exit 1; \
	fi


check-env: check-poetry
	@poetry env info --path > /dev/null 2>&1 || { echo "Poetry environment is not activated, \
	run 'make activate' first, then go back two directories"; exit 1; } \


activate: check-poetry
	@if poetry env info --path > /dev/null 2>&1; then \
		echo "Poetry environment is activated."; \
	else \
	    echo "Poetry environment is not activated. Activating..."; \
		cd src/f1tenth_system; \
		poetry shell || { echo "Failed to activate Poetry environment."; exit 1; } \
	fi

build: check-env
	python -m colcon build --symlink-install
	source install/setup.zsh

run_manual: check-env
	ros2 launch f1tenth_stack bringup_base_launch.py

run_straight: check-env
	ros2 launch f1tenth_stack bringup_auto_straight_launch.py

run_roomba: check-env
	ros2 launch f1tenth_stack bringup_auto_roomba_launch.py

run_wiggle: check-env
	ros2 launch f1tenth_stack bringup_auto_wiggle_launch.py
