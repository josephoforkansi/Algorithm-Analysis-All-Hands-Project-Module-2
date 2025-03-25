"""Timing utilities for data structure operations."""

import functools
import time
from typing import Dict, Any


class TimingResult:
    """Store timing results for a data structure's operations."""

    def __init__(self, name: str):
        self.name = name
        self.operations = {}  # Dict of operation_name -> (total_time, total_elements)
        self.total_time = 0.0

    def add_timing(self, operation: str, time_taken: float, elements: int):
        """Add timing result for an operation."""
        if operation not in self.operations:
            self.operations[operation] = (0.0, 0)
        curr_time, curr_elements = self.operations[operation]
        self.operations[operation] = (curr_time + time_taken, curr_elements + elements)
        self.total_time += time_taken


def timed(operation_name: str):
    """Decorator to time the execution of an operation."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            count = kwargs.get("count", 1)
            total_time = 0.0

            # Time each iteration separately to get accurate measurements
            for _ in range(count):
                start = time.perf_counter()
                result = func(self, *args, **kwargs)
                elapsed = time.perf_counter() - start
                total_time += elapsed

            # Add timing to results if the object has timing_result attribute
            if hasattr(self, "timing_result"):
                self.timing_result.add_timing(operation_name, total_time, count)
            return result

        return wrapper

    return decorator
