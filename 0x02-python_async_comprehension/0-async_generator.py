#!/usr/bin/env python3
"""Create generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Create generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
