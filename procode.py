import re
import requests

class ProCodeInterpreter:
    def __init__(self):
        self.variables = {}
        self.session = requests.Session()  # Create an HTTP session for API requests

    def interpret(self, code):
        lines = code.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith("class"):
                self.handle_class_declaration(line)
            elif line.startswith("prop"):
                self.handle_property_declaration(line)
            elif "=" in line:
                self.handle_assignment(line)
            elif line.startswith("print"):
                self.handle_print(line)
            elif line.startswith("request"):
                self.handle_request(line)

    def handle_class_declaration(self, line):
        class_name = re.search(r'class (\w+)', line).group(1)
        self.variables[class_name] = {}

    def handle_property_declaration(self, line):
        prop_type, prop_name = re.search(r'prop (\w+) (\w+)', line).groups()
        class_name = line.split('.')[0]
        self.variables[class_name][prop_name] = None

    def handle_assignment(self, line):
        var_name, value = line.split('=')
        var_name = var_name.strip()
        value = value.strip()
        class_name, prop_name = var_name.split('.')
        self.variables[class_name][prop_name] = value

    def handle_print(self, line):
        var_name = line.split('(')[-1].split(')')[0].strip()
        class_name, prop_name = var_name.split('.')
        value = self.variables[class_name][prop_name]
        print(value)

    def handle_request(self, line):
        url = line.split('(')[-1].split(')')[0].strip()
        response = self.session.get(url)
        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Request failed with status code {response.status_code}")
