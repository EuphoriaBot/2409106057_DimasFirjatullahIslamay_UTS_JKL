#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama file : identitas.py
Tujuan    : Module pendukung untuk membuat ID unik perangkat jaringan
            berdasarkan jenis perangkat, kode cabang, dan nomor perangkat.
Pembuat   : Dimas Firjatullah Islamay
"""

nim = "2409106057"
nama = "Dimas Firjatullah Islamay"
kode_cabang = nim[-3:]

def buat_id_perangkat(jenis, nomor):

    kode_cabang = getattr(buat_id_perangkat, "kode_cabang", "000")

    return f"{jenis}-{kode_cabang}-{nomor}"