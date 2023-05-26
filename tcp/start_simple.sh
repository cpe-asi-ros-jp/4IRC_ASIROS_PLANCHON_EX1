#!/usr/bin/env bash
(trap 'kill 0' SIGINT; \
    python3 tcp_controller_simple.py | sed 's/^/[CONTROLLER SIMPLE]: /' & \
    sleep 1 && python3 tcp_equipment_simple.py | sed 's/^/[EQUIPMENT SIMPLE]: /')