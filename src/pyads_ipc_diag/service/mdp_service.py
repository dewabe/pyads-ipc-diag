"""
mdp_service.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 22.12.2025 13.51

"""
from pyads_ipc_diag import data_types as dtypes


class MDPService:
    """High level class for reading MDP data """
    def _read(self, subindex, var_type) -> int :
        return self.ipc.read(self.MODULE, self.TABLE_BASE, subindex, var_type)

    def _u16(self, subindex: int) -> int:
        return self._read(subindex, dtypes.UNSIGNED16)

    def _s16(self, subindex: int) -> int:
        return self._read(subindex, dtypes.SIGNED16)

    def _u32(self, subindex: int) -> int:
        return self._read(subindex, dtypes.UNSIGNED32)

    def _s32(self, subindex: int) -> int:
        return self._read(subindex, dtypes.SIGNED32)

    def _u64(self, subindex: int) -> int:
        return self._read(subindex, dtypes.UNSIGNED64)

    def _string(self, subindex: int) -> str:
        return self._read(subindex, dtypes.VISIBLE_STRING)