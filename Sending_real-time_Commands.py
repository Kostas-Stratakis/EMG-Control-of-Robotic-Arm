# In this Python code in line 230 change the parameters C and Gamma to the values found by the other Python code named "Finding_best_SVM_for_5gestures.py"
#This code trains the optimal SVM and then it Sends coommands in form of byte streams to the Lego NXT microprocessor so the the motors start and stop moving in real time.


import serial	
import time
import serial
import numpy as np
import sys
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
np.set_printoptions(threshold=sys.maxsize)
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn import preprocessing

#opening the ports to be ready for comms
#ser.__del__()
#serout.__del__()
serout=serial.Serial('COM3', 9600) #com3 bluetooth out for NXT
ser=serial.Serial('COM12', 9600) #com9 prolific

# session 1 loading data to variables lists
s1g0="C:/Users/ece73/Desktop/recordings/session1/gesture0.txt"
s1g1="C:/Users/ece73/Desktop/recordings/session1/gesture1.txt"
s1g2="C:/Users/ece73/Desktop/recordings/session1/gesture2.txt"
s1g3="C:/Users/ece73/Desktop/recordings/session1/gesture3.txt"
s1g4="C:/Users/ece73/Desktop/recordings/session1/gesture4.txt"
s1g5="C:/Users/ece73/Desktop/recordings/session1/gesture5.txt"
s1g6="C:/Users/ece73/Desktop/recordings/session1/gesture6.txt"
s1g7="C:/Users/ece73/Desktop/recordings/session1/gesture7.txt"
s1g8="C:/Users/ece73/Desktop/recordings/session1/gesture8.txt"

ds1g0 = np.loadtxt(s1g0, delimiter=",")
ds1g1 = np.loadtxt(s1g1, delimiter=",")
ds1g2 = np.loadtxt(s1g2, delimiter=",")
ds1g3 = np.loadtxt(s1g3, delimiter=",")
ds1g4 = np.loadtxt(s1g4, delimiter=",")
ds1g5 = np.loadtxt(s1g5, delimiter=",")
ds1g6 = np.loadtxt(s1g6, delimiter=",")
ds1g7 = np.loadtxt(s1g7, delimiter=",")
ds1g8 = np.loadtxt(s1g8, delimiter=",")
###################################################

# session 2 loading data to variables lists
s2g0="C:/Users/ece73/Desktop/recordings/session2/gesture0.txt"
s2g1="C:/Users/ece73/Desktop/recordings/session2/gesture1.txt"
s2g2="C:/Users/ece73/Desktop/recordings/session2/gesture2.txt"
s2g3="C:/Users/ece73/Desktop/recordings/session2/gesture3.txt"
s2g4="C:/Users/ece73/Desktop/recordings/session2/gesture4.txt"
s2g5="C:/Users/ece73/Desktop/recordings/session2/gesture5.txt"
s2g6="C:/Users/ece73/Desktop/recordings/session2/gesture6.txt"
s2g7="C:/Users/ece73/Desktop/recordings/session2/gesture7.txt"
s2g8="C:/Users/ece73/Desktop/recordings/session2/gesture8.txt"

ds2g0 = np.loadtxt(s2g0, delimiter=",")
ds2g1 = np.loadtxt(s2g1, delimiter=",")
ds2g2 = np.loadtxt(s2g2, delimiter=",")
ds2g3 = np.loadtxt(s2g3, delimiter=",")
ds2g4 = np.loadtxt(s2g4, delimiter=",")
ds2g5 = np.loadtxt(s2g5, delimiter=",")
ds2g6 = np.loadtxt(s2g6, delimiter=",")
ds2g7 = np.loadtxt(s2g7, delimiter=",")
ds2g8 = np.loadtxt(s2g8, delimiter=",")
##################################################################

# session 3 loading data to variables lists
s3g0="C:/Users/ece73/Desktop/recordings/session3/gesture0.txt"
s3g1="C:/Users/ece73/Desktop/recordings/session3/gesture1.txt"
s3g2="C:/Users/ece73/Desktop/recordings/session3/gesture2.txt"
s3g3="C:/Users/ece73/Desktop/recordings/session3/gesture3.txt"
s3g4="C:/Users/ece73/Desktop/recordings/session3/gesture4.txt"
s3g5="C:/Users/ece73/Desktop/recordings/session3/gesture5.txt"
s3g6="C:/Users/ece73/Desktop/recordings/session3/gesture6.txt"
s3g7="C:/Users/ece73/Desktop/recordings/session3/gesture7.txt"
s3g8="C:/Users/ece73/Desktop/recordings/session3/gesture8.txt"

ds3g0 = np.loadtxt(s3g0, delimiter=",")
ds3g1 = np.loadtxt(s3g1, delimiter=",")
ds3g2 = np.loadtxt(s3g2, delimiter=",")
ds3g3 = np.loadtxt(s3g3, delimiter=",")
ds3g4 = np.loadtxt(s3g4, delimiter=",")
ds3g5 = np.loadtxt(s3g5, delimiter=",")
ds3g6 = np.loadtxt(s3g6, delimiter=",")
ds3g7 = np.loadtxt(s3g7, delimiter=",")
ds3g8 = np.loadtxt(s3g8, delimiter=",")
##################################################################

# session 4 loading data to variables lists
s4g0="C:/Users/ece73/Desktop/recordings/session4/gesture0.txt"
s4g1="C:/Users/ece73/Desktop/recordings/session4/gesture1.txt"
s4g2="C:/Users/ece73/Desktop/recordings/session4/gesture2.txt"
s4g3="C:/Users/ece73/Desktop/recordings/session4/gesture3.txt"
s4g4="C:/Users/ece73/Desktop/recordings/session4/gesture4.txt"
s4g5="C:/Users/ece73/Desktop/recordings/session4/gesture5.txt"
s4g6="C:/Users/ece73/Desktop/recordings/session4/gesture6.txt"
s4g7="C:/Users/ece73/Desktop/recordings/session4/gesture7.txt"
s4g8="C:/Users/ece73/Desktop/recordings/session4/gesture8.txt"

ds4g0 = np.loadtxt(s4g0, delimiter=",")
ds4g1 = np.loadtxt(s4g1, delimiter=",")
ds4g2 = np.loadtxt(s4g2, delimiter=",")
ds4g3 = np.loadtxt(s4g3, delimiter=",")
ds4g4 = np.loadtxt(s4g4, delimiter=",")
ds4g5 = np.loadtxt(s4g5, delimiter=",")
ds4g6 = np.loadtxt(s4g6, delimiter=",")
ds4g7 = np.loadtxt(s4g7, delimiter=",")
ds4g8 = np.loadtxt(s4g8, delimiter=",")
##################################################################

# session 5 loading data to variables lists
s5g0="C:/Users/ece73/Desktop/recordings/session5/gesture0.txt"
s5g1="C:/Users/ece73/Desktop/recordings/session5/gesture1.txt"
s5g2="C:/Users/ece73/Desktop/recordings/session5/gesture2.txt"
s5g3="C:/Users/ece73/Desktop/recordings/session5/gesture3.txt"
s5g4="C:/Users/ece73/Desktop/recordings/session5/gesture4.txt"
s5g5="C:/Users/ece73/Desktop/recordings/session5/gesture5.txt"
s5g6="C:/Users/ece73/Desktop/recordings/session5/gesture6.txt"
s5g7="C:/Users/ece73/Desktop/recordings/session5/gesture7.txt"
s5g8="C:/Users/ece73/Desktop/recordings/session5/gesture8.txt"

ds5g0 = np.loadtxt(s5g0, delimiter=",")
ds5g1 = np.loadtxt(s5g1, delimiter=",")
ds5g2 = np.loadtxt(s5g2, delimiter=",")
ds5g3 = np.loadtxt(s5g3, delimiter=",")
ds5g4 = np.loadtxt(s5g4, delimiter=",")
ds5g5 = np.loadtxt(s5g5, delimiter=",")
ds5g6 = np.loadtxt(s5g6, delimiter=",")
ds5g7 = np.loadtxt(s5g7, delimiter=",")
ds5g8 = np.loadtxt(s5g8, delimiter=",")
##################################################################

# Creating y lists for the classification for every session and every gesture
#session 1 gestures y matrices
ys1g0=[0 for i in range(len(ds1g0))]
ys1g1=[1 for i in range(len(ds1g1))]
ys1g2=[2 for i in range(len(ds1g2))]
ys1g3=[3 for i in range(len(ds1g3))]
ys1g4=[4 for i in range(len(ds1g4))]
ys1g5=[5 for i in range(len(ds1g5))]
ys1g6=[6 for i in range(len(ds1g6))]
ys1g7=[7 for i in range(len(ds1g7))]
ys1g8=[8 for i in range(len(ds1g8))]

#session 2 gestures y matrices
ys2g0=[0 for i in range(len(ds2g0))]
ys2g1=[1 for i in range(len(ds2g1))]
ys2g2=[2 for i in range(len(ds2g2))]
ys2g3=[3 for i in range(len(ds2g3))]
ys2g4=[4 for i in range(len(ds2g4))]
ys2g5=[5 for i in range(len(ds2g5))]
ys2g6=[6 for i in range(len(ds2g6))]
ys2g7=[7 for i in range(len(ds2g7))]
ys2g8=[8 for i in range(len(ds2g8))]

#session 3 gestures y matrices
ys3g0=[0 for i in range(len(ds3g0))]
ys3g1=[1 for i in range(len(ds3g1))]
ys3g2=[2 for i in range(len(ds3g2))]
ys3g3=[3 for i in range(len(ds3g3))]
ys3g4=[4 for i in range(len(ds3g4))]
ys3g5=[5 for i in range(len(ds3g5))]
ys3g6=[6 for i in range(len(ds3g6))]
ys3g7=[7 for i in range(len(ds3g7))]
ys3g8=[8 for i in range(len(ds3g8))]

#session 4 gestures y matrices
ys4g0=[0 for i in range(len(ds4g0))]
ys4g1=[1 for i in range(len(ds4g1))]
ys4g2=[2 for i in range(len(ds4g2))]
ys4g3=[3 for i in range(len(ds4g3))]
ys4g4=[4 for i in range(len(ds4g4))]
ys4g5=[5 for i in range(len(ds4g5))]
ys4g6=[6 for i in range(len(ds4g6))]
ys4g7=[7 for i in range(len(ds4g7))]
ys4g8=[8 for i in range(len(ds4g8))]

#session 5 gestures y matrices
ys5g0=[0 for i in range(len(ds5g0))]
ys5g1=[1 for i in range(len(ds5g1))]
ys5g2=[2 for i in range(len(ds5g2))]
ys5g3=[3 for i in range(len(ds5g3))]
ys5g4=[4 for i in range(len(ds5g4))]
ys5g5=[5 for i in range(len(ds5g5))]
ys5g6=[6 for i in range(len(ds5g6))]
ys5g7=[7 for i in range(len(ds5g7))]
ys5g8=[8 for i in range(len(ds5g8))]

#creating a complete dataset with y matrices for every session. 
#session 1
ds1=np.concatenate((ds1g0,ds1g3,ds1g4,ds1g6,ds1g8))
ys1=np.concatenate((ys1g0,ys1g3,ys1g4,ys1g6,ys1g8))

#session 2
ds2=np.concatenate((ds2g0,ds2g3,ds2g4,ds2g6,ds2g8))
ys2=np.concatenate((ys2g0,ys2g3,ys2g4,ys2g6,ys2g8))

#session 3
ds3=np.concatenate((ds3g0,ds3g3,ds3g4,ds3g6,ds3g8))
ys3=np.concatenate((ys3g0,ys3g3,ys3g4,ys3g6,ys3g8))

#session 4
ds4=np.concatenate((ds4g0,ds4g3,ds4g4,ds4g6,ds4g8))
ys4=np.concatenate((ys4g0,ys4g3,ys4g4,ys4g6,ys4g8))

#session 5
ds5=np.concatenate((ds5g0,ds5g3,ds5g4,ds5g6,ds5g8))
ys5=np.concatenate((ys5g0,ys5g3,ys5g4,ys5g6,ys5g8))

#Creating the input for SVM. Complete data (x matrix) and y matrices.
datall=np.concatenate((ds1,ds2,ds3,ds4,ds5))
ysall=np.concatenate((ys1,ys2,ys3,ys4,ys5))

data=datall
y=ysall

#splitting training and testng set randomly


#scaling the data sets 
X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2, random_state=0)
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_transformed = scaler.transform(X_train)
X_test_transformed = scaler.transform(X_test)

#SVM model traing and and testing the test set on it printing the results 
#care for the parameters they are taken from previous recordings
model = SVC(kernel='rbf', C=512,gamma=0.125,decision_function_shape='ovr')
model.fit(X_train_transformed,y_train)
y_true, y_pred = y_test, model.predict(X_test_transformed)
print(classification_report(y_true, y_pred))
print('model trained')


#reading rms vectors from microprocessors and deciding what the Nxt will do
#5th byte is the motor
#start motor on port A, 0x0D, 0x00, 0x80, 0x04, 0x00, 0x64, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00
#start motor on port B, 0x0D, 0x00, 0x80, 0x04, 0x01, 0x64, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00
#start motor on port C, 0x0D, 0x00, 0x80, 0x04, 0x02, 0x64, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00
#Stop  motor on port A, 0x0C, 0x00, 0x00, 0x04, 0x00, 0x00, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00
#Stop  motor on port B, 0x0C, 0x00, 0x00, 0x04, 0x01, 0x00, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00
#Stop  motor on port C, 0x0C, 0x00, 0x00, 0x04, 0x02, 0x00, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00
#6th byte 0x64 for 50% power for anticlockwise direction and 0xCD for clockwise

while True:
 x = ser.readline()                                #reading a series of bytes
 g=x.decode("ascii")                               #decoding the byte to string
 g = np.fromstring( g, dtype=np.float, sep=',' )  #changing the string to an array of floats
 g=np.reshape(g,(1,-1))                                 #reshaping to 2d array 
 print(g)
 g_transformed=scaler.transform(g)                #normalizing vector with params from training set
 y_predg=model.predict(g_transformed)              #predicting which gesture this is
 print(y_predg)                                    #printing prediction for me to know
 
 #If gesture0 detected stop all motor movements
 if y_predg==0:
    #stop port A
     packet = bytearray([ 0x0C, 0x00, 0x00, 0x04, 0x00, 0x00, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)
     #stop port B
     packet = bytearray([ 0x0C, 0x00, 0x00, 0x04, 0x01, 0x00, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)
     #stop port C
     packet = bytearray([ 0x0C, 0x00, 0x00, 0x04, 0x02, 0x00, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)
 #if gesture 3 detected open hand
 if   y_predg==3:
      #start port A anticlockwise
     packet = bytearray([  0x0D, 0x00, 0x80, 0x04, 0x00, 0x32, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)
     #stop port B
     packet = bytearray([ 0x0C, 0x00, 0x00, 0x04, 0x01, 0x00, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)
  #if gesture 4 detected close hand
 if   y_predg==4:
      #start port A anticlockwise
     packet = bytearray([  0x0D, 0x00, 0x80, 0x04, 0x00, 0xCD, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)
     #stop port B
     packet = bytearray([ 0x0C, 0x00, 0x00, 0x04, 0x01, 0x00, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)
  #if gesture 6 detected go up   
 if   y_predg==6:
      #start port B clockwise
     packet = bytearray([  0x0D, 0x00, 0x80, 0x04, 0x01, 0x32, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)
     #stop port A
     packet = bytearray([ 0x0C, 0x00, 0x00, 0x04, 0x00, 0x00, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)
   #if gesture 8 detected go down 
 if   y_predg==8:
      #start port B anticlockwise
     packet = bytearray([  0x0D, 0x00, 0x80, 0x04, 0x01, 0xCD, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)
     #stop port A
     packet = bytearray([ 0x0C, 0x00, 0x00, 0x04, 0x00, 0x00, 0x07, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00])
     serout.write(packet)

