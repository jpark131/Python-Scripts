"""Execute a command on multiple hosts"""

import os
import sys
import shlex
import subprocess as sp
from packages.ping import ping
sys.path.append('C:/Users/jakep/Documents/code/packages')

def open_subprocess(command):
    """Use subprocess.Popen to open a subprocess and return the child process object"""
    child = sp.Popen(shlex.split(command),
                     universal_newlines=True,
                     stdout=sp.PIPE, stderr=sp.STDOUT)
    return child

def ssh_execute(host, command):
    """Execute a command over ssh and print the output"""
    if not ping(host):
        print(f"{host} not reachable, skipping")
        return
    child = open_subprocess(f"ssh {host} {command}")
    output = child.communicate()
    print(output[0])

def main():
    pass

if __name__ == "__main__":
    main()
