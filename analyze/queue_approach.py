"""Enum for different queue implementation approaches."""

from enum import Enum


class QueueApproach(str, Enum):
    """Enum for different queue implementation approaches."""

    dll = "dll"
    sll = "sll"
    array = "array"

    def __str__(self) -> str:
        """Return string representation of the enum value."""
        return self.value

    @property
    def option(self) -> str:
        """Return the command-line option format."""
        return f"--{self.value}"
