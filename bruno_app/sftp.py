
"""SFTP with Richie's Instance"""

import pysftp

with pysftp.Connection('hostname', username='me', password='secret') as sftp:
    with sftp.cd('D:\RaspberryPi_Bruno_Api\bruno_app'):           # temporarily chdir to allcode
        sftp.put('/home/pi/Downloads/bruno_app/.env')  	# upload file to allcode/pycode on remote
        #sftp.get('remote_file')         # get a remote file
