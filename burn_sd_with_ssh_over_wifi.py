import os
from rpi_tools import DebianCommand

# chosing the SD drive
image_filepath = input('Please type the raspian image to burn: (ex: /home/sam/Downloads/2018-11-13-raspbian-stretch-full.img) ')
disks = DebianCommand.list_disks()
print('Available disks:')
for i, disk in enumerate(disks):
    print(f'{i}: {disk}')
disk_index = int(input('Please select the raspberry pi SD card: (ex: 2) '))
dest_disk = disks[disk_index]

# burning the raspian image onto the selected SD drive
confirmation = input(f'Confirm target disk is: {dest_disk}? (ex: y) ')
if confirmation == 'y':
    DebianCommand.burn_sd(image_filepath, dest_disk)
print('Please remove and re-insert the SD card...')

# enabling ssh
boot_path = input('Please type the raspberry boot path: (ex: /media/sam/boot) ' )
print('Enabling ssh...')
DebianCommand.enable_ssh_on_rpi_sd(boot_path)
print('Enabling ssh...Done.')

# enabling wifi connection
rootfs_path = input('Please type the raspberry rootfs path: (ex: /media/sam/rootfs) ' )
wifi_country = input('Please enter the wifi country: (ex: FR) ')
wifi_ssid = input('Please enter the wifi ssid: (ex: BBox-26354) ')
wifi_password = input('Please enter the wifi password: (ex: acemyraspberrypi) ')
print('Setting up wifi...')
DebianCommand.setup_wifi(rootfs_path, wifi_country, wifi_ssid, wifi_password, 'wpa_supplicant')
print('Setting up wifi...Done.')

# setting up ping task
print('We can start an HTTP server so that the raspberry pi can ping its IP address so that')
print('you can SSH into it. Otherwise you can skip this step and scan your wifi network by your own.')
confirmation = input('Do you want to set up the ping server? (ex: y) ')
if confirmation == 'y':
    print('Please start the script: start_ping_server in another terminal and let it run.')
    server_ip_address = input('Please enter the current IP address printed by the script: ')
    print('Setting up ping task...')
    DebianCommand.setup_ping_task(rootfs_path, server_ip_address, 8000)
    print('Setting up ping task... Done.')
print('Done.')
print('You can now insert your SD card into your raspberry pi and monitor the ping server script')
print('to get the raspberry IP.')