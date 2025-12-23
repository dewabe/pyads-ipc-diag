"""
test_cpu.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 23.12.2025 10.10

"""
from pyads_ipc_diag.service.cpu import CPU
from pyads_ipc_diag.areas import CONFIG_AREA
from pyads_ipc_diag.data_types import UNSIGNED16, UNSIGNED32, SIGNED16


def test_cpu_info(fake_ipc):
    cpu = CPU(fake_ipc)

    info = cpu.info()

    # Values
    assert info.frequency == 1917
    assert info.usage == 3
    assert info.temperature == 43

    # Calls (order matters)
    assert fake_ipc.calls == [
        (CONFIG_AREA.CPU, 0x8001, 1, UNSIGNED32),
        (CONFIG_AREA.CPU, 0x8001, 2, UNSIGNED16),
        (CONFIG_AREA.CPU, 0x8001, 3, SIGNED16),
    ]
