import os
import subprocess
from datetime import datetime
import re
import time
import csv

# for naming the file on script start
now = datetime.now()
startTime = now.strftime("%m%d%Y")
count = 0 # number of pings 
average = 0
sum = 0

# run until ctrl-c lul
while True:
    # make the ping and save the output
    output = subprocess.check_output('ping www.google.com -c 1; echo $?', shell=True).decode('utf-8').strip().split('\n')
    #print(output)
    count += 1
    # get date and time to string
    now = datetime.now()
    date_now = now.strftime('%m/%d/%Y')
    time_now = now.strftime('%H:%M:%S')

    # check if ping didn't exit with an error
    if(int(output[len(output)-1]) == 0):
        # find the time=xx.xxx ms pattern in the output
        ping = re.search('time=(.*)ms', output[1])
        #(ping)
        if ping:
            pingTime = ping.group(1)
            sum+=float(pingTime)
            average=sum/count
    else:
        pingTime = 'error/timedout'
    
    # write data to file
    toWrite = [date_now, time_now, str(count), pingTime]
    #print(toWrite)
    with open(startTime+'_ping.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(toWrite)
    
    print('last: '+pingTime+'   Updated Average: '+str(average))
    # wait 
    time.sleep(1)


   