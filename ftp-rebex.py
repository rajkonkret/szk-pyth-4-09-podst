import ftplib

ftp = ftplib.FTP('test.rebex.net')
logowanie = ftp.login('demo', 'password')
print(logowanie)  # 230 User 'demo' logged in.
# katalog = ftp.nlst()
katalog = ftp.nlst('pub/example')
print(katalog)  # ['pub', 'readme.txt']
# plik = ftp.retrbinary('RETR readme.txt', open('README.log', 'wb').write)
plik = ftp.retrbinary('RETR pub/example/KeyGenerator.png', open('plik.png', 'wb').write)
plik = ftp.retrbinary('RETR pub/example/WinFormClient.png', open('plik2.png', 'wb').write)
# paramiko

