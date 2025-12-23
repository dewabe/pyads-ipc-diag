"""
test_fan.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 23.12.2025 10.57

"""
from pyads_ipc_diag import CONFIG_AREA
from pyads_ipc_diag.service.fan import Fan
from pyads_ipc_diag.data_types import SIGNED16


def test_memory_info(fake_ipc):
    fan = Fan(fake_ipc)

    info = fan.info()

    # Values
    assert info.speed == 2500

    # Calls (order matters)
    assert (CONFIG_AREA.FAN, 0x8001, 1, SIGNED16) in fake_ipc.calls