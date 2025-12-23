"""
fake_ipc.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 23.12.2025 10.18

"""
from pyads_ipc_diag.areas import CONFIG_AREA
from pyads_ipc_diag.data_types import (
    UNSIGNED16,
    UNSIGNED32,
    SIGNED16,
    UNSIGNED64,
    VISIBLE_STRING,
    BOOL
)

class FakeIPC:
    def __init__(self):
        self.calls = []
        self.responses = {
            # Memory
            (CONFIG_AREA.MEMORY, 0x8001, 1, UNSIGNED32): 1024,
            (CONFIG_AREA.MEMORY, 0x8001, 2, UNSIGNED32): 2048,
            (CONFIG_AREA.MEMORY, 0x8001, 3, UNSIGNED32): 0,
            (CONFIG_AREA.MEMORY, 0x8001, 4, UNSIGNED32): 0,
            (CONFIG_AREA.MEMORY, 0x8001, 5, UNSIGNED32): 0,
            (CONFIG_AREA.MEMORY, 0x8001, 6, UNSIGNED64): 0,
            (CONFIG_AREA.MEMORY, 0x8001, 7, UNSIGNED64): 0,

            # CPU
            (CONFIG_AREA.CPU, 0x8001, 1, UNSIGNED32): 1917,
            (CONFIG_AREA.CPU, 0x8001, 2, UNSIGNED16): 3,
            (CONFIG_AREA.CPU, 0x8001, 3, SIGNED16): 43,

            # Fan
            (CONFIG_AREA.FAN, 0x8001, 1, SIGNED16): 2500,

            # NIC
            (CONFIG_AREA.NIC, 0x8001, 1, VISIBLE_STRING): "00:11:22:33:44:55",
            (CONFIG_AREA.NIC, 0x8001, 2, VISIBLE_STRING): "192.168.1.100",
            (CONFIG_AREA.NIC, 0x8001, 3, VISIBLE_STRING): "255.255.255.0",
            (CONFIG_AREA.NIC, 0x8001, 4, BOOL): True,
            (CONFIG_AREA.NIC, 0x8001, 5, VISIBLE_STRING): "192.168.1.1",
            (CONFIG_AREA.NIC, 0x8001, 6, VISIBLE_STRING): "8.8.8.8",
            (CONFIG_AREA.NIC, 0x8001, 7, VISIBLE_STRING): "eth0",
            (CONFIG_AREA.NIC, 0x8001, 8, VISIBLE_STRING): "2",
        }

    def read(self, module, table_base, subindex, plc_type):
        key = (module, table_base, subindex, plc_type)
        self.calls.append(key)
        try:
            return self.responses[key]
        except KeyError:
            raise AssertionError(f"Unexpected read() call: {key}")

