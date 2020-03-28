import paramiko
import gzip
user_name = 'Richie'
host='LAPTOP-25QB2DD1@192.168.43.186'
user_name = 'pi'
host='192.168.43.82'
with open(r'C:\Users\Richie\.ssh\passwd.txt', 'r') as file:    
    passwd = file.readlines()
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = host,
                   port = 22,
                   username = user_name,
                   key_filename='/home/pi/Downloads/bruno_app/.ssh/id_rsa')
                   password = passwd[0])

remotepath = '/home/pi/Downloads/bruno_app/.env'
localpath = 'D:\\RaspberryPi_Bruno_Api\\bruno_app\\.env'
sftp.get(remotepath,localpath)
