# Rosie demos

Example robots and projects that use the [Rosie](https://github.com/rosie-framework/rosie)
framework. Each subdirectory is a self-contained robot project: edit
`robot.yaml`, flash with `rosie mcu`, drive with `rosie drive`.

Rosie itself lives in a **separate** repository — install it first, then open a
demo folder.

## Install Rosie (once)

From a Rosie checkout (recommended while developing Rosie + demos on one machine):

```bash
pip install -e "/path/to/rosie/python[mcu]"           # required: flash / build
# optional: OpenCV for `rosie drive` snap / live camera view
# pip install -e "/path/to/rosie/python[mcu,camera]"
# Quote the path — zsh treats [...] as a glob.
rosie setup
```

Or from a released package (when published):

```bash
pip install "rosie-framework[mcu]"
# pip install "rosie-framework[mcu,camera]"
rosie setup
```

## Demos

| Demo | Hardware | Notes |
|------|----------|--------|
| [esp32s3-car-1](esp32s3-car-1/) | Freenove ESP32-S3 CAM + TB6612 + encoders + MPU6050 | DiffDriveStack reference car |

## Typical workflow

```bash
cd esp32s3-car-1
rosie mcu setup && rosie mcu flash
rosie router                  # terminal 1 — Zenoh bus
rosie drive --config robot.yaml   # terminal 2 — interactive REPL
# or: python drive_demo.py        # terminal 2 — scripted MobileRobot
```

Follow each demo’s README for network bring-up (e.g. SoftAP). Edit that
demo’s `robot.yaml` for pins, Wi‑Fi, and gains.

## Docs

- [Getting started](https://github.com/rosie-framework/rosie/blob/main/docs/getting-started.md)
- [BYOR](https://github.com/rosie-framework/rosie/blob/main/docs/byor.md)
- [Mobile base](https://github.com/rosie-framework/rosie/blob/main/docs/mobile-base.md)
- [Fleet networking](https://github.com/rosie-framework/rosie/blob/main/docs/fleet-networking.md)

