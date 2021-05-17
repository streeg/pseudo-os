# -*- coding: utf-8 -*-

class RoundRobin:

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
            temporary.extend([processId, arrivalTime, burstTime, 0, burstTime]) 
            processData.append(temporary)
        quantum = 2.0
        RoundRobin.schedulingProcess(self, processData, quantum)

    def schedulingProcess(self, processData, quantum):
        startTime = []
        exitTime = []
        executedProcess = []
        readyQueue = []
        sTime = 0
        processData.sort(key=lambda x: x[1])
        #Sort processes according to the Arrival Time
        while 1:
            normalQueue = []
            temp = []
            for i in range(len(processData)):
                if processData[i][1] <= sTime and processData[i][3] == 0:
                    present = 0
                    if len(readyQueue) != 0:
                        for k in range(len(readyQueue)):
                            if processData[i][0] == readyQueue[k][0]:
                                present = 1
                    #The above if loop checks that the next process is not a part of readyQueue
                    if present == 0:
                        temp.extend([processData[i][0], processData[i][1], processData[i][2], processData[i][4]])
                        readyQueue.append(temp)
                        temp = []
                    #The above if loop adds a process to the readyQueue only if it is not already present in it
                    if len(readyQueue) != 0 and len(executedProcess) != 0:
                        for k in range(len(readyQueue)):
                            if readyQueue[k][0] == executedProcess[len(executedProcess) - 1]:
                                readyQueue.insert((len(readyQueue) - 1), readyQueue.pop(k))
                    #The above if loop makes sure that the recently executed process is appended at the end of readyQueue
                elif processData[i][3] == 0:
                    temp.extend([processData[i][0], processData[i][1], processData[i][2], processData[i][4]])
                    normalQueue.append(temp)
                    temp = []
            if len(readyQueue) == 0 and len(normalQueue) == 0:
                break
            if len(readyQueue) != 0:
                if readyQueue[0][2] > quantum:
                    #If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    startTime.append(sTime)
                    sTime = sTime + quantum
                    eTime = sTime
                    exitTime.append(eTime)
                    executedProcess.append(readyQueue[0][0])
                    for j in range(len(processData)):
                        if processData[j][0] == readyQueue[0][0]:
                            break
                    processData[j][2] = processData[j][2] - quantum
                    readyQueue.pop(0)
                elif readyQueue[0][2] <= quantum:
                    #If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    startTime.append(sTime)
                    sTime = sTime + readyQueue[0][2]
                    eTime = sTime
                    exitTime.append(eTime)
                    executedProcess.append(readyQueue[0][0])
                    for j in range(len(processData)):
                        if processData[j][0] == readyQueue[0][0]:
                            break
                    processData[j][2] = 0
                    processData[j][3] = 1
                    processData[j].append(eTime)
                    readyQueue.pop(0)
            elif len(readyQueue) == 0:
                if sTime < normalQueue[0][1]:
                    sTime = normalQueue[0][1]
                if normalQueue[0][2] > quantum:
                    #If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    startTime.append(sTime)
                    sTime = sTime + quantum
                    eTime = sTime
                    exitTime.append(eTime)
                    executedProcess.append(normalQueue[0][0])
                    for j in range(len(processData)):
                        if processData[j][0] == normalQueue[0][0]:
                            break
                    processData[j][2] = processData[j][2] - quantum
                elif normalQueue[0][2] <= quantum:
                    #If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    startTime.append(sTime)
                    sTime = sTime + normalQueue[0][2]
                    eTime = sTime
                    exitTime.append(eTime)
                    executedProcess.append(normalQueue[0][0])
                    for j in range(len(processData)):
                        if processData[j][0] == normalQueue[0][0]:
                            break
                    processData[j][2] = 0
                    processData[j][3] = 1
                    processData[j].append(eTime)
        tTime = RoundRobin.calculateTurnaroundTime(self, processData)
        wTime = RoundRobin.calculateWaitingTime(self, processData)
        RoundRobin.printData(self, processData, tTime, wTime, quantum)
        print()
        print()
        print()
        RoundRobin.printDataVerbose(self, executedProcess, quantum)

    def calculateTurnaroundTime(self, processData):
        totalTurnaroundTime = 0
        for i in range(len(processData)):
            turnaroundTime = processData[i][5] - processData[i][1]
            totalTurnaroundTime = totalTurnaroundTime + turnaroundTime
            processData[i].append(turnaroundTime)
        averageTurnaroundTime = totalTurnaroundTime / len(processData)
        return averageTurnaroundTime

    def calculateWaitingTime(self, processData):
        totalWaitingTime = 0
        for i in range(len(processData)):
            waitingTime = processData[i][6] - processData[i][4]
            totalWaitingTime = totalWaitingTime + waitingTime
            processData[i].append(waitingTime)
        averageWaitingTime = totalWaitingTime / len(processData)
        return averageWaitingTime

    def printData(self, processData, averageTurnaroundTime, averageWaitingTime, quantum):
        processData.sort(key=lambda x: x[0])
        print(f'Average Turnaround Time: {averageTurnaroundTime}')
        print(f'Average Response Time: {quantum}')
        print(f'Average Waiting Time: {averageWaitingTime}')
    
    def printDataVerbose(self, executedProcess, quantum):
        quantumAmount = 0
        print("RR:")
        for i in range(len(executedProcess)):
            print("Running process", end = " [") 
            print(executedProcess[i], end = "] ")
            print("from", end = " [") 
            if(i != 0):
                print(quantumAmount, end = "] ")
            else:
                print("0", end = "] ")
            print("to", end = " [") 
            quantumAmount = quantumAmount + int(quantum)
            print(quantumAmount, end = "]\n")    