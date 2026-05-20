"""
High-level trainer actions for Crusader Kings III.
Provides methods to modify gold, piety, prestige, and stats.
"""

import logging
from .memory_reader import CK3MemoryReader

logger = logging.getLogger(__name__)


class CK3TrainerActions:
    """Encapsulates common trainer operations."""

    # Example static offsets (would need reverse-engineering for real use)
    # These are placeholders for demonstration.
    GOLD_OFFSET = 0x00A1B2C0
    PIETY_OFFSET = 0x00A1B2C4
    PRESTIGE_OFFSET = 0x00A1B2C8
    HEALTH_OFFSET = 0x00A1B2CC

    def __init__(self, reader: CK3MemoryReader):
        self.reader = reader

    def set_gold(self, amount: int) -> bool:
        """Set the player's gold to a specific amount."""
        try:
            addr = self.reader.base_address + self.GOLD_OFFSET
            self.reader.write_int(addr, amount)
            logger.info("Gold set to %d", amount)
            return True
        except Exception as e:
            logger.error("Failed to set gold: %s", e)
            return False

    def get_gold(self) -> int:
        """Read current gold amount."""
        try:
            addr = self.reader.base_address + self.GOLD_OFFSET
            return self.reader.read_int(addr)
        except Exception as e:
            logger.error("Failed to read gold: %s", e)
            return -1

    def set_piety(self, amount: int) -> bool:
        """Set piety to a given value."""
        try:
            addr = self.reader.base_address + self.PIETY_OFFSET
            self.reader.write_int(addr, amount)
            logger.info("Piety set to %d", amount)
            return True
        except Exception as e:
            logger.error("Failed to set piety: %s", e)
            return False

    def set_prestige(self, amount: int) -> bool:
        """Set prestige to a given value."""
        try:
            addr = self.reader.base_address + self.PRESTIGE_OFFSET
            self.reader.write_int(addr, amount)
            logger.info("Prestige set to %d", amount)
            return True
        except Exception as e:
            logger.error("Failed to set prestige: %s", e)
            return False

    def set_health(self, amount: float) -> bool:
        """Set character health (float)."""
        try:
            addr = self.reader.base_address + self.HEALTH_OFFSET
            self.reader.write_float(addr, amount)
            logger.info("Health set to %.2f", amount)
            return True
        except Exception as e:
            logger.error("Failed to set health: %s", e)
            return False

    def get_health(self) -> float:
        """Read current health value."""
        try:
            addr = self.reader.base_address + self.HEALTH_OFFSET
            return self.reader.read_float(addr)
        except Exception as e:
            logger.error("Failed to read health: %s", e)
            return -1.0
