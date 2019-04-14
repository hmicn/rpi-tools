cat > {{CONF_FILE}} <<EOF
country={{WIFI_COUNTRY}}
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="{{WIFI_SSID}}"
    psk="{{WIFI_PASSWORD}}"
}
EOF