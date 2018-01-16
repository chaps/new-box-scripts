import os
import sys
import logging
import subprocess

def get_os():
    osPlatform = sys.platform
    return(osPlatform)

if __name__ == '__main__':
    my_os = get_os()
    print my_os