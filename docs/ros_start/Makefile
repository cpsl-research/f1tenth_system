NAME := f1tenth
POETRY := $(shell command -v poetry 2> /dev/null)
UV := $(shell command -v uv 2> /dev/null)
SHELL := /bin/zsh
.DEFAULT_GOAL := help


.PHONY: help
help:
		@echo "Please use 'make <target>' where <target> is one of"
		@echo ""
		@echo "  clean       remove all temporary files"
		@echo "  activate    activates the uv environment"
		@echo "  build       build the project with colcon"
		@echo ""
		@echo "Check the Makefile to know exactly what each target is doing."

.PHONY: clean
clean:
	rm -rf build/ install/ log/

check-uv:
	@if [ $(shell which uv | grep uv | wc -l) -gt 0 ]; then \
		echo "UV is installed."; \
	else \
		echo "UV is not installed. Please install it."; \
		exit 1; \
	fi

.PHONY: build
build:
	cd src/f1tenth_system; \
	source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; }; \
	cd ../..; \
	python -m colcon build --symlink-install; \

.PHONY: run_manual
run_manual:
	source install/setup.zsh \
	cd src/f1tenth_system; \
	source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; }; \
	cd ../..; \
	ros2 launch f1tenth_bringup bringup_base_launch.py

.PHONY: run_straight
run_straight:
	source install/setup.zsh \
	cd src/f1tenth_system; \
	source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; }; \
	cd ../..; \
	ros2 launch f1tenth_bringup bringup_auto_straight_launch.py

.PHONY: run_roomba
run_roomba:
	source install/setup.zsh \
	cd src/f1tenth_system; \
	source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; }; \
	cd ../..; \
	ros2 launch f1tenth_bringup bringup_auto_roomba_launch.py

.PHONY: run_wiggle
run_wiggle:
	source install/setup.zsh \
	cd src/f1tenth_system; \

.PHONY: run_follower
run_follower:
	source install/setup.zsh \
	cd src/f1tenth_system; \
	source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; }; \
	cd ../..; \
	ros2 launch f1tenth_bringup bringup_auto_follower_launch.py
