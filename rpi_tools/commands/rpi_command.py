import os

class RpiCommand:
    @staticmethod
    def prepare_rpi_source():
        'apt-get install build-essential raspberrypi-kernel-headers bc'
        'wget "https://raw.githubusercontent.com/notro/rpi-source/master/rpi-source" -O /usr/bin/rpi-source'
        'chmod 755 /usr/bin/rpi-source'
        'rpi-source'

    @staticmethod
    def install_rtl8812au(is_64):
        'git clone https://github.com/aircrack-ng/rtl8812au -b v5.2.20'
        'cd rtl*'
        platforms = {
            'I386_PC' : False,
            'ARM64_RPI' : is_64,
            'ARM_RPI' : not is_64
        }
        for platform in platforms:
            f"sed -i 's/CONFIG_PLATFORM_{platform} = y/CONFIG_PLATFORM_{platform} = {'y' if platforms[platform] else 'n'}/g' Makefile"
        'make'
        'cp 8812au.ko /lib/modules/`uname -r`/kernel/drivers/net/wireless'
        'depmod -a'
        'modprobe 88XXau'