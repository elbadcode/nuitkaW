from sys import argv
from os import system

if len(argv) == 1:
    system("@echo usage: python file must be first argument or open with windows explorer")

if argv[1].endswith(('.py','.pyw')):
    command = f'nuitka --standalone --onefile --main="{argv[1]}"'
    if len(argv) > 2:
        command += argv[2:]
    system(command)
