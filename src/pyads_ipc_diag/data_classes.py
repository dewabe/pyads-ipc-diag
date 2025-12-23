"""
data_classes.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 22.12.2025 13.58

"""
from dataclasses import dataclass

@dataclass
class TwinCAT_Info:
    major: int
    minor: int
    build: int
    ams_net_id: str
    reg_level: int
    status: int
    run_as_device: int
    show_target_visu: int
    log_file_size: int
    log_file_path: str
    system_id: str
    revision: int
    seconds_since_status_change: int

@dataclass
class CPU_Info:
    frequency: int
    usage: int
    temperature: int

@dataclass
class Mainboard_Info:
    mainboard_type: str
    serial_number: str
    production_date: str

    boot_count: int
    operating_time_minutes: int

    min_board_temperature: int
    max_board_temperature: int

    min_input_voltage: int
    max_input_voltage: int

    board_temperature: int
