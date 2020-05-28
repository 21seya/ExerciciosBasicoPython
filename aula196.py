import os 
from getpass import getpass
from ftplib import FTP

nonpassive = False

nome_arquivo = 'README'

dir_nome = 'debian'

site_nome = 'ftp.debin.org'

usuario_info = []

print('Conectando.....')

coenxao = FTP(site_nome)

conexao.login(*usuario_info)
