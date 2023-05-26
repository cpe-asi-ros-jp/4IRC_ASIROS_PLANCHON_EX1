#!/usr/bin/env bash
(trap 'kill 0' SIGINT; \
    python3 udp_controller_video.py | sed 's/^/[CONTROLLER VIDEO]: /' & \
    python3 udp_equipment_video.py | sed 's/^/[EQUIPMENT VIDEO]: /')