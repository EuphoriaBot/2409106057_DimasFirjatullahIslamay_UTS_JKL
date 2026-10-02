#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File   : telemetry_modul.py
Tujuan      : Menyimpan data SAMPEL telemetry (menyerupai hasil decode GPB
              yang diterima collector) dan mengklasifikasikan nilai cpuUsage
              (in-uti) menjadi KRITIS / WASPADA / NORMAL.
Pembuat     : Dimas Firjatullah Islamay - 2409106057
"""

from identitas import kode_cabang  

digit_nim = [int(d) for d in kode_cabang]


def _hitung_cpu(digit):
    """Menurunkan nilai cpuUsage (%) dari satu digit NIM."""
    return digit * 12 + 10

data_telemetry = {
    f"sampel_{i + 1}": {
        "sensor_path": "huawei-devm:devm/cpuInfos/cpuInfo",
        "position": f"{i}",
        "cpuUsage": _hitung_cpu(d),
    }
    for i, d in enumerate(digit_nim)
}


def klasifikasi_telemetry():
    hasil = []
    print("=== Klasifikasi Telemetry (cpuUsage) ===")

    for nama, sampel in data_telemetry.items():
        cpu = sampel["cpuUsage"]

        if cpu > 80:
            status = "KRITIS"
        elif cpu >= 50:
            status = "WASPADA"
        else:
            status = "NORMAL"

        print(f"{nama}: cpuUsage = {cpu}% -> {status}")
        hasil.append((nama, cpu, status))

    return hasil

if __name__ == "__main__":
    klasifikasi_telemetry()