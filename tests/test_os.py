"""
test_os.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 23.12.2025 12.20

"""
from pyads_ipc_diag import CONFIG_AREA
from pyads_ipc_diag.service.os import OS
from pyads_ipc_diag.data_types import UNSIGNED32, VISIBLE_STRING


def test_os_info(fake_ipc):
    os = OS(fake_ipc)

    info = os.info()

    # Values
    assert info.major_version == 10
    assert info.minor_version == 0
    assert info.build == 19045
    assert info.csd_version == "22H2"

    # Calls (order does not strictly matter)
    assert (CONFIG_AREA.OS, 0x8001, 1, UNSIGNED32) in fake_ipc.calls
    assert (CONFIG_AREA.OS, 0x8001, 2, UNSIGNED32) in fake_ipc.calls
    assert (CONFIG_AREA.OS, 0x8001, 3, UNSIGNED32) in fake_ipc.calls
    assert (CONFIG_AREA.OS, 0x8001, 4, VISIBLE_STRING) in fake_ipc.calls
