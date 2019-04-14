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

import logging

from .tuya import TuyaDevice


_LOGGER = logging.getLogger(__name__)


class WorkMode:
    AUTO = 'auto'
    NO_SWEEP = 'Nosweep'
    SMALL_ROOM = 'SmallRoom'
    EDGE = 'Edge'
    Spot = 'Spot'


class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    FORWARD = 'forward'
    BACKWARD = 'backward'


class WorkStatus:
    CHARGING = 'Charging'
    STAND_BY = 'standby'
    SLEEPING = 'Sleeping'
    RECHARGING = 'Recharge'


class CleanSpeed:
    NO_SUCTION = 'No_suction'
    STANDARD = 'Standard'
    BOOST_IQ = 'Boost_IQ'
    MAX = 'Max'


class ErrorCode:
    pass


class Robovac(TuyaDevice):
    """Represents a generic Eufy Robovac."""

    PLAY_PAUSE = '2'
    DIRECTION = '3'
    WORK_MODE = '5'
    WORK_STATUS = '15'
    GO_HOME = '101'
    CLEAN_SPEED = '102'
    FIND_ROBOT = '103'
    BATTERY_LEVEL = '104'
    ERROR_CODE = '106'
    KEY_NAMES = {
        PLAY_PAUSE: 'play/pause',
        DIRECTION: 'direction',
        WORK_MODE: 'work mode',
        WORK_STATUS: 'work status',
        GO_HOME: 'go home',
        CLEAN_SPEED: 'clean speed',
        FIND_ROBOT: 'find robot',
        BATTERY_LEVEL: 'battery level',
        ERROR_CODE: 'error code'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def async_start_cleaning(self, callback=None):
        await self.async_set({self.WORK_MODE: WorkMode.AUTO}, callback)

    async def async_go_home(self, callback=None):
        await self.async_set({self.GO_HOME: True}, callback)
