"""
basic.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 22.12.2025 8.56

"""
import pyads_ipc_diag as bhf

# Connect to IPC/EPC
with bhf.MDP("10.10.10.11.1.1") as ipc:

    # Read Operating System using prepared OS class
    os = bhf.OS(ipc)
    print(os.info())

    # Read MAC address using module, table and subindex
    mac_address = ipc.read(bhf.CONFIG_AREA.NIC, 0x8001, 1, bhf.VISIBLE_STRING)
    print(mac_address) # nn:nn:nn:nn:nn:nn