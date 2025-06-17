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


# check-env: check-uv
# 	@uv env info --path > /dev/null 2>&1 || { echo "UV environment is not activated, \
# 	run 'make activate' first, then go back two directories"; exit 1; } \


# activate: check-uv
# 	@if uv env info --path > /dev/null 2>&1; then \
# 		echo "UV environment is activated."; \
# 	else \
# 	    echo "UV environment is not activated. Activating..."; \
# 		cd src/f1tenth_system; \
# 		source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; } \
# 	fi

.PHONY: build
build:
	cd src/f1tenth_system; \
	source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; }; \
	cd ../..; \
	python -m colcon build --symlink-install; \
	source install/setup.zsh \

.PHONY: run_manual
run_manual:
	cd src/f1tenth_system; \
	source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; }; \
	cd ../..; \
	ros2 launch f1tenth_stack bringup_base_launch.py

.PHONY: run_straight
run_straight:
	cd src/f1tenth_system; \
	source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; }; \
	cd ../..; \
	ros2 launch f1tenth_stack bringup_auto_straight_launch.py

.PHONY: run_roomba
run_roomba:
	cd src/f1tenth_system; \
	source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; }; \
	cd ../..; \
	ros2 launch f1tenth_stack bringup_auto_roomba_launch.py

.PHONY: run_wiggle
run_wiggle:
	cd src/f1tenth_system; \
	source .venv/bin/activate || { echo "Failed to activate UV environment."; exit 1; }; \
	cd ../..; \
	ros2 launch f1tenth_stack bringup_auto_wiggle_launch.py
