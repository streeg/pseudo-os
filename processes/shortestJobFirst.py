# -*- coding: utf-8 -*-
class shortestJobFist:

    def processData(self, listOfNumbers):

        #takes only the first element of each tuple
        n = 0
        arrivalTimeList = [x[n] for x in listOfNumbers]
        #takes only the second element of each tuple
        n = 1
        burstTimeList = [x[n] for x in listOfNumbers]

        processData = []
        for i in range(len(listOfNumbers)):
            temporary = []
            processId = i
            arrivalTime = arrivalTimeList[i]
            burstTime = burstTimeList[i]
            #'0' is the state of the process. 0 means not executed and 1 means execution complete
            temporary.extend([processId, arrivalTime, burstTime, 0]) 
            processData.append(temporary)
        shortestJobFist.schedulingProcess(self, processData)

    def schedulingProcess(self, processData):
        startTime = []
        exitTime = []
        sTime = 0
        processData.sort(key=lambda x: x[1])
        #Sort process according to the Arrival time
        for i in range(len(processData)):
            readyQueue = []
            temp = []
            normalQueue = []

            for j in range(len(processData)):
                if (processData[j][1] <= sTime) and (processData[j][3] == 0):
                    temp.extend([processData[j][0], processData[j][1], processData[j][2]])
                    readyQueue.append(temp)
                    temp = []
                elif processData[j][3] == 0:
                    temp.extend([processData[j][0], processData[j][1], processData[j][2]])
                    normalQueue.append(temp)
                    temp = []

            if len(readyQueue) != 0:
                readyQueue.sort(key=lambda x: x[2])
                #Sort the processes according to the Burst Time
                startTime.append(sTime)
                sTime = sTime + readyQueue[0][2]
                eTime = sTime
                exitTime.append(eTime)
                for k in range(len(processData)):
                    if processData[k][0] == readyQueue[0][0]:
                        break
                processData[k][3] = 1
                processData[k].append(eTime)

            elif len(readyQueue) == 0:
                if sTime < normalQueue[0][1]:
                    sTime = normalQueue[0][1]
                startTime.append(sTime)
                sTime = sTime + normalQueue[0][2]
                eTime = sTime
                exitTime.append(eTime)
                for k in range(len(processData)):
                    if processData[k][0] == normalQueue[0][0]:
                        break
                processData[k][3] = 1
                processData[k].append(eTime)

        tTime = shortestJobFist.calculateTurnaroundTime(self, processData)
        wTime = shortestTime = shortestJobFist.calculateWaitingTime(self, processData)
        rTime = shortestJobFist.calculateResponseTime(self, processData)
        shortestTime = shortestJobFist.printData(self, processData, tTime, wTime, rTime)
        print()
        print()
        print()
        shortestJobFist.printDataVerbose(self, processData)

    def calculateTurnaroundTime(self, processData):
        totalTurnaoundTime = 0
        for i in range(len(processData)):
            turnaroundTime = processData[i][4] - processData[i][1]
            totalTurnaoundTime = totalTurnaoundTime + turnaroundTime
            processData[i].append(turnaroundTime)
        averageTurnaroundtime = totalTurnaoundTime / len(processData)
        return averageTurnaroundtime


    def calculateWaitingTime(self, processData):
        totalWaitingTime = 0
        for i in range(len(processData)):
            waitingTime = processData[i][5] - processData[i][2]
            totalWaitingTime = totalWaitingTime + waitingTime
            processData[i].append(waitingTime)
        averageWaitingTime = totalWaitingTime / len(processData)
        return averageWaitingTime


    def calculateResponseTime(self, processData):
        totalResponseTime = 0
        for i in range(len(processData)):
            responseTime = processData[i][5] - processData[i][2]
            totalResponseTime = totalResponseTime + responseTime
            processData[i].append(responseTime)
        averageResponseTime = totalResponseTime / len(processData)
        return averageResponseTime


    def printData(self, processData, averageTurnaroundTime, averageWaitingTime, averageResponseTime):
        print(f'Average Turnaround Time: {averageTurnaroundTime}')
        print(f'Average Waiting Time: {averageWaitingTime}')
        print(f'Average Response Time: {averageResponseTime}')
    
    def printDataVerbose(self, processData):
        processData.sort(key=lambda x: x[4])
        print("shortestJobFist:")
        for i in range(len(processData)):

            print("Running process", end = " [") 
            print(processData[i][0], end = "] ")
            print("from", end = " [") 
            if(i != 0):
                print(processData[i-1][4], end = "] ")
            else:
                print("0", end = "] ")
            print("to", end = " [") 
            print(processData[i][4], end = "]\n")            