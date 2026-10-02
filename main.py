#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File   : main.py
Tujuan      : Mengintegrasikan modul identitas, ssh_modul, snmp_modul,
              netconf_modul, dan telemetry_modul, menjalankan seluruh
              function secara berurutan, lalu mencetak SATU laporan akhir.
Pembuat     : Dimas Firjatullah Islamay - 2409106057
"""

import identitas
import ssh_modul
import snmp_modul
import netconf_modul
import telemetry_modul


class LaporanCabang:
    """Menyimpan hasil semua modul dan mencetaknya sebagai satu laporan"""

    def __init__(self, id_perangkat, hasil_ssh, hasil_snmp,
                 pesan_netconf, hasil_telemetry):
        self.id_perangkat = id_perangkat
        self.hasil_ssh = hasil_ssh
        self.hasil_snmp = hasil_snmp
        self.pesan_netconf = pesan_netconf
        self.hasil_telemetry = hasil_telemetry

    def tampilkan_laporan(self):
        garis = "=" * 60
        print(f"\n{garis}")
        print("LAPORAN AKHIR CABANG VIRTUAL")
        print(garis)
        print(f"Nama          : {identitas.nama}")
        print(f"NIM           : {identitas.nim}")
        print(f"ID Perangkat  : {self.id_perangkat}")

        print("\n[1] Hasil SSH (Paramiko)")
        print(self.hasil_ssh)

        print("\n[2] Hasil SNMP (sysName)")
        print(self.hasil_snmp)

        print("\n[3] Pesan NETCONF yang dibuat")
        print(self.pesan_netconf)

        print("\n[4] Hasil Klasifikasi Telemetry (cpuUsage)")
        ringkasan = {"KRITIS": 0, "WASPADA": 0, "NORMAL": 0}
        for nama, cpu, status in self.hasil_telemetry:
            print(f"  {nama}: {cpu}% -> {status}")
            ringkasan[status] += 1
        print("  Ringkasan: " + ", ".join(
            f"{k}={v}" for k, v in ringkasan.items()))
        print(garis)


def jalankan(fungsi, *args):
    """Menjalankan function; kegagalan tidak menghentikan program."""
    try:
        hasil = fungsi(*args)
        return hasil if hasil is not None else "(selesai, lihat output di atas)"
    except Exception as e:
        return f"GAGAL: {e}"


def main():
    print("--- Identitas ---")
    id_perangkat = identitas.buat_id_perangkat("router", 1)
    print(id_perangkat)

    print("\n--- SSH ---")
    hasil_ssh = jalankan(ssh_modul.cek_ssh)

    print("\n--- SNMP ---")
    hasil_snmp = jalankan(snmp_modul.cek_snmp)

    print("\n--- NETCONF ---")
    pesan_netconf = jalankan(netconf_modul.buat_pesan_netconf)
    print(pesan_netconf)

    print("\n--- Telemetry ---")
    hasil_telemetry = telemetry_modul.klasifikasi_telemetry()

    laporan = LaporanCabang(id_perangkat, hasil_ssh, hasil_snmp,
                            pesan_netconf, hasil_telemetry)
    laporan.tampilkan_laporan()


if __name__ == "__main__":
    main()