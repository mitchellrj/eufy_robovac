# -*- coding: utf-8 -*-

# Copyright 2019 Richard Mitchell
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import logging
import pprint
import sys

from eufy_robovac.robovac import Robovac


logging.basicConfig(level=logging.DEBUG)


async def connected_callback(message, device):
    print("Connected. Current device state:")
    pprint.pprint(device.state)


async def cleaning_started_callback(message, device):
    print("Cleaning started.")


async def async_main(device_id, ip, local_key=None, *args, **kwargs):
    r = Robovac(device_id, ip, local_key, *args, **kwargs)
    await r.async_connect(connected_callback)
    await asyncio.sleep(1)
    print("Starting cleaning...")
    await r.async_start_cleaning(cleaning_started_callback)
    await asyncio.sleep(5)
    print("Pausing...")
    r.play_pause = False
    await asyncio.sleep(1)
    print("Disconnecting...")
    await r.async_disconnect()


def main(*args, **kwargs):
    if not args:
        args = sys.argv[1:]
    asyncio.run(async_main(*args, **kwargs))


if __name__ == '__main__':
    main(*sys.argv[1:])
