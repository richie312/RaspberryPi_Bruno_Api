import paramiko
import gzip
user_name = 'pi'
host='192.168.43.82'
with open(r'C:\Users\Richie\.ssh\passwd.txt', 'r') as file:    
    passwd = file.readlines()
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = host,
                   port = 22,
                   username = user_name,
                   password = passwd[0])

a,b,c = ssh_client.exec_command('hostname')
print(b.readlines())
sftp=ssh_client.open_sftp()

remotepath = '/home/pi/Downloads/bruno_app/.env'
localpath = 'D:\\RaspberryPi_Bruno_Api\\bruno_app\\.env'
sftp.get(remotepath,localpath)