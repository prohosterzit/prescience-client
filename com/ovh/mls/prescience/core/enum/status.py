# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Copyright 2019 The Prescience-Client Authors. All rights reserved.

from enum import Enum, unique, auto
from termcolor import colored

@unique
class Status(Enum):
    # Tasks status
    PENDING = auto()
    SCHEDULED = auto()
    RUNNING = auto()
    ERROR = auto()
    DONE = auto()
    INTERRUPTED = auto()

    # Entity status
    BUILDING = auto()
    BUILT = auto()
    FAILED = auto()
    OUTDATED = auto()

    def __str__(self):
        switch = {
            Status.PENDING: 'PENDING',
            Status.SCHEDULED: 'SCHEDULED',
            Status.RUNNING: 'RUNNING',
            Status.ERROR: 'ERROR',
            Status.DONE: 'DONE',
            Status.INTERRUPTED: 'INTERRUPTED',

            Status.BUILDING: 'BUILDING',
            Status.BUILT: 'BUILT',
            Status.FAILED: 'FAILED',
            Status.OUTDATED: 'OUTDATED'
        }
        return colored(switch.get(self), self.color())

    def color(self):
        switch = {
            Status.PENDING: 'yellow',
            Status.SCHEDULED: 'yellow',
            Status.RUNNING: 'yellow',
            Status.ERROR: 'red',
            Status.DONE: 'green',
            Status.INTERRUPTED: 'magenta',

            Status.BUILDING: 'yellow',
            Status.BUILT: 'green',
            Status.FAILED: 'red',
            Status.OUTDATED: 'cyan'
        }
        return switch.get(self)