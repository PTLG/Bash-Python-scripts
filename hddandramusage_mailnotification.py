import os
import time
import subprocess

"""
Following scripts generates the mail message to mutt mail client with ram and hdd usage for given time.
This script could be connected, for example, to the cyclic cron job, or executed if nneded from cli.
"""


summaryraport=open("/home/PTLG/scripts/summaryraport.txt", "w")
hdd = subprocess.check_output('df -h', shell=True)
summaryraport.write(str(hdd))
summaryraport.write("\n")

ram = subprocess.check_output('free -h', shell=True)
summaryraport.write(str(ram))
summaryraport.write("\n")

summaryraport.close()

os.system("mutt -s 'hhd and ram usage sumamry for "+str(time.asctime())+"' sample@email.com < /home/user/scripts/summaryraport.txt")



