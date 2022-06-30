import os
import sys
import time
import shutil
import subprocess


def loadTests():
    print("Loading tests and test data")
    TASK_DIR = "/tmp/task"

    if not os.path.exists(TASK_DIR):
        print("Creating task folder in /tmp")
        os.makedirs(TASK_DIR)
        print("Copying test files to /tmp/task")
        os.system('cp -r /var/task /tmp')
        print("Deleting previous screenshots")
        os.system('find /tmp/results/* -type f -not -name "*.py"-delete')
        os.makedirs("/tmp/results")
    else:
        print("task folder already exists in /tmp")


def loadBrowser(browser_driver):
    try:
        print("Loading browser and browser driver")
        BIN_DIR = "/tmp/bin"
        CURR_BIN_DIR = "/opt"

        if not os.path.exists(BIN_DIR):
            print("Creating bin folder in /tmp")
            os.makedirs(BIN_DIR)
        else:
            print("bin folder already exists in /tmp")

        for i in browser_driver:
            if (i not in (os.listdir('/tmp/bin'))):
                print("Copying " + i + " in /tmp/bin")
                currfile = os.path.join(CURR_BIN_DIR, i)
                newfile = os.path.join(BIN_DIR, i)
                shutil.copy2(currfile, newfile)

                print("Giving permissions for lambda")
                os.chmod(newfile, 0o775)

            else:
                print(i + " already present in /tmp/bin")

    except Exception as e:
        exeMsg = type(e).__name__ + " : " + str(e)
        print(e)
        print(exeMsg)
        raise e