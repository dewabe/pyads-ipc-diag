"""
fake_ipc.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 23.12.2025 10.18

"""
from ctypes import (
    c_uint16,
    c_uint32,
    c_int16
)

CONFIG_AREA_CPU = 0x000B

class FakeIPC:
    """Minimal fake IPC that records read() calls and returns predefined values."""
    def __init__(self):
        self.calls = []

    def read(self, module, table_base, subindex, plc_type):
        self.calls.append((module, table_base, subindex, plc_type))

        # Return dummy values based on subindex (CPU.TABLE_BASE = 0x8001)
        if (module, table_base, subindex, plc_type) == (CONFIG_AREA_CPU, 0x8001, 1, c_uint32):
            return 1917  # frequency
        if (module, table_base, subindex, plc_type) == (CONFIG_AREA_CPU, 0x8001, 2, c_uint16):
            return 3  # usage
        if (module, table_base, subindex, plc_type) == (CONFIG_AREA_CPU, 0x8001, 3, c_int16):
            return 43  # temperature

        raise AssertionError(f"Unexpected read() call: {(module, table_base, subindex, plc_type)}")