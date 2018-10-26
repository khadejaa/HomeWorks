
import matplotlib.pyplot as plt
from numpy.random import randint
from numpy.random import seed
import matplotlib.pyplot as plt


BurstTime = []
ArrivalTime = []
AWTPoints = [0]


#Function to fill Burst Time and its ArrivalTime randomaly
#Assume process take Burst Time between 1 to 10
#Assume ArrivalTime is between 1 to 10 and first process has t=0 (to ensure there are at leaset one process has t=0)

def fillBurstTimeRandomly(BurstTime,ArrivalTime):
    seed(1)
    for i in range(10):
        BurstTime.insert(i ,randint(1,10))
    for i in range(10):
        if i==0:
            ArrivalTime.insert(0,0)
        else:
            ArrivalTime.insert(i , randint(0,len(BurstTime)))

    print "BurstTime before sorting by ArrivalTime"
    printTable(BurstTime, ArrivalTime)
    print "number of process is :%d" % len(BurstTime)

# Function that sort Burst Time by its ArrivalTime
def sorting (BurstTime , ArrivalTime):
    swap = 0
    for i in range(0,len(ArrivalTime)-1):
        for j in range(0,len(ArrivalTime)-i-1):
                if ArrivalTime[j] > ArrivalTime[j+1]:
                    swap = ArrivalTime[j]
                    ArrivalTime[j] = ArrivalTime[j + 1]
                    ArrivalTime[j + 1] = swap

                    swap = BurstTime[j]
                    BurstTime[j] = BurstTime[j + 1]
                    BurstTime[j + 1] = swap

    print
    print "BurstTime after sorting by ArrivalTime"
    printTable(BurstTime,ArrivalTime)

def printTable (BurstTime , ArrivalTime):
    print ("(burst time , arrival time)")
    for T in zip(BurstTime,ArrivalTime):
        print T


#function that calculate average waiting time depend on its arrival time
def calculateAWT(BurstTime , ArrivalTime):
    waitingTime = float(0)
    totalTime= float( ArrivalTime[0])
    for i in range(len(BurstTime)-1):
        totalTime += BurstTime[i]
        waitingTime += totalTime - ArrivalTime[i+1]
    print totalTime
    print waitingTime
    AWT = float(waitingTime/len(BurstTime))  # type: float
    print ("AWT is : %f" % float(AWT))

    return AWT


for i in range(10):
    print ("_________________________________")
    fillBurstTimeRandomly(BurstTime,ArrivalTime)
    sorting(BurstTime, ArrivalTime)
    AWTPoints.append(calculateAWT(BurstTime,ArrivalTime))
print AWTPoints

plt.plot([0,10,20,30,40,50,60,70,80,90,100],AWTPoints)
plt.plot([0,10,20,30,40,50,60,70,80,90,100],AWTPoints,'ro')
plt.xlabel("number of process")
plt.ylabel("Avrage waiting time (AWT)")
plt.show()