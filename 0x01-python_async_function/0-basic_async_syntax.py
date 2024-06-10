#!/usr/bin/env python3
"""asynchronous"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random float"""
    r = random.random() * max_delay
    await asyncio.sleep(r)
    return r
