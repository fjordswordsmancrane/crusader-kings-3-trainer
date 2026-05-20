"""
Unit tests for CK3TrainerActions.
Uses mocking to avoid requiring the actual game process.
"""

import unittest
from unittest.mock import MagicMock, patch
from src.trainer_actions import CK3TrainerActions
from src.memory_reader import CK3MemoryReader


class TestCK3TrainerActions(unittest.TestCase):
    """Test suite for trainer actions."""

    def setUp(self):
        """Set up a mock memory reader before each test."""
        self.mock_reader = MagicMock(spec=CK3MemoryReader)
        self.mock_reader.base_address = 0x10000000
        self.actions = CK3TrainerActions(self.mock_reader)

    def test_set_gold_success(self):
        """Test that set_gold writes the correct value."""
        self.mock_reader.write_int = MagicMock()
        result = self.actions.set_gold(5000)
        self.assertTrue(result)
        expected_addr = self.mock_reader.base_address + self.actions.GOLD_OFFSET
        self.mock_reader.write_int.assert_called_once_with(expected_addr, 5000)

    def test_set_gold_failure(self):
        """Test that set_gold returns False on exception."""
        self.mock_reader.write_int.side_effect = RuntimeError("Memory error")
        result = self.actions.set_gold(100)
        self.assertFalse(result)

    def test_get_gold_success(self):
        """Test reading gold returns expected value."""
        self.mock_reader.read_int.return_value = 1234
        gold = self.actions.get_gold()
        self.assertEqual(gold, 1234)
        expected_addr = self.mock_reader.base_address + self.actions.GOLD_OFFSET
        self.mock_reader.read_int.assert_called_once_with(expected_addr)

    def test_get_gold_failure(self):
        """Test get_gold returns -1 on error."""
        self.mock_reader.read_int.side_effect = Exception("Read error")
        gold = self.actions.get_gold()
        self.assertEqual(gold, -1)

    def test_set_health_float(self):
        """Test that set_health writes a float value."""
        self.mock_reader.write_float = MagicMock()
        result = self.actions.set_health(95.5)
        self.assertTrue(result)
        expected_addr = self.mock_reader.base_address + self.actions.HEALTH_OFFSET
        self.mock_reader.write_float.assert_called_once_with(expected_addr, 95.5)

    def test_get_health_float(self):
        """Test reading health returns float."""
        self.mock_reader.read_float.return_value = 80.0
        health = self.actions.get_health()
        self.assertAlmostEqual(health, 80.0)


if __name__ == "__main__":
    unittest.main()
