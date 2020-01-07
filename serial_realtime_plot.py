import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
 
A= []
B=[]
C=[]

arduinoData = serial.Serial('COM4',115200) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0
 
def makeFig(): #Create a function that makes our desired plot
    plt.ylim(0,1024)                                 #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Data 1')                            #Set ylabels
    plt.plot(B, 'ro-', label='Data 1')       #plot the A
    plt.legend(loc='upper left')                    #plot the legend
    plt2=plt.twinx()                                #Create a second y axis
    plt.ylim(0,1024)                           #Set limits of second y axis- adjust to readings you are getting
    plt2.plot(C, 'b^-', label='Data 2') #plot C data
    plt2.set_ylabel('Data 2)')                    #label second y axis
    plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                  #plot the legend
    

while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    arduinoString = arduinoData.readline().decode().strip() #read the line of text from the serial port
    dataArray = arduinoString.split(',')   #Split it into an array called dataArray
    A = float(dataArray[0])            #Convert first element to floating number and put in A
    p = float(dataArray[1])            #Convert second element to floating number and put in P
    #print(A,",",p)
    B.append(A)                     #Build our B array by appending A readings
    C.append(p)                     #Building our pressure array by appending P readings
    #print (B)
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.0000000000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>512):                            #If you have 50 or more points, delete the first one from the array
        B.pop(0)                       #This allows us to just see the last 50 data points
        C.pop(0)
   

