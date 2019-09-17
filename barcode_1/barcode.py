import datetime
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17 , GPIO.OUT)
GPIO.setup(27 , GPIO.IN)
GPIO.setup(22 , GPIO.OUT)

status = 0

while True:
    senser = GPIO.input(17)
    f = open('data.txt', 'a')
    barcode_input = input("Barcode : ")

    if barcode_input != "":
        read_product = open('product.txt', 'r')
        while True:
            product = read_product.readline()
            product_data = product.rstrip().split(',')
            #print(product_data)
            if product == "": 
                break

            elif product_data[0] == barcode_input:
                datenow = datetime.datetime.now()
                time = str(datenow.hour) + ":" + str(datenow.minute) + ":" + str(datenow.second)
                date = str(datenow.day) + "/" + str(datenow.month) + "/" + str(datenow.year)
                f.write(barcode_input + "  " + str(product_data[1]) + "  " + time + "  " + date + "\n")
                status = 1    
            
    if status == 1:
        print("success")
        GPIO.output(17 , GPIO.LOW)	
	    time.sleep(10)	
        GPIO.output(17 , GPIO.HIGH)

        if senser == False:
            GPIO.output(22 , GPIO.LOW)	
	        time.sleep(10)	
            GPIO.output(22 , GPIO.HIGH)
    else:
        print("no data")
    status = 0

    if(barcode_input == "e"):
        f.close()
        break
