import os, zipfile, json
import time, datetime

WORLDS = ["C:\\ftb\\EthosLPPackserver\\EthosLPPackserver-bk\\EthosLPPackserver\\world2"]
backupLog = "mcbackup.log"

def zip_dir(zipname, dir_to_zip):
    dir_to_zip_len = len(dir_to_zip.rstrip(os.sep)) + 1
    with zipfile.ZipFile(zipname, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for dirname, subdirs, files in os.walk(dir_to_zip):
            for filename in files:
                path = os.path.join(dirname, filename)
                entry = path[dir_to_zip_len:]
                zf.write(path, entry)	

def get_dir_modified(dir):
    lastModified = 0
    for dirname, subdirs, files in os.walk(dir):
        for filename in files:
            path = os.path.join(dirname, filename)
            statbuf = os.stat(path)
            fileModified = statbuf.st_mtime
            if fileModified > lastModified:
                lastModified = fileModified
    return lastModified

def backup_world(world):
    # When was the folder system last modified?
    lastModified = get_dir_modified(world)
    
    # When was our last backup?
    logFile = None
    log = {}
    lastBackup = 0
    try:
        logFile = open(backupLog, 'r+')
        log = json.load(logFile)
        lastBackup = log[world]
    except IOError as e:
        lotFile = open(backupLog, 'w')
        print backupLog + " not found; assuming first run."
        logFile = open(backupLog, 'w')
    except KeyError as e:
        print world + " not found in log. Adding it."
    
    if lastModified > lastBackup:
        nowHuman = time.strftime("%Y-%m-%d_%H-%M-%S")
        nowUTC = time.time()
        zipName = world.split(os.sep)[-1] + '_' + nowHuman + '.zip'	
        print "Compressing " + zipName
        zip_dir(zipName, world)
        logFile.seek(0)
        log[world] = nowUTC
        json.dump(log, logFile)
        logFile.truncate()
        logFile.flush()
        logFile.close()
    else:
        dt = datetime.datetime.fromtimestamp(lastModified)
        iso_format = dt.isoformat()
        print world + ' has not been modified since ' + str(dt)
        
if __name__ == "__main__":
    for world in WORLDS:
        backup_world(world)
