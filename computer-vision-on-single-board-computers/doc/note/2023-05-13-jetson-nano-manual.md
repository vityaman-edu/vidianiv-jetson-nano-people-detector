# Jetson Nano Manual

## Table of contents

- [Jetson Nano Manual](#jetson-nano-manual)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [Connection](#connection)
    - [Using USB](#using-usb)
    - [Using SSH](#using-ssh)
  - [Docker Setup](#docker-setup)
  - [Reference](#reference)

## Installation

Install Jetson Nano Ubuntu image
following [official guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write).

## Connection

This chapter describes how to connect
to running Jetson Nano via either
USB or SSH.

### Using USB

First of all you need a USB to Micro USB
wire, it will be used to connect to Jetson.

Next install `screen` utility.

```bash
sudo apt-get install -y screen
```

Then connect you computer to Jetson via
that wire and run.

```bash
dmesg | grep --color 'tty'
ls -l /dev/ttyACM0
sudo screen /dev/ttyACM0 115200
```

Wait a bit, enter login and password
and you are done!

### Using SSH

Also you can connect to jetson using
ssh, but first you need some setup.

Connect Jetson and your desktop to
the same wireless network to be explorable
for each other.

Get Jetson Nano IP address.

```bash
nmcli

# Example output:
#
# vidianiv@ubuntu:~$ nmcli
# wlan0: connected to __private 1
#     "Realtek 802.11n WLAN Adapter"
#     wifi (rtl8192cu), 88:D7:F6:01:D9:0A, hw, mtu 1500
#     ip4 default, ip6 default
#     inet4 192.168.59.57/24    <-- here is IP address we need
#     route4 0.0.0.0/0
#     route4 192.168.59.0/24
#     route4 169.254.0.0/16
#     inet6 2a00:1fa0:c6c6:cdaa:55fe:6484:8ce2:477c/64
#     inet6 2a00:1fa0:c6c6:cdaa:b13b:7feb:c80:9db9/64
#     inet6 fe80::220b:bc71:8e7b:c10a/64
#     route6 2a00:1fa0:c6c6:cdaa::/64
#     route6 ::/0
#     route6 ff00::/8
#     route6 fe80::/64
#     route6 fe80::/64
# l4tbr0: connected to l4tbr0
#     "l4tbr0"
#     bridge, E6:6C:F5:B4:45:CD, sw, mtu 1500
#     inet4 192.168.55.1/24
#     route4 192.168.55.0/24
#     route4 0.0.0.0/0
#     inet6 fe80::1/128
#     inet6 fe80::e46c:f5ff:feb4:45cd/64
#     route6 ff00::/8
#     route6 fe80::/64
#
# From this message we want to take 192.168.59.57
```

Then you can connect to Jetson.

```bash
ssh vidianiv@192.168.59.57
```

## Docker Setup

NVIDIA Container Runtime on Jetson should be installed
already, so we can move on directly to usage.

Following [manual](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/l4t-jetpack)
manual download and run NVIDIA L4T JetPack docker image.

```bash
sudo docker pull nvcr.io/nvidia/l4t-jetpack:r35.3.1

sudo docker run -it --rm \
    --net=host \
    --runtime nvidia \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix/:/tmp/.X11-unix \
    nvcr.io/nvidia/l4t-jetpack:r35.3.1
```

## Reference

- [Official guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)
- [Guide from @zeanfa](https://github.com/zeanfa/mobileCV_public)
- [Docker NVIDIA L4T JetPack image](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/l4t-jetpack)
