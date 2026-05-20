"""
Module for reading and writing process memory for Crusader Kings III.
Uses pymem for Windows process interaction.
"""

import pymem
import pymem.process
import logging

logger = logging.getLogger(__name__)


class CK3MemoryReader:
    """Handles low-level memory operations for the CK3 process."""

    PROCESS_NAME = "ck3.exe"

    def __init__(self):
        self.pm = None
        self.base_address = None
        self.attached = False

    def attach(self) -> bool:
        """Attach to the CK3 process. Returns True on success."""
        try:
            self.pm = pymem.Pymem(self.PROCESS_NAME)
            self.base_address = pymem.process.module_from_name(
                self.pm.process_handle, self.PROCESS_NAME
            ).lpBaseOfDll
            self.attached = True
            logger.info("Attached to CK3 process at base 0x%X", self.base_address)
            return True
        except pymem.exception.ProcessNotFound:
            logger.error("CK3 process not found. Is the game running?")
            return False
        except Exception as e:
            logger.exception("Failed to attach: %s", e)
            return False

    def read_int(self, address: int) -> int:
        """Read a 4-byte integer from game memory."""
        if not self.attached:
            raise RuntimeError("Not attached to process")
        return self.pm.read_int(address)

    def write_int(self, address: int, value: int) -> None:
        """Write a 4-byte integer to game memory."""
        if not self.attached:
            raise RuntimeError("Not attached to process")
        self.pm.write_int(address, value)

    def read_float(self, address: int) -> float:
        """Read a 4-byte float from game memory."""
        if not self.attached:
            raise RuntimeError("Not attached to process")
        return self.pm.read_float(address)

    def write_float(self, address: int, value: float) -> None:
        """Write a 4-byte float to game memory."""
        if not self.attached:
            raise RuntimeError("Not attached to process")
        self.pm.write_float(address, value)

    def get_pointer_address(self, base: int, offsets: list) -> int:
        """
        Follow a chain of pointers to resolve the final address.
        base: base address (e.g., module base + static offset)
        offsets: list of offsets to follow sequentially
        """
        addr = self.pm.read_int(base)
        for offset in offsets[:-1]:
            addr = self.pm.read_int(addr + offset)
        return addr + offsets[-1] if offsets else addr

    def detach(self) -> None:
        """Cleanly detach from the process."""
        if self.pm:
            self.pm.close_process()
            self.attached = False
            logger.info("Detached from CK3 process")
