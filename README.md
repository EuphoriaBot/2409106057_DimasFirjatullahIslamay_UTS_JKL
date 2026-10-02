# UTS Jaringan Komputer Lanjut - Integration Network with Python

Project Python modular untuk otomatisasi kantor cabang virtual: identitas,
akses SSH, monitoring SNMP, pembuatan pesan NETCONF, dan analisis telemetry.

- Nama : <Nama Lengkap Kamu>
- NIM : <NIM Kamu>
- Mata kuliah: Jaringan Komputer Lanjut, Kelas B 2024

## Struktur Folder

```
NIM_NamaLengkap_UTS_JKL/
├── .gitignore
├── README.md
├── main.py              # integrasi semua modul + class LaporanCabang
├── identitas.py         # identitas cabang & buat_id_perangkat()
├── ssh_modul.py         # cek_ssh()  (Paramiko)
├── snmp_modul.py        # cek_snmp() (PySNMP, SNMPv2c, OID sysName)
├── netconf_modul.py     # buat_pesan_netconf() (XML <rpc><edit-config>)
└── telemetry_modul.py   # klasifikasi_telemetry() (data sampel cpuUsage)
```

## Cara Menjalankan

1. Clone repository dan masuk ke foldernya.
2. Buat dan aktifkan virtual environment:

```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Linux/macOS
```

3. Install dependensi:

```
   pip install paramiko pysnmp
```

4. Jalankan program utama (Python 3.9+):

```
   python main.py
```

Jika VM/perangkat tidak dapat dihubungi, modul SSH dan SNMP menangani
kegagalan dengan try/except sehingga program tetap berjalan sampai laporan akhir.

## Ringkasan Personalisasi

- Kode cabang diturunkan dari 3 digit terakhir NIM.
- Username SSH memakai format `admin_<kode_cabang>`.
- Community string SNMP memakai format `comm_<kode_cabang>`.
- VLAN ID pada NETCONF memakai angka dari kode cabang secara langsung.
- Nilai sampel telemetry diturunkan dari digit kode cabang dengan rumus
  `cpuUsage = digit x 12 + 10`, menghasilkan variasi NORMAL, WASPADA, dan KRITIS.
- Password dan kredensial tidak dicantumkan di repository ini.
