#!/usr/bin/env bash
(trap 'kill 0' SIGINT; \
    python3 tcp_controller_video.py | sed 's/^/[CONTROLLER VIDEO]: /' & \
    sleep 1 && python3 tcp_equipment_video.py | sed 's/^/[EQUIPMENT VIDEO]: /')