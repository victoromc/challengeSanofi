import os
import ftplib
import zipfile

site = "ftp.datasus.gov.br"
diretorio = "/dissemin/publicos/CIH/200801_201012/Dados/"

ftp = ftplib.FTP(site)
ftp.login("anonymous", "anonymous@")

ftp.cwd(diretorio)
print(ftp.retrlines('LIST'))

savedir = "/home/oliver/Desktop/dbc2csv/Source"
os.chdir(savedir)

fn = "CRSP1001.dbc"
print(fn)
file = open(fn, "wb")
ftp.retrbinary('RETR ' + fn, file.write)
ftp.quit()

print(fn)
#input("\nDigite o número da pasta que deseja acessar: \n")
