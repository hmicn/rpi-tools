git clone https://github.com/aircrack-ng/rtl8812au -b v5.2.20
cd rtl8812au
sed -i 's/CONFIG_PLATFORM_I386_PC = y/CONFIG_PLATFORM_I386_PC = n/g' Makefile
sed -i 's/CONFIG_PLATFORM_ARM64_RPI = y/CONFIG_PLATFORM_ARM64_RPI = {{IS_64}}/g' Makefile
sed -i 's/CONFIG_PLATFORM_ARM_RPI = y/CONFIG_PLATFORM_ARM_RPI = {{NOT_IS_64}}/g' Makefile
make
cp 8812au.ko /lib/modules/`uname -r`/kernel/drivers/net/wireless
depmod -a
modprobe 88XXau