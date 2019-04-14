# Tools and Scripts for Raspberry Pi

rpi-tools is a cross-platform open-source ready-to-use tools and scripts to setup Raspberry Pis.
rpi-tools allows developers to develop their own ideas without the hassle of setting up their Raspberry Pis so that they can focus on what matters.

We are looking for contributors!

## Current Tools and Scripts
Below are our ready-to-use scripts you can use to setup your Raspberry Pi:

|  Script  | Description |
|:---|----------------:|
| **burn_sd_with_ssh_over_wifi.py** | Burn an image on an SD card without any external software, setup ssh and wifi. Very handy when it comes to setup a headless Raspberry Pi |
| **setup_wifi_repeater.py** | Automatically configure a raspberry pi to be a Wifi repeater (requires 2 wifi cards though) |
| **build_rtl8812au.py** | Automatically build and install the rtl8812au wifi driver on your Raspberry Pi |
| **install_dotnet_core.py** | Automatically install .NET Core on your Raspberry Pi |

## Examples
```
sam@system:~/Projects/rpi-tools$ sudo python3 burn_sd_with_ssh_over_wifi.py

Please type the raspian image to burn: (ex: /home/sam/Downloads/2018-11-13-raspbian-stretch-full.img) /home/sam/Downloads/2018-11-13-raspbian-stretch-full.img
> "fdisk -l | grep "Disk /""
Available disks:
0: Disk /dev/loop0: 295.9 MiB, 310247424 bytes, 605952 sectors
1: Disk /dev/loop1: 294.2 MiB, 308449280 bytes, 602440 sectors
2: Disk /dev/loop2: 91 MiB, 95416320 bytes, 186360 sectors
3: Disk /dev/loop3: 91.1 MiB, 95522816 bytes, 186568 sectors
4: Disk /dev/loop4: 89.3 MiB, 93581312 bytes, 182776 sectors
5: Disk /dev/loop5: 271.7 MiB, 284835840 bytes, 556320 sectors
6: Disk /dev/sda: 119.2 GiB, 128035676160 bytes, 250069680 sectors
7: Disk /dev/sdb: 7.4 GiB, 7948206080 bytes, 15523840 sectors
Please select the raspberry pi SD card: (ex: 2) 7

Confirm target disk is: Disk /dev/sdb: 7.4 GiB, 7948206080 bytes, 15523840 sectors? (ex: y) y

> "dd if=/home/sam/Downloads/2018-11-13-raspbian-stretch-full.img of=/dev/sdb status=progress bs=4M"
5293211648 bytes (5.3 GB, 4.9 GiB) copied, 568 s, 9.3 MB/s
1263+0 records in
1263+0 records out
5297405952 bytes (5.3 GB, 4.9 GiB) copied, 568.684 s, 9.3 MB/s

Please remove and re-insert the SD card...
Please type the raspberry boot path: (ex: /media/sam/boot) /media/sam/boot

Enabling ssh...
> "touch /media/sam/boot/ssh"
Enabling ssh...Done.

Please type the raspberry rootfs path: (ex: /media/sam/rootfs) /media/sam/rootfs
Please enter the wifi country: (ex: FR) FR
Please enter the wifi ssid: (ex: BBox-26354) RaspAP
Please enter the wifi password: (ex: acemyraspberrypi) secret_password

Setting up wifi...
> "cat > /media/sam/rootfs/etc/wpa_supplicant/wpa_supplicant.conf <<EOF
country=FR
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="RaspAP"
    psk="secret_password"
}
EOF"
Setting up wifi...Done.
