import os, re

class DebianCommand:
    @staticmethod
    def enable_ssh_on_rpi_sd(boot_path):
        os.system(f'touch {os.path.join(boot_path, "ssh")}')

    @staticmethod
    def setup_wifi(rootfs_path, country, ssid, password, conf_file = 'wpa_supplicant'):
        conf_file = os.path.join(rootfs_path, f'etc/wpa_supplicant/{conf_file}.conf')
        os.system('''cat > ''' + conf_file + ''' <<EOF
country=''' + country + '''
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="''' + ssid + '''"
    psk="''' + password + '''"
}
EOF''')

    @staticmethod
    def burn_sd(image_filepath, dest_disk):
        m = re.search('(/dev/[a-z]+)', dest_disk)
        if not m:
            return
        dest_disk = m.group(1)
        print(f'dd if={image_filepath} of={dest_disk} status=progress bs=4M')
        os.system(f'dd if={image_filepath} of={dest_disk} status=progress bs=4M')

    @staticmethod
    def list_disks():
        return os.popen(f'fdisk -l | grep "Disk /"').read().strip().split("\n")

    @staticmethod
    def setup_ping_task(rootfs_path, server_ip_address, server_port):
        home_path = os.path.join(rootfs_path, 'home', 'pi')
        ping_bash = os.path.join(home_path, 'ping_server.sh')
        os.system(f'''cat > {ping_bash} <<EOF
wget http://{server_ip_address}:{server_port}
EOF''')
        os.system(f'chmod 777 {ping_bash}')
        bash_rc_path = os.path.join(home_path, '.bashrc')
        os.system(f'''cat >> {bash_rc_path} <<EOF
./ping_server.sh
EOF''')