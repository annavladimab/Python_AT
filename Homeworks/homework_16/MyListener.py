from robot.libraries.BuiltIn import BuiltIn


class MyListener:
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        self.builtin = BuiltIn()

    def end_keyword(self, name, attrs):
        tags = attrs['Tags']
        if 'Screenshot' in tags:
            print(f'Screenshot : {name}')


if __name__ == '__main__':
    BuiltIn().import_library(MyListener())
