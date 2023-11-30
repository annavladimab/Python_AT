from robot.libraries.BuiltIn import BuiltIn

class MyListener:

    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        self.builtin = BuiltIn()

    def start_test(self, name, attrs):
        self.builtin.log(f"Starting test: {name}", console=True)

    def end_test(self, name, attrs):
        self.builtin.log(f"Ending test: {name}", console=True)

    def start_suite(self, name, attrs):
        self.builtin.log(f"Starting suite: {name}", console=True)

    def end_suite(self, name, attrs):
        self.builtin.log(f"Ending suite: {name}", console=True)

    def start_keyword(self, name, attrs):
        self.builtin.log(f"Starting keyword: {name}", console=True)

    def end_keyword(self, name, attrs):
        self.builtin.log(f"Ending keyword: {name}", console=True)
