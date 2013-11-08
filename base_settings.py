"""
Base config file for diskalert.
Normally it is a bad idea to edit it
as it can be changed in the upstream and
your changes will cause a conflict
during update. You can override anything
defined in this file in settings.py
"""

import socket

SEND_NOTIFICATIONS_BY_EMAIL = False
EMAIL_FROM = 'root@' + socket.gethostname()
EMAIL_TO = 'you@example.com'
SMTP = 'localhost'
NOTIFY_IF_USAGE_GREATER_THAN = 90  # percents
SKIP_MOUNT_POINTS = {'/dev', '/sys/fs/cgroup'}
