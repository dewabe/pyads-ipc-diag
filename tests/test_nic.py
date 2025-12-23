"""
test_nic.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 23.12.2025 11.46

"""
from pyads_ipc_diag.service.nic import NIC
from pyads_ipc_diag.areas import CONFIG_AREA
from pyads_ipc_diag.data_types import VISIBLE_STRING, BOOL


def test_nic(fake_ipc):
    nic = NIC(fake_ipc)

    # Read values (lazy properties)
    assert nic.mac_address == "00:11:22:33:44:55"
    assert nic.ipv4_address == "192.168.1.100"
    assert nic.ipv4_netmask == "255.255.255.0"
    assert nic.dhcp_enabled is True
    assert nic.ipv4_gateway == "192.168.1.1"
    assert nic.ipv4_dns == "8.8.8.8"
    assert nic.virtual_device_name == "eth0"
    assert nic.ipv4_dns_servers_active == "2"

    # Verify ADS reads (order matters because we accessed properties in this order)
    assert fake_ipc.calls == [
        (CONFIG_AREA.NIC, 0x8001, 1, VISIBLE_STRING),
        (CONFIG_AREA.NIC, 0x8001, 2, VISIBLE_STRING),
        (CONFIG_AREA.NIC, 0x8001, 3, VISIBLE_STRING),
        (CONFIG_AREA.NIC, 0x8001, 4, BOOL),
        (CONFIG_AREA.NIC, 0x8001, 5, VISIBLE_STRING),
        (CONFIG_AREA.NIC, 0x8001, 6, VISIBLE_STRING),
        (CONFIG_AREA.NIC, 0x8001, 7, VISIBLE_STRING),
        (CONFIG_AREA.NIC, 0x8001, 8, VISIBLE_STRING),
    ]
