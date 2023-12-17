import os
from procode import ProCodeInterpreter as PCI

directory = 'Directory Here'

for filename in os.listdir(directory):
    if filename.endswith('.pc'):

        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            procode_code = file.read()

        interpreter = PCI()
        interpreter.interpret(procode_code)