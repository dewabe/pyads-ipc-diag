"""
conftest.py

Project: pyads-ipc-diag
:author: Teemu Vartiainen
:license: MIT
:created on: 23.12.2025 11.48

"""
import pytest
from fake_ipc import FakeIPC

@pytest.fixture
def fake_ipc():
    return FakeIPC()