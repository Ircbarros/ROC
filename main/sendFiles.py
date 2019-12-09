# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

__author__ = "Ítalo Barros"
__copyright__ = "Copyright 2019, LASER - UFPB"
__license__ = "X11"
__version__ = "alpha 0.1"
__maintainer__ = "Ítalo Barros"
__email__ = "italorenan_@hotmail.com"
__status__ = "In Development"


import os
import paramiko
from os import environ
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et


# Save Logs
paramiko.util.log_to_file('/tmp/paramiko.log')
paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

# Reads the Experiment Configuration XML File
configurationFile = et.parse('experimentConfig.xml')
# Find the root element from the file (in this case "environment")
root = configurationFile.getroot()
# Save the Robot Selected
robot_selection = root.findtext('ROBOT_SELECTED')

if robot_selection=='TB1':
    # Reads the TB1 Settings XML File
    sshParameters = et.parse('tb1Settings.xml')
    # Find the root element from the file (in this case "environment")
    tb1_root = sshParameters.getroot()
    # SSH Variables from TB1
    ssh_IP = tb1_root.findtext('SSH_TB1_IP')
    ssh_USER = tb1_root.findtext('SSH_TB1_USERNAME')
    ssh_PASSWORD = tb1_root.findtext('SSH_TB1_PASSWORD')
    ssh_PORT = tb1_root.findtext('SSH_TB1_PORT')
elif robot_selection=='TB2':
    # Reads the TB2 Settings XML File
    sshParameters = et.parse('tb2Settings.xml')
    # Find the root element from the file (in this case "environment")
    tb2_root = sshParameters.getroot()
    # SSH Variables from TB2
    ssh_IP = tb2_root.findtext('SSH_TB2_IP')
    ssh_USER = tb2_root.findtext('SSH_TB2_USERNAME')
    ssh_PASSWORD = tb2_root.findtext('SSH_TB2_PASSWORD')
    ssh_PORT = tb2_root.findtext('SSH_TB2_PORT')
elif robot_selection=='TB3':
    # Reads the TB3 Settings XML File
    sshParameters = et.parse('tb2Settings.xml')
    # Find the root element from the file (in this case "environment")
    tb3_root = sshParameters.getroot()
    # SSH Variables from TB3
    ssh_IP = tb3_root.findtext('SSH_TB3_IP')
    ssh_USER = tb3_root.findtext('SSH_TB3_USERNAME')
    ssh_PASSWORD = tb3_root.findtext('SSH_TB3_PASSWORD')
    ssh_PORT = tb3_root.findtext('SSH_TB3_PORT')
elif robot_selection=='TB4':
    # Reads the TB3 Settings XML File
    sshParameters = et.parse('tb4Settings.xml')
    # Find the root element from the file (in this case "environment")
    tb4_root = sshParameters.getroot()
    # SSH Variables from TB3
    ssh_IP = tb4_root.findtext('SSH_TB4_IP')
    ssh_USER = tb4_root.findtext('SSH_TB4_USERNAME')
    ssh_PASSWORD = tb4_root.findtext('SSH_TB4_PASSWORD')
    ssh_PORT = tb4_root.findtext('SSH_TB4_PORT')


def sshSendFiles():
    print(ssh_IP)
    print(ssh_USER)
    print(ssh_PASSWORD)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ssh_IP, username=ssh_USER, password=ssh_PASSWORD)
    ftp_client = ssh_client.open_sftp()
    ftp_client.put('~/Desktop/RoC/main/experimentConfig.xml', '~/var/temp')
    ftp_client.close()

if __name__ == "__main__":
    sshSendFiles()