#........................................................IMPORT LIBRARIES..................................................

import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
import math
import pylab
import scipy.fftpack
import scipy
import csv
import sys

#........................................................CONFIGURATIONS...................................................  
A=[]   # real time x axis data
B=[]   # x axis data matrix storage
B1=[]
C=[]   # real time y axis data
D=[]   # y axis data matrix storage
D1=[]
All=[] # all raw data
A1=[]
dataArray=[]
n=4096  # no of points take
N=4096  # data reading end end point
i=0;
j=0;
Fs=1000 # sampling rate
cnt=0

arduinoData = serial.Serial('COM4',2000000) #Creating our serial object named arduinoData
#plt.ion() #Tell matplotlib you want interactive mode to plot live data

'''
def makeFig(): #Create a function that makes our desired plot
    plt.ylim(-2,2)                                 #Set y min and max values
    plt.title('My Live Streaming accerlaration Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('X axis (g)')                            #Set ylabels
    plt.plot(B, 'ro-', label='X axis')       #plot the A
    plt.legend(loc='upper left')                    #plot the legend
    plt2=plt.twinx()                                #Create a second y axis
    plt.ylim(-2,2)                           #Set limits of second y axis- adjust to readings you are getting
    plt2.plot(D, 'b^-', label='Y axis') #plot C data
    plt2.set_ylabel('Y axis (g)')                    #label second y axis
    plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                  #plot the legend
   
'''
for s in range(n): # While loop that loops forever
    arduinoString = arduinoData.readline(16).decode().strip('\r\n') #read the line of text from the serial port
    All.append(arduinoString.split(',') ) #Split it into an array called dataArray
    
    #All.append(dataArray)
    #print (dataArray)
    #B.append(dataArray[1])
    #print (float.dataArray[0])
    #print (B)
    #drawnow(makeFig)                       #Call drawnow to update our live graph
    #plt.pause(.0000000000001)                     #Pause Briefly. Important to keep drawnow from crashing
    '''cnt=cnt+1
    #print (AA)
    if(cnt>n):                            #If you have 50 or more points, delete the first one from the array
        B.pop(0)                       #This allows us to just see the last 50 data points
        C.pop(0)
        '''
##    if s == N:
##        break
#A1=float(dataArray[9][1])
print ("data reading complete ")
#print (All)

for j in range (n):
    #print(float(All[j][0]))
    A=float(All[j][0])
    #print (math.pow(A,2))
    B.append(A)
    #print (B)
    C=float(All[j][1])
    D.append(C)
    #if j == 9:
    #    break
#print (B)
#plt.figure()
#plt.plot (B)
#plt.show()
#B=numpy.transpose(B1) #matrix transpose
#D=numpy.transpose(D1)
#print (B)
#E=math.pow(B,2)
#print (B)
#plt.plot(B1)
#for i in range (n):
#print (All[1])
  # B.append(All[i][0])
    #print (A)   

#...............................................END OF REAL TIME DATA ANALYSIS .....................   
#print(B)
plt.figure() # to get new figure
plt.title('Accerlaration Data of X axis 20cm_7')
plt.ylabel('X axis Accerlaration (g+25)')
plt.xlabel('n')
plt.plot(B)  # plot B data array
plt.savefig('Accerlaration Data of X axis 20cm_7.png', format="png")
#plt.show()
plt.figure()
plt.title('Accerlaration Data of Z axis 20cm_7')
plt.ylabel('Z axis Accerlaration (g+25)')
plt.xlabel('n')
plt.plot(D)   # plot C data array
plt.savefig('Accerlaration Data of Z axis 20cm_7.png', format="png")
#plt.show()



#.................................................. SAVE TEXT FILE .....................................
numpy.savetxt('X axis data for steel 20cm_7.txt', B, fmt='%1.5f') # X axis data to txt file
numpy.savetxt('Z axis data for steel 20cm_7.txt', D, fmt='%1.5f') # Y axis data to txt file

numpy.savetxt('X axis data for steel 20cm_7.csv', B, fmt='%1.5f') # X axis data to csv file
numpy.savetxt('Z axis data for steel 20cm_7.csv', D, fmt='%1.5f') # Y axis data to csv file


#............................................... FREQUENCY DOMAIN ANALYSIS...........................
Ftx = scipy.fft(B)
Fty = scipy.fft(D)
#Ft_x = Ftx[1:n/2+1]
#Ft_y = Fty[1:n/2+1]
Ft_x = Ftx[1:n//2+1]
Ft_y = Fty[1:n//2+1]
#print ("X axis",abs(Ft_x))
#print ("Y axis",abs(Ft_y))

f = numpy.linspace(1, 1.0*Fs/2.0-1, n//2)
plt.figure()
plt.title('Frequency domain Accerlaration Data of X axis 20cm_7')
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hz)')
markerline, stemlines, baseline = plt.stem(f,abs(Ft_x),'-.') # Frequency domain stem plot of X axis
plt.savefig('Frequency domain Accerlaration Data of X axis 20cm_7.png', format="png")
#plt.show()
plt.figure(4)
plt.title('Frequency domain Accerlaration Data of Z axis 20cm_7')
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hz)')
markerline, stemlines, baseline = plt.stem(f,abs(Ft_y),'-.') # Frequency domain stem plot of y axis
plt.savefig('Frequency domain Accerlaration Data of Z axis 20cm_7.png', format="png")
plt.show()
#print (f)



 


