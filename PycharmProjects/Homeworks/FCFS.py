import matplotlib.pyplot as plt
from numpy.random import seed
from numpy.random import randint


# this function fill BurstTime list with random number between 1 ,10
def fillBurstTimeRandomly(BurstTime):
    # seed(1)
    for _ in range(10):
        BurstTime.append(randint(1,10))
        # print (BurstTime[i])
    print ("Burst Time is :" )
    print(BurstTime)
    print ("BurstTime length is :%d" % len(BurstTime))
    # calculateArrivalTime(BurstTime=BurstTime)

# this function calculate Arrival time for each process where ArrivalTime list has one value (0) which represent arrival time for first process
def calculateArrivalTime(BurstTime):
    for i in range(len(ArrivalTime),len(BurstTime)):
        # print BurstTime[i]
        ArrivalTime.append(ArrivalTime[i-1]+BurstTime[i-1])
    print ("Arrival Time is :")
    print(ArrivalTime)
    print ("ArrivalTime length is: %d"% len(ArrivalTime))
    # calculateAWT(ArrivalTime)

# this function calculate AWT
def calculateAWT(ArrivalTime):
    AWT = 0
    for i in range(len(ArrivalTime)):
        AWT = AWT+ArrivalTime[i]
    print ("total WT is : %d" %AWT)
    AWT = AWT/len(ArrivalTime)
    print ("AWT is : %d" %AWT)

    return AWT


BurstTime = []
ArrivalTime = [0]
AWTPoints = [0]

for i in range(10):
    print ("_________________________________")
    fillBurstTimeRandomly(BurstTime=BurstTime)
    calculateArrivalTime(BurstTime=BurstTime)
    AWTPoints.append(calculateAWT(ArrivalTime))
    # AWTPoints.append(fillBurstTimeRandomly(BurstTime=BurstTime))
print AWTPoints
plt.plot([1,10,20,30,40,50,60,70,80,90,100],AWTPoints)
plt.plot([1,10,20,30,40,50,60,70,80,90,100],AWTPoints,'ro')
plt.xlabel("number of process")
plt.ylabel("Avrage waiting time (AWT)")
plt.show()
