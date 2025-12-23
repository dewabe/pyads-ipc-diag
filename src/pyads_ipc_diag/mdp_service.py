"""
mdp_service.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 22.12.2025 13.51

"""
from .areas import CONFIG_AREA
from . import data_types as dtypes
from .data_classes import TwinCAT_Info, CPU_Info,\
    Mainboard_Info, Memory_Info


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

class TwinCAT(MDPService):
    MODULE = CONFIG_AREA.TWINCAT
    TABLE_BASE = 0x8001

    def __init__(self, ipc):
        self.ipc = ipc
        self._major = None
        self._minor = None
        self._build = None
        self._ams_net_id = None
        self._reg_level = None
        self._status = None
        self._run_as_device = None
        self._show_target_visu = None
        self._log_file_size = None
        self._log_file_path = None
        self._system_id = None
        self._revision = None
        self._seconds_since_status_change = None

    @property
    def major(self) -> int:
        """Major Version (UNSIGNED16)"""
        if self._major is None:
            self._major = self._u16(1)
        return self._major

    @property
    def minor(self) -> int:
        """Minor Version (UNSIGNED16)"""
        if self._minor is None:
            self._minor = self._u16(2)
        return self._minor

    @property
    def build(self) -> int:
        """Build (UNSIGNED16)"""
        if self._build is None:
            self._build = self._u16(3)
        return self._build

    @property
    def ams_net_id(self) -> str:
        """Ams Net ID (VISIBLE STRING)"""
        if self._ams_net_id is None:
            self._ams_net_id = self._string(4)
        return self._ams_net_id

    @property
    def reg_level(self) -> int:
        """Reg Level (UNSIGNED32) - only for TwinCAT 2"""
        if self._reg_level is None:
            self._reg_level = self._u32(5)
        return self._reg_level

    @property
    def status(self) -> int:
        """TwinCAT Status (UNSIGNED16)"""
        if self._status is None:
            self._status = self._u16(6)
        return self._status

    @property
    def run_as_device(self) -> int:
        """RunAsDevice (UNSIGNED16) - only for Windows CE"""
        if self._run_as_device is None:
            self._run_as_device = self._u16(7)
        return self._run_as_device

    @property
    def show_target_visu(self) -> int:
        """ShowTargetVisu (UNSIGNED16) - only for Windows CE"""
        if self._show_target_visu is None:
            self._show_target_visu = self._u16(8)
        return self._show_target_visu

    @property
    def log_file_size(self) -> int:
        """Log File size (UNSIGNED32) - only for Windows CE"""
        if self._log_file_size is None:
            self._log_file_size = self._u32(9)
        return self._log_file_size

    @property
    def log_file_path(self) -> str:
        """Log File Path (VISIBLE STRING) - only for Windows CE"""
        if self._log_file_path is None:
            self._log_file_path = self._string(10)
        return self._log_file_path

    @property
    def system_id(self) -> str:
        """TwinCAT System ID (VISIBLE STRING) - MDP v1.6+"""
        if self._system_id is None:
            self._system_id = self._string(11)
        return self._system_id

    @property
    def revision(self) -> int:
        """TwinCAT Revision (UNSIGNED16)"""
        if self._revision is None:
            self._revision = self._u16(12)
        return self._revision

    @property
    def seconds_since_status_change(self) -> int:
        """Seconds since last TwinCAT status change (UNSIGNED64)"""
        if self._seconds_since_status_change is None:
            self._seconds_since_status_change = self._u64(13)
        return self._seconds_since_status_change

    def info(self) -> TwinCAT_Info:
        """Return all TwinCAT information as a dataclass"""
        return TwinCAT_Info(
            major=self.major,
            minor=self.minor,
            build=self.build,
            ams_net_id=self.ams_net_id,
            reg_level=self.reg_level,
            status=self.status,
            run_as_device=self.run_as_device,
            show_target_visu=self.show_target_visu,
            log_file_size=self.log_file_size,
            log_file_path=self.log_file_path,
            system_id=self.system_id,
            revision=self.revision,
            seconds_since_status_change=self.seconds_since_status_change,
        )

    def version(self):
        """Convenience: return (major, minor, build)"""
        return self.major, self.minor, self.build

    def refresh(self):
        """Force re-reading all TwinCAT values from IPC"""
        self._major = None
        self._minor = None
        self._build = None
        self._ams_net_id = None
        self._reg_level = None
        self._status = None
        self._run_as_device = None
        self._show_target_visu = None
        self._log_file_size = None
        self._log_file_path = None
        self._system_id = None
        self._revision = None
        self._seconds_since_status_change = None

class CPU(MDPService):
    MODULE = CONFIG_AREA.CPU
    TABLE_BASE = 0x8001

    def __init__(self, ipc):
        self.ipc = ipc
        self._frequency = None
        self._usage = None
        self._temperature = None

    @property
    def frequency(self) -> int:
        """CPU frequency (UNSIGNED32)"""
        if self._frequency is None:
            self._frequency = self._u32(1)
        return self._frequency

    @property
    def usage(self) -> int:
        """CPU usage in percent (UNSIGNED16)"""
        if self._usage is None:
            self._usage = self._u16(2)
        return self._usage

    @property
    def temperature(self) -> int:
        """CPU temperature (SIGNED16)"""
        if self._temperature is None:
            self._temperature = self._s16(3)
        return self._temperature

    def info(self) -> CPU_Info:
        """Return all CPU information as a dataclass"""
        return CPU_Info(
            frequency=self.frequency,
            usage=self.usage,
            temperature=self.temperature,
        )

    def refresh(self):
        """Force re-reading all CPU values from IPC"""
        self._frequency = None
        self._usage = None
        self._temperature = None

class Mainboard(MDPService):
    MODULE = CONFIG_AREA.MAINBOARD
    TABLE_BASE = 0x8001

    def __init__(self, ipc):
        self.ipc = ipc
        self._mainboard_type = None
        self._serial_number = None
        self._production_date = None
        self._boot_count = None
        self._operating_time_minutes = None
        self._min_board_temperature = None
        self._max_board_temperature = None
        self._min_input_voltage = None
        self._max_input_voltage = None
        self._board_temperature = None

    @property
    def mainboard_type(self) -> str:
        """Mainboard type (VISIBLE STRING)"""
        if self._mainboard_type is None:
            self._mainboard_type = self._string(1)
        return self._mainboard_type

    @property
    def serial_number(self) -> str:
        """Serial number (VISIBLE STRING)"""
        if self._serial_number is None:
            self._serial_number = self._string(2)
        return self._serial_number

    @property
    def production_date(self) -> str:
        """Production date (VISIBLE STRING)"""
        if self._production_date is None:
            self._production_date = self._string(3)
        return self._production_date

    @property
    def boot_count(self) -> int:
        """Boot count (UNSIGNED32)"""
        if self._boot_count is None:
            self._boot_count = self._u32(4)
        return self._boot_count

    @property
    def operating_time_minutes(self) -> int:
        """Operating time in minutes (UNSIGNED32)"""
        if self._operating_time_minutes is None:
            self._operating_time_minutes = self._u32(5)
        return self._operating_time_minutes

    @property
    def min_board_temperature(self) -> int:
        """Minimum board temperature (SIGNED32, °C)"""
        if self._min_board_temperature is None:
            self._min_board_temperature = self._s32(6)
        return self._min_board_temperature

    @property
    def max_board_temperature(self) -> int:
        """Maximum board temperature (SIGNED32, °C)"""
        if self._max_board_temperature is None:
            self._max_board_temperature = self._s32(7)
        return self._max_board_temperature

    @property
    def min_input_voltage(self) -> int:
        """Minimum input voltage (SIGNED32, mV)"""
        if self._min_input_voltage is None:
            self._min_input_voltage = self._s32(8)
        return self._min_input_voltage

    @property
    def max_input_voltage(self) -> int:
        """Maximum input voltage (SIGNED32, mV)"""
        if self._max_input_voltage is None:
            self._max_input_voltage = self._s32(9)
        return self._max_input_voltage

    @property
    def board_temperature(self) -> int:
        """Current board temperature (SIGNED16, °C)"""
        if self._board_temperature is None:
            self._board_temperature = self._s16(10)
        return self._board_temperature

    def info(self) -> Mainboard_Info:
        """Return all mainboard information as a dataclass"""
        return Mainboard_Info(
            mainboard_type=self.mainboard_type,
            serial_number=self.serial_number,
            production_date=self.production_date,
            boot_count=self.boot_count,
            operating_time_minutes=self.operating_time_minutes,
            min_board_temperature=self.min_board_temperature,
            max_board_temperature=self.max_board_temperature,
            min_input_voltage=self.min_input_voltage,
            max_input_voltage=self.max_input_voltage,
            board_temperature=self.board_temperature,
        )

    def refresh(self):
        """Force re-reading all mainboard values from IPC"""
        self._mainboard_type = None
        self._serial_number = None
        self._production_date = None
        self._boot_count = None
        self._operating_time_minutes = None
        self._min_board_temperature = None
        self._max_board_temperature = None
        self._min_input_voltage = None
        self._max_input_voltage = None
        self._board_temperature = None

class Memory(MDPService):
    MODULE = CONFIG_AREA.MEMORY
    TABLE_BASE = 0x8001

    def __init__(self, ipc):
        self.ipc = ipc
        self._program_allocated_u32 = None
        self._program_available_u32 = None
        self._storage_allocated_u32 = None
        self._storage_available_u32 = None
        self._memory_division_u32 = None
        self._program_allocated_u64 = None
        self._program_available_u64 = None

    # --- always available (per your table) ---

    @property
    def program_allocated_u32(self) -> int:
        """Program Memory Allocated (UNSIGNED32)"""
        if self._program_allocated_u32 is None:
            self._program_allocated_u32 = self._u32(1)
        return self._program_allocated_u32

    @property
    def program_available_u32(self) -> int:
        """Program Memory Available (UNSIGNED32)"""
        if self._program_available_u32 is None:
            self._program_available_u32 = self._u32(2)
        return self._program_available_u32

    # --- Windows CE only (may not exist on many targets) ---

    @property
    def storage_allocated_u32(self):
        """Storage Memory Allocated (UNSIGNED32) - only for Windows CE"""
        if self._storage_allocated_u32 is None:
            self._storage_allocated_u32 = self._u32(3)
        return self._storage_allocated_u32

    @property
    def storage_available_u32(self):
        """Storage Memory Available (UNSIGNED32) - only for Windows CE"""
        if self._storage_available_u32 is None:
            self._storage_available_u32 = self._u32(4)
        return self._storage_available_u32

    @property
    def memory_division_u32(self):
        """Memory Division (UNSIGNED32) - only for Windows CE (read-write)"""
        if self._memory_division_u32 is None:
            self._memory_division_u32 = self._u32(5)
        return self._memory_division_u32

    # --- MDP v1.7+ (64-bit counters) ---

    @property
    def program_allocated_u64(self):
        """Program Memory Allocated (UNSIGNED64) - MDP v1.7+"""
        if self._program_allocated_u64 is None:
            self._program_allocated_u64 = self._u64(6)
        return self._program_allocated_u64

    @property
    def program_available_u64(self):
        """Program Memory Available (UNSIGNED64) - MDP v1.7+"""
        if self._program_available_u64 is None:
            self._program_available_u64 = self._u64(7)
        return self._program_available_u64

    def info(self) -> Memory_Info:
        """Return all memory information as a dataclass"""
        return Memory_Info(
            program_allocated_u32=self.program_allocated_u32,
            program_available_u32=self.program_available_u32,
            storage_allocated_u32=self.storage_allocated_u32,
            storage_available_u32=self.storage_available_u32,
            memory_division_u32=self.memory_division_u32,
            program_allocated_u64=self.program_allocated_u64,
            program_available_u64=self.program_available_u64,
        )

    def refresh(self):
        """Force re-reading all memory values from IPC"""
        self._program_allocated_u32 = None
        self._program_available_u32 = None
        self._storage_allocated_u32 = None
        self._storage_available_u32 = None
        self._memory_division_u32 = None
        self._program_allocated_u64 = None
        self._program_available_u64 = None
