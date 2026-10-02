#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""  
NIM: 2409106057 | Nama: Dimas Firjatullah Islamay 
""" 

import paramiko 
from pysnmp.hlapi.v3arch.asyncio import * 
  
nim = "2409106057" 
host_vm = "127.0.0.1" 
port_ssh_vm = 2222  
user_ssh = "dimasubuntu" 
pass_ssh = "dimasubuntu" 

  
def cek_ssh(): 
    try: 
        client = paramiko.SSHClient() 
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        client.connect(host_vm, port=port_ssh_vm, username=user_ssh, password=pass_ssh, timeout=5) 
        stdin, stdout, stderr = client.exec_command("hostname") 
        hasil_hostname = stdout.read().decode().strip() 
        stdin, stdout, stderr = client.exec_command("whoami") 
        hasil_whoami = stdout.read().decode().strip() 
        print("[SSH] hostname VM: " + hasil_hostname) 
        print("[SSH] whoami di VM: " + hasil_whoami) 
        client.close() 
    except Exception as e: 
        print("[SSH] GAGAL: " + str(e)) 
  
