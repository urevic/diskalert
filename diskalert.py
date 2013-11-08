#!/usr/bin/env python

import subprocess
import smtplib
from email.mime.text import MIMEText
try:
    import settings
except ImportError:
    print("Please rename settings.py.example to settings.py, edit it and try again")


class UnsupportedDfOutputFormatException(Exception):
    pass


def main():
    commands = (['df', '-h'], ['df', '-i'])
    for command in commands:
        notification_text = get_notification_text(command)
        if notification_text is not None:
            send_notification(notification_text)


def get_notification_text(command):
    """
    Runs a command (df -h or df -i), parses its output
    and returns text of notification only if disk usage at any
    mount point above the threshold
    """
    command_stdout = subprocess.Popen(command, stdout=subprocess.PIPE).stdout.readlines()
    table_captions = command_stdout[0].split()
    if table_captions[4] != 'Use%' and table_captions[4] != 'IUse%':
        unsupported_df_output_format()
    # Start notification text with table header from df output
    notification_lines = [command_stdout[0]]
    for line in command_stdout[1:]:
        if is_usage_above_threshold(line):
            notification_lines.append(line)
    if len(notification_lines) > 1:
        return "".join(notification_lines)
    else:
        return None


def is_usage_above_threshold(line):
    values = line.split()
    usage, mount_point = values[4], values[5]
    if not mount_point in settings.SKIP_MOUNT_POINTS:
        if usage == '-':
            usage = 0
        elif usage.endswith('%'):
            usage = int(usage.rstrip('%'))
        else:
            unsupported_df_output_format()
        if usage > settings.NOTIFY_IF_USAGE_GREATER_THAN:
            return True
    return False


def send_notification(text):
    if settings.SEND_NOTIFICATIONS_BY_EMAIL:
        msg = MIMEText(text)
        msg['Subject'] = 'Alert: Almost out of disk space'
        email_from = settings.EMAIL_FROM
        email_to = settings.EMAIL_TO
        msg['From'] = settings.EMAIL_FROM
        msg['To'] = settings.EMAIL_TO
        s = smtplib.SMTP(settings.SMTP)
        s.sendmail(email_from, [email_to], msg.as_string())
        s.quit()
    else:
        print(text)


def unsupported_df_output_format():
    print('Unsupported format of df output')
    raise UnsupportedDfOutputFormatException()


if __name__ == '__main__':
    try:
        main()
    except:
        # In case of any exceptions, notify about it
        # and raise again, we need to know when monitoring fails
        import sys
        import traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        exc_text = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        send_notification(exc_text)
        raise
