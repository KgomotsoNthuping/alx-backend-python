#!/usr/bin/env python3
"""creating asyncio tasks"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns the created asyncio.Task object"""
    return asyncio.create_task(wait_random(max_delay))
