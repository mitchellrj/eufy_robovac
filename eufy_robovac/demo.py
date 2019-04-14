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
import pprint
import sys

from eufy_robovac.robovac import Robovac


async def connected_callback(message, device):
    print("Connected. Current device state:")
    pprint.pprint(device.state)


async def cleaning_started_callback(message, device):
    print("Cleaning started.")


async def go_home_callback(message, device):
    print("Device on its way home.")


async def async_main(device_id, local_key, ip, *args, **kwargs):
    r = Robovac(device_id, local_key, ip, *args, **kwargs)
    await r.async_connect(connected_callback)
    await asyncio.sleep(5)
    print("Starting cleaning...")
    await r.async_start_cleaning(cleaning_started_callback)
    await asyncio.sleep(30)
    print("Sending home...")
    await r.async_go_home(go_home_callback)
    await asyncio.sleep(10)
    print("Disconnecting...")
    await r.async_disconnect()


def main(*args, **kwargs):
    if not args:
        args = sys.argv[1:]
    asyncio.run(async_main(*args, **kwargs))


if __name__ == '__main__':
    main(*sys.argv[1:])
