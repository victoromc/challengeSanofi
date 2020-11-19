import os
import ftplib
import zipfile

site = "ftp.datasus.gov.br"
diretorio = "/dissemin/publicos/"
# CIH/200801_201012/Dados/
ftp = ftplib.FTP(site)
ftp.login("anonymous", "anonymous@")
info = sorted([
    'SIHSUS - Arquivos dissemináveis para tabulação do Sistema de Informações Hospitalares do SUS',
    'SIASUS - Arquivos dissemináveis para tabulação do Sistema de Informações Ambulatoriais do SUS',
    'SIM - Arquivos dissemináveis para tabulação do Sistema de informações de Mortalidade',
    'CIH - Arquivos dissemináveis para tabulação do Sistema de Comunicação de Informação Hospitalar',
    'CIHA - Arquivos dissemináveis para tabulação do Sistema de Comunicação de Informação Hospitalar e Ambulatorial',
    'SINASC - Arquivos dissemináveis para tabulação do Sistema de informação de Nascidos Vivos',
    'SISPRENATAL - Arquivos dissemináveis para tabulação do Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puerpério e Criança',
    'SISAB - Arquivos dissemináveis para tabulação do Sistema de Informação em Saúde para a Atenção Básica.',
    'SINAN - Arquivos dissemináveis para tabulação do Sistema de agravos de notificação compulsória.'
])
for i in info:
    print(str(info.index(i)) + ') ' + str(i))

pasta = int(input('\nDigite o número da pasta que quer acessar: \n'))
if pasta == 8:
    folder = diretorio + '/CMD'
else:
    folder = diretorio + '/' + info[pasta].split(' -')[0]
ftp.cwd(folder)

print("\n---------------------------\n")
print("Dentro do diretório: \n")
sgndDir = []
sgndDir = ftp.nlst()
for d in sgndDir:
    print(str(sgndDir.index(d)) + ') ' + str(d))
pasta = int(input('\nDigite o número da pasta que quer acessar: \n'))
folder = ftp.pwd() + '/' + sgndDir[pasta]
ftp.cwd(folder)

print("\n---------------------------\n")
print("Dentro do diretório: \n")
sgndDir = ftp.nlst()
for d in sgndDir:
    print(str(sgndDir.index(d)) + ') ' + str(d))
pasta = int(input('\nDigite o número da pasta que quer acessar: \n'))
folder = ftp.pwd() + '/' + sgndDir[pasta]
ftp.cwd(folder)

print("\n---------------------------\n")
print("Dentro do diretório: \n")
arquivos = []
arquivos = ftp.nlst()
for arquivo in arquivos:
    print(arquivo)

# savedir = "/home/oliver/Desktop/dbc2csv/Source" # linux

fn = input("\nDigite o nome do arquivo que deseja baixar:")
savedir = input("\nDigite o diretório que o arquivo será salvo:\n")
os.chdir(savedir)
file = open(fn, "wb")
ftp.retrbinary('RETR ' + fn, file.write)
print('\nDownload concluido')

ftp.quit()
