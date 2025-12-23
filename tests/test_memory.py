"""
test_memory.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 23.12.2025 10.32

"""
from pyads_ipc_diag.service.memory import Memory
from pyads_ipc_diag.areas import CONFIG_AREA
from pyads_ipc_diag.data_types import UNSIGNED32


def test_memory_info(fake_ipc):
    memory = Memory(fake_ipc)

    info = memory.info()

    # Values
    assert info.program_allocated_u32 == 1024
    assert info.program_available_u32 == 2048

    # Calls (order matters)
    assert (CONFIG_AREA.MEMORY, 0x8001, 1, UNSIGNED32) in fake_ipc.calls
    assert (CONFIG_AREA.MEMORY, 0x8001, 2, UNSIGNED32) in fake_ipc.calls
