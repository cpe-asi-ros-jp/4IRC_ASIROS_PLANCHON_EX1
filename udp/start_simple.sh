#!/usr/bin/env bash
(trap 'kill 0' SIGINT; \
    python3 udp_controller_simple.py | sed 's/^/[CONTROLLER SIMPLE]: /' & \
    python3 udp_equipment_simple.py | sed 's/^/[EQUIPMENT SIMPLE]: /')