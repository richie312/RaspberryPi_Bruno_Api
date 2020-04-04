import paramiko
import gzip
import getpass
user_name = 'pi'
host='192.168.43.82'
root = r'C:\Users\'
sys_user = getpass.getuser()
file_path = r'\.ssh\passwd.txt'
target_path = root + sys_user + file_path
with open(target_path', 'r') as file:
	passwd = file.readlines()
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = host,
	port = 22,
	username = user_name,
	password = passwd[0])
sftp=ssh_client.open_sftp()

remotepath = '/home/pi/Downloads/bruno_app/.env'
localpath = 'D:\\RaspberryPi_Bruno_Api\\bruno_app\\.env'
sftp.get(remotepath,localpath)
