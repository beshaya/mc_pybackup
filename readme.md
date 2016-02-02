==mc_pybackup==

A simple compression script for backing up Minecraft worlds that should work for backing up any other folder.

Usage:

* Modify WORLDS array in mcbackup.py to include any folders that you want to back up
* Run mcbackup.py to create backups
 * Backups are compressed as .zip for portability
 * mcbackup won't make a new backup if the original file hasn't been modified since the last backup. This saves a LOT of space if the folder isn't constantly being modified.
* Suggested: set up cron or Windows Scheduler to run your script. The included .bat file will work with Windows Scheduler.
