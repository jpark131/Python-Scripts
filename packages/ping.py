"""Quick package for pinging a network device"""
import os
import shlex
import subprocess as sp

def ping(hostname, num_pings=4):
    """
    Purpose: ping a network host. Works on windows and posix systems
    Parameters:
        -hostname: hostname or ip of network host to be pinged
        -num_pings: number of times to attempt ping
    Return: True if success, False otherwise
    """
    if os.name == "nt":
        pingstring = f"ping -n {num_pings} {hostname}"
    elif os.name == "posix":
        pingstring = f"ping -c {num_pings} {hostname}"
    else:
        print(f"OS {os.name} not handled")
        return False
    child = sp.Popen(shlex.split(pingstring), 
                     universal_newlines=True, 
                     stdout=sp.PIPE, stderr=sp.PIPE)
    child_stdout = child.communicate()[0]
    return "bytes" in child_stdout
