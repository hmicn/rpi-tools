import os, re
from rpi_tools import RpiPythonApi

current_platform = 'ubuntu'
api = RpiPythonApi()

# chosing the SD drive
image_filepath = input('Please type the raspian image to burn: (ex: /home/sam/Downloads/2018-11-13-raspbian-stretch-full.img) ')
disks = api.exec(current_platform, 'list_disks')
print('Available disks:')
for i, disk in enumerate(disks):
    print(f'{i}: {disk}')
disk_index = int(input('Please select the raspberry pi SD card: (ex: 2) '))
dest_disk = disks[disk_index]

# burning the raspian image onto the selected SD drive
confirmation = input(f'Confirm target disk is: {dest_disk}? (ex: y) ')
if confirmation == 'y':
    m = re.search('(/dev/[a-z]+)', dest_disk)
    if m:
        dest_disk = m.group(1)
        api.exec(current_platform, 'burn_sd', {
            'IMG_FILEPATH' : image_filepath,
            'DEST_DISK' : dest_disk
        })
print('Please remove and re-insert the SD card...')

# enabling ssh
boot_path = input('Please type the raspberry boot path: (ex: /media/sam/boot) ' )
print('Enabling ssh...')
api.exec(current_platform, 'enable_ssh_on_rpi_sd', {
    'SSH_FILE' : os.path.join(boot_path, 'ssh')
})
print('Enabling ssh...Done.')

# enabling wifi connection
rootfs_path = input('Please type the raspberry rootfs path: (ex: /media/sam/rootfs) ' )
wifi_country = input('Please enter the wifi country: (ex: FR) ')
wifi_ssid = input('Please enter the wifi ssid: (ex: BBox-26354) ')
wifi_password = input('Please enter the wifi password: (ex: acemyraspberrypi) ')
print('Setting up wifi...')
api.exec(current_platform, 'setup_wifi', {
    'CONF_FILE' : os.path.join(rootfs_path, f'etc/wpa_supplicant/wpa_supplicant.conf'),
    'WIFI_COUNTRY' : wifi_country,
    'WIFI_SSID' : wifi_ssid,
    'WIFI_PASSWORD' : wifi_password
})
print('Setting up wifi...Done.')