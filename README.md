# Camera Streaming app
A project for streaming the video contents of a camera connected to a raspberry pi to a mobile phone.
This README file provides the main documentation for the setup of this project. 
It is divided in several sections, starting with the hardware below.

## Hardware
In order to stream the video contents of a camera to a phone, the following devices are required:
- **Video camera:** I've chosen for a [Raspberry pi Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/1), 
  which has two variants, [the standard version](https://www.raspberrypi.org/products/camera-module-v2/), 
  and the [NoIR version](https://www.raspberrypi.org/products/pi-noir-camera-v2/) (NoIR stands for No Infrared Filter).
  Both modules are around € 20,00 (excluding shipping) and will work with all Raspberry Pi models that have a CSI connector 
  (all except Raspberry Pi 400 and the 2016 launch version of Zero).
- **Raspberry pi:** for setting up a webserver that sends the video contents to a phone. 
  I already have a [Raspberry Pi 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/), 
  so I decided to use this one for this project. 
- **A phone:** (or browser) for seeing the video content. 
  This repository also provides a mobile application, implemented in [React Native](https://reactnative.dev/), 
  which means that it will work on iOS an Android. It is only tested (and used) on an Android phone.

## Software
In order to stream the video contents of a camera to a phone, the following software is required:
- **A webservice** for broadcasting the video data. See [raspberry-pi](/raspberry-pi)-folder for more information.
- **A mobile application** for displaying the video data.

# Installation

## Getting started
Below are some commands to get you started on every device.

### Raspberry pi:
```shell
git clone git@github.com:FlyingBird95/camera-streaming-app.git
cd camera-streaming-app/raspberry-pi
python3 -m venv env         # Create a virtual environment. We assume you have python3 and pip installed. 
source env/bin/activate     # Activate the virtual environment. 
pip install --upgrade pip   # Use latest pip to ensure compatibility with pyproject.toml.
pip install .               # Install project and testing dependencies. 
gunicorn streamer.wsgi:app  # Run the server.
```

## Contributing
In order to contribute to this project, I encourage you to fork this repository and send a PR with improvements.
To getting started, perform the following steps:

```shell
git clone git@github.com:<your-fork>/camera-streaming-app.git
cd camera-streaming-app/raspberry-pi
python3 -m venv env         # Create a virtual environment. We assume you have python3 and pip installed. 
source env/bin/activate     # Activate the virtual environment. 
pip install --upgrade pip   # Use latest pip to ensure compatibility with pyproject.toml.
pip install -e .[testing]   # Install project and testing dependencies. 
gunicorn streamer.wsgi:app  # Run the server.
```