# -*- coding: utf-8 -*-
import arrow

from alarm.models import AlarmActive
from alarm_collect.clients.custom.baseclient import BaseClient

PROMETHEUS_LEVEL_DICT = {
    "critical": AlarmActive.FATAL,
    "minor": AlarmActive.WARNING,
    "warning": AlarmActive.REMAIN,
}


class AlarmClient(BaseClient):
    """主动推送消息"""

    # 定义是否通过ip拿到主机在cmdb中的信息
    ABOUND_HOST_CC_INFO_BY_IP = True

    def __init__(self, alarm_list, alarm_source_obj):
        super(AlarmClient, self).__init__(alarm_source_obj)
        self.alarm_list = alarm_list

    @staticmethod
    def clean_alarm_type(alarm):
        return alarm["annotations"].get("summary", "")

    @staticmethod
    def clean_alarm_time(alarm):
        return arrow.get(alarm["startsAt"]).format("YYYY-MM-DD HH:mm:ss")

    @staticmethod
    def clean_alarm_name(alarm):
        return alarm["annotations"].get("summary", "")

    @staticmethod
    def clean_event_id(alarm):
        labels = alarm.get("labels", {})
        return "{}-{}".format(labels.get("host_ip", ""), labels.get("alertname", ""))

    @staticmethod
    def clean_alarm_content(alarm):
        return alarm["annotations"].get("description", "")

    @staticmethod
    def clean_level(alarm):
        return PROMETHEUS_LEVEL_DICT.get(alarm.get("labels", {}).get("severity", "warning"))

    @staticmethod
    def clean_action(alarm):
        return alarm.get("status", "firing")

    @staticmethod
    def clean_ip(alarm):
        return alarm.get("labels", {}).get("host_ip", "")

