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

import enum


class StringEnum(enum.Enum):

    def __str__(self):
        return self.value


class DeviceProperty:

    def __init__(self, key, type_cast=None, read_only=False):
        self.key = key
        self.type_cast = type_cast
        self.read_only = read_only

    def __get__(self, instance, owner):
        value = instance.state.get(self.key)
        if value is not None and self.type_cast is not None:
            value = self.type_cast(value)
        return value

    def __set__(self, instance, value):
        if self.read_only:
            raise AttributeError("can't set attribute")

        if not isinstance(value, (bool, int, float, str, type(None))):
            value = str(value)
        instance.set({self.key: value})
