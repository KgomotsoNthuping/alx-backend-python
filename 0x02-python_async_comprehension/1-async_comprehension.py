#!/usr/bin/env python3
"""Generate list from async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns async generated list"""
    return [_ async for _ in async_generator()]
