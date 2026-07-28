#!/usr/bin/env python3
"""Control esp32s3-car-1 from Python (``MobileRobot``) instead of ``rosie drive``.

Prerequisites (same as the CLI path):

1. Flash the car (``rosie mcu flash``) and power it on
2. Join SoftAP **ESP32S3-Car-1** / password ``esp32s3-car-1``
   (or your station Wi‑Fi if you changed ``network`` in ``robot.yaml``)
3. In another terminal: ``rosie router``

Run from this directory::

    python drive_demo.py

Identity (``robot`` / ``fleet`` / teleop defaults) comes from ``robot.yaml``.
Host connect stays on the local router — SoftAP MCU uses ``network.connect``
from YAML (``tcp/192.168.4.2:7447``); the laptop talks to ``127.0.0.1``.
"""

from __future__ import annotations

from pathlib import Path

from rosie import MobileRobot

HERE = Path(__file__).resolve().parent
ROBOT_YAML = HERE / "robot.yaml"
# Laptop → local zenohd. Do not use robot.yaml's network.connect (that is for the MCU).
HOST_CONNECT = "tcp/127.0.0.1:7447"


def main() -> None:
    print("Opening MobileRobot (zenohd / `rosie router` must be running)...")
    bot = MobileRobot(
        config_path=ROBOT_YAML,
        connect=HOST_CONNECT,
        name="drive_demo",
    )
    try:
        print(f"Robot id: {bot.robot_id}")
        pose = bot.wait_for_pose(timeout_s=5.0)
        if not pose:
            raise SystemExit(
                "No pose yet — is the car on the bus? "
                "Reset the board if it connected before the router was up."
            )
        print(
            f"Linked. pose x={pose.get('x', 0):.3f} y={pose.get('y', 0):.3f} "
            f"mode={pose.get('mode', '?')}"
        )

        bot.zero()
        print("Pose zeroed at current location.")

        # Short desk move — raise distances once you have clear floor space.
        print("drive_to (2, 1) m ...")
        bot.drive_to(2, 1)

        print("drive_route — small L ...")
        bot.drive_route([(0.5, 0.5), (0.0, 0.5), (0.0, 0.0)])

        print("Done. Final pose:", bot.pose())
    except KeyboardInterrupt:
        print("\nInterrupted — sending stop.")
        bot.stop()
    finally:
        bot.close()


if __name__ == "__main__":
    main()
