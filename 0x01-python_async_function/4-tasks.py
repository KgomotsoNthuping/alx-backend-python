#!/usr/bin/env python3
"""creating and running multiple asyncio tasks"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """creating and running multiple asyncio tasks"""
    r = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(r)
