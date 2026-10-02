#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""  
NIM: 2409106057 | Nama: Dimas Firjatullah Islamay 
""" 

from pysnmp.hlapi.v3arch.asyncio import * 
  
nim = "2409106057" 
host_vm = "127.0.0.1" 
port_snmp_vm = 1161 
community = "comm_057" 
  
async def cek_snmp(): 
    try: 
        errorIndication, errorStatus, errorIndex, varBinds = await get_cmd( 
            SnmpEngine(), 
            CommunityData(community), 
            await UdpTransportTarget.create((host_vm, port_snmp_vm)), 
            ContextData(), 
            ObjectType(ObjectIdentity("1.3.6.1.2.1.1.5.0")) 
        )
        if errorIndication: 
            print("[SNMP] GAGAL: " + str(errorIndication)) 
        elif errorStatus: 
            print("[SNMP] GAGAL: " + errorStatus.prettyPrint()) 
        else: 
            for vb in varBinds: 
                print("[SNMP] sysName VM: " + str(vb[1])) 
    except Exception as e: 
        print("[SNMP] GAGAL: " + str(e)) 
