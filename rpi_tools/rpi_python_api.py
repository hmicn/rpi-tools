import os

class RpiPythonApi:
    def __init__(self):
        self.__extensions = {
            'raspian' : '.sh',
            'ubuntu' : '.sh'
        }

    def exec(self, platform, function, variables = {}):
        if platform not in self.__extensions:
            raise Exception(f'Platform: {platform} unknown.')
        script_filepath = os.path.join('rpi_tools', platform, f'{function}{self.__extensions[platform]}')
        if not os.path.isfile(script_filepath):
            raise Exception(f'Script file: {script_filepath} cannot be found.')
        with open(script_filepath, 'r') as fp:
            content = fp.read()
        for key in variables:
            content = content.replace('{{' + key + '}}', variables[key])
        print(f'> "{content}"')
        return os.popen(content).read().strip().split("\n")