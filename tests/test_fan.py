"""
test_fan.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 23.12.2025 10.57

"""
from fake_ipc import FakeIPC

from pyads_ipc_diag.service.fan import Fan
from pyads_ipc_diag.areas import CONFIG_AREA
from pyads_ipc_diag.data_types import SIGNED16


def test_memory_info():
    ipc = FakeIPC()
    fan = Fan(ipc)

    info = fan.info()

    # Values
    assert info.speed == 2500

    # Calls (order matters)
    assert (CONFIG_AREA.FAN, 0x8001, 1, SIGNED16) in ipc.calls