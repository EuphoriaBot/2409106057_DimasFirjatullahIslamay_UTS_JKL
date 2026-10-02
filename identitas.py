#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama file : identitas.py
Tujuan    : Module pendukung untuk membuat ID unik perangkat jaringan
            berdasarkan jenis perangkat, kode cabang, dan nomor perangkat.
Pembuat   : Dimas Firjatullah Islamay
"""

def buat_id_perangkat(jenis, nomor):
    """
    Membuat ID unik perangkat jaringan.

    Parameter:
        jenis  (str): kode jenis perangkat, contoh "RTR", "SWT", "FWL".
        nomor  (str): nomor urut perangkat, contoh "01".

    Return:
        str: ID perangkat dalam format JENIS-KODECABANG-NOMOR.
    """

    kode_cabang = getattr(buat_id_perangkat, "kode_cabang", "000")

    return f"{jenis}-{kode_cabang}-{nomor}"