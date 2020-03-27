import paramiko
import gzip
<<<<<<< HEAD
user_name = 'Richie'
host='LAPTOP-25QB2DD1@192.168.43.186'
=======
user_name = 'pi'
host='192.168.43.82'
with open(r'C:\Users\Richie\.ssh\passwd.txt', 'r') as file:    
    passwd = file.readlines()
>>>>>>> 0ed84b17b92e6a81cca68cc26f33a0e475a0c6d9
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = host,
                   port = 22,
                   username = user_name,
<<<<<<< HEAD
                   key_filename='/home/pi/Downloads/bruno_app/.ssh/id_rsa')
=======
                   password = passwd[0])
>>>>>>> 0ed84b17b92e6a81cca68cc26f33a0e475a0c6d9

a,b,c = ssh_client.exec_command('hostname')
print(b.readlines())
sftp=ssh_client.open_sftp()

<<<<<<< HEAD
remotepath = 'D:\RaspberryPi_Bruno_Api\bruno_app'
localpath = '/home/pi/Downloads/bruno_app/readme.txt'
sftp.get(remotepath,localpath)

ssh_client.connect(hostname = host,
                   port = 22,
                   username = user_name)
=======
remotepath = '/home/pi/Downloads/bruno_app/.env'
localpath = 'D:\\RaspberryPi_Bruno_Api\\bruno_app\\.env'
sftp.get(remotepath,localpath)
>>>>>>> 0ed84b17b92e6a81cca68cc26f33a0e475a0c6d9
