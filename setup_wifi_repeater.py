from rpi_tools import RpiPythonApi

api = RpiPythonApi()
print(api.exec('ubuntu', 'list_disks'))