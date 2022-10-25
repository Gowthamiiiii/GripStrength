import cv2
import numpy
import time
import csv
import datetime
#import supervisor

webcam = 1
start = 0
cam = cv2.VideoCapture(0)
new_current_date = []
cd = []
filename = 'images1/blue_0_top.csv'
#referenceTime = round(time.time())
startTime = time.time()
print(startTime)
#print(time.monotonic())
def current_milli_time():
    return round(time.time() * 1000)
milli = current_milli_time()
def _format_datetime(datetime):
        return "{:02}/{:02}/{} {:02}:{:02}:{:02}".format(datetime.tm_mon,datetime.tm_mday,datetime.tm_year,datetime.tm_hour,datetime.tm_min,datetime.tm_sec,)
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['reference_timestamp', 'filename'])
    for x in range(10):
        #print(x)
        result,image = cam.read()
        #print(result)
        if result:
            #cv2.imshow("image", image)
            #print(x)
            #incrementTime = round(time.monotonic()-startTime,1)
            #currentTime = referenceTime + incrementTime
            #Time = datetime.datetime.now()
            #print(time.time())
            unix_time = 1665942864 # Wed Aug 17 2022 19:36:10 GMT+0000  # NY Timezone
            get_timestamp = int(unix_time )
            current_unix_time = time.localtime(get_timestamp)
            current_struct_time = time.struct_time(current_unix_time)
            current_date = "{}".format(_format_datetime(current_struct_time))
            #print("Timestamp:", current_date)
            new_current_date = current_date.split(' ')
            cd = new_current_date[1].split(':')
            s = ""
            for i in cd:
                s = s + str(i)
            current_date = int(s)
            start = start + 1
            incrementTime = time.time()-startTime
            currentTime = current_date + start
            #print(incrementTime)
            csvwriter.writerow([time.monotonic(), currentTime])
            fileName = "images1/Lighting_Condition2_images/pink_65_side/{0:.1f}.png".format(currentTime)
            cv2.imwrite(fileName, image)
            #print(Time)
            time.sleep(0.1)

cv2.waitKey(0)
#cv2.destroyAllWindows("image")

