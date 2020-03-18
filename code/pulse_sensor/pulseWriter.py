from pulsesensor2 import Pulsesensor
import time
import csv
import sys
import os


p = Pulsesensor()

print("hello1")

print("hello2")


startTime = time.time()

            

with open('/home/pi/WriterTest/heartRateCSV.csv', 'a', newline='') as f:
    
    theWriter = csv.writer(f)
    theWriter.writerow(['Time','BPM','col3'])    #column names  
    try:
        p.startAsyncBPM()
        while True:
            bpm = p.BPM
            print("hello")
            elapsedTime = time.time() - startTime
            theWriter.writerow([round(elapsedTime), round(bpm),'three'])   #cell values
            
            if bpm > 0:
                print("BPM: %d" % bpm)
                            
            else:
                print("No Heartbeat found")
            time.sleep(1)
                
            
    except:
        p.stopAsyncBPM()


      
                






