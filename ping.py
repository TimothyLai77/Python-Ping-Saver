import os
import subprocess
from datetime import datetime
import re
import time
import csv

# for naming the file on script start
now = datetime.now()
startTime = now.strftime("%m%d%Y_%H%M")
count = 0 # number of pings 

# run until ctrl-c lul
while True:
    # make the ping and save the output
    output = subprocess.check_output('ping www.google.com -c 1', shell=True).decode('utf-8').strip().split('\n')
    count+=1

    # get date and time to string
    now = datetime.now()
    date_now = now.strftime('%m/%d/%Y')
    time_now = now.strftime('%H:%M:%S')

    # find the time=xx.xxx ms pattern in the output
    ping = re.search('time=(.*)ms', output[1])
    if ping:
        pingTime = ping.group(1)
    else:
        pingTime = 'timedout'
   
    # write data to file
    toWrite = [date_now, time_now, str(count), pingTime]
    with open(startTime+'_ping.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(toWrite)

    # wait 
    time.sleep(1)


   