# -*- coding: utf-8 -*-
from lib.model import Model


class MonitorResult(Model):
    __table__ = 't_monitor_result'
    CREATED_AT = 'create_time'
    UPDATED_AT = 'update_time'

    def fresh_timestamp(self):
        return Pendulum.now()