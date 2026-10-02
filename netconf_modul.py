#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File   : netconf_modul.py
Tujuan      : Membangun (generate) pesan NETCONF <rpc><edit-config> berbentuk
              XML untuk membuat VLAN dengan ID = kode_cabang
              Program tidak terhubung ke perangkat NETCONF sungguhan
Pembuat     : Dimas Firjatullah Islamay - 2409106057
"""

import xml.etree.ElementTree as ET

from identitas import kode_cabang  

VLAN_ID = int(kode_cabang)


def buat_pesan_netconf():
    """Membangun string XML <rpc><edit-config> untuk membuat VLAN."""

    rpc = ET.Element("rpc", {
        "xmlns": "urn:ietf:params:xml:ns:netconf:base:1.0",
        "message-id": "101",
    })

    edit_config = ET.SubElement(rpc, "edit-config")
    target = ET.SubElement(edit_config, "target")
    ET.SubElement(target, "running")

    config = ET.SubElement(edit_config, "config")
    vlan = ET.SubElement(config, "vlan", {
        "xmlns": "http://www.huawei.com/netconf/vrp/huawei-vlan"
    })
    vlans = ET.SubElement(vlan, "vlans")
    vlan_item = ET.SubElement(vlans, "vlan")
    ET.SubElement(vlan_item, "id").text = str(VLAN_ID)
    ET.SubElement(vlan_item, "name").text = f"VLAN_CABANG_{kode_cabang}"

    ET.indent(rpc, space="  ") 
    return ET.tostring(rpc, encoding="unicode")


if __name__ == "__main__":
    pesan = buat_pesan_netconf()
    print("=== Pesan NETCONF <rpc><edit-config> ===")
    print(pesan)