diskalert
=========

Script for free disk space monitoring
-------------------------------------

Have you ever been in a situaion when you have plenty of disk space, but thousands of small files
ate all of your inodes? Unlike many others this script monitors output of both `df -h` and `df -i`, so
you'll be notified when you're either out of space or out of inodes.

Instalation
-----------

1. Clone this repository and 

    `git clone git://github.com/urevic/diskalert.git`
    
2. Copy settings.py.example to settings.py

    `cp ./settings.py.example ./settings.py`

3. Edit settings.py. For most usage scenarios you have to change the email where you want to recieve notifications and
   probably the threshold for notifications

    `vim ./settings.py`

4. Add the script to cron

    `crontab -e`
 
