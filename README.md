diskalert
=========

Script for free disk space monitoring
-------------------------------------

Have you ever been in a situaion when you plenty of disk space, but thousands of small files
ate all your inodes? Unlike many others this script monitors output of both df -h and df -i, so
you'll be notified when you're either out of space or out of inodes.

Instalation
-----------

1. Clone this repo and rename settings.py.example to settings.py. 
2. Edit settings.py. For most usage scenarios you have to change the email where you want to recieve notifications and
   probably the threshold for notifications.
3. Add the script to cron.
 
