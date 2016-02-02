==mc_pybackup==

A simple compression script for backing up Minecraft worlds that should work for backing up any other folder.

Usage:

* Modify WORLDS array in mcbackup.py to include any folders that you want to back up
* Set MIN_BACKUP_INTERVAL in mcbackup.py if you want to limit how often backups are created
 * Backups will be created no more often than MIN_BACKUP_INTERVAL, i.e. setting it to 6 * HOURS will limit the script to 4 backups per day
 * MIN_BACKUP_INTERVAL has no effect if it is set shorter than how often the script is run. 
* Run mcbackup.py to create backups
 * Backups are compressed as .zip for portability
 * mcbackup won't make a new backup if the original file hasn't been modified since the last backup. This saves a LOT of space if the folder isn't constantly being modified.
* Suggested: set up cron or Windows Scheduler to run your script. The included .bat file will work with Windows Scheduler.
* By default, backups will be stored in a folder named with the *two* bottom-most folders where your target is
 * In the default setup, this backups for [..]/EthosLPPackserver/world2 will be stored in ./EthosLPPackserver-world2/
 * This can be changed manually by changing the function make_backup_dir