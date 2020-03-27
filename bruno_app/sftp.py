
"""SFTP with Richie's Instance"""

import paramiko
import gzip
user_name = 'Richie'
host='192.168.43.186'
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = host,
                   port = 22,
                   username = user_name,
                   key_filename='/home/pi/Downloads/bruno_app/.ssh/id_rsa.pub')

a,b,c = ssh_client.exec_command('hostname')
print(b.readlines())
sftp=ssh_client.open_sftp()

remotepath = 'D:\RaspberryPi_Bruno_Api\bruno_app'
localpath = '/home/pi/Downloads/bruno_app/readme.txt'
sftp.get(remotepath,localpath)

