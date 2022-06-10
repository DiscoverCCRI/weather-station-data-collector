Authors: Yiwei Zhang, NAU IoT (Duane Booher, Jacob Hagan)

# Introduction 
This repository contains sample code to read and collect Seeed SenseCAP ONE S900 Compact Weather Station data within a Docker container. The purpose of this code is to support the Discover project at Northern Arizona University.

Users may use this code as a starting point for any experiments that may utilize the Seeed SenseCAP ONE S900 Compact Weather Station.

# Getting Started
The following steps outline the dependencies for the project and provide installation instructions to get the project running on a local device. 

## Hardware
The system that was used to host this project is a Raspberry Pi 3 Model B running Ubuntu Server 20.04, with a [Seeed SenseCAP ONE S900 Compact Weather Station](https://files.seeedstudio.com/products/101990784/SenseCAP%20ONE%20Compact%20Weather%20Sensor%20User%20Guide-v1.6.pdf) attached via USB using a (TODO: name of the adapter that Yiwei wired up).

(TODO: add image of the wiring & adapter)

## Installation process
Clone this repository:

```
git clone https://github.com/DiscoverCCRI/weather-station-test1.git
```

## Software dependencies
Since this is a container-based application, the only dependency is Docker. Use the apt package manager to install it:

```
sudo apt install docker.io
```

## Latest releases
TODO: Make a latest release entry for version 1.0. Explain current design.


# Build and Test
With the repo pulled down and Docker installed, we can begin building and running the application.

Navigate to the directory that the repository was cloned to and build the Docker image:
```
cd weather-station-test1
sudo docker build --rm -t weather-station-read .
```
* `--rm ` : Remove intermediate containers after a successful build.
* `-t weather-station-read` : Assign a name to the Docker image that will be built.

This application requires a volume to be allocated in order to store weather station readings. Execute the following command:
```
sudo docker volume create experiment-data
```

Once the volume has been created, we can run the Docker container:
```
sudo docker run --device=/dev/ttyUSB0 -v experiment-data:/data -t -i -d weather-station-read
```
* `--device=/dev/ttyUSB0` : Gives the container permission to access to the weather station device.
* `-v experiment-data:/data` : Mounts the 'experiment-data' volume to '/data' in the container's file system.
* `-t` : Allocate a pseudo-tty.
* `-i` : Keep STDIN open even if not attached.
* `-d` : Start the container in detached mode.

TODO: Explain how to view cron.log (docker logging) and explain how to view the data (this could be in the same way that Duane explained it --> run ubuntu container with shared volume mounted, check out the data)

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)

This section can talk about plans for the future:
* Docker Compose w/ an MQTT container to deliver weather station data over MQTT.
    * Is this relevant to the flow? Data may be communicated with the end user through the testbed portal... Maybe MQTT can be utilized for experiment updates?

=================================
