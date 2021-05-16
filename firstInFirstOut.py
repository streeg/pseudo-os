# -*- coding: utf-8 -*-
class firstInFirstOut:

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
            temporary.extend([processId, arrivalTime, burstTime])
            processData.append(temporary)
        firstInFirstOut.schedulingProcess(self, processData)

    def schedulingProcess(self, processData):
        processData.sort(key=lambda x: x[1])
        startTime = []
        exitTime = []
        sTime = 0
        for i in range(len(processData)):
            if sTime < processData[i][1]:
                sTime = processData[i][1]
            startTime.append(sTime)
            sTime = sTime + processData[i][2]
            eTime = sTime
            exitTime.append(eTime)
            processData[i].append(eTime)
        tTime = firstInFirstOut.calculateTurnaroundTime(self, processData)
        wTime = firstInFirstOut.calculateWaitingTime(self, processData)
        rTime = firstInFirstOut.calculateResponseTime(self, processData)
        firstInFirstOut.printData(self, processData, tTime, wTime, rTime)

    def calculateTurnaroundTime(self, processData):
        totalTurnaroundTime = 0
        for i in range(len(processData)):
            turnaoundTime = processData[i][3] - processData[i][1]
            totalTurnaroundTime = totalTurnaroundTime + turnaoundTime
            processData[i].append(turnaoundTime)
        averageTurnaroundTime = totalTurnaroundTime / len(processData)
        return averageTurnaroundTime

    def calculateWaitingTime(self, processData):
        totalWaitingTime = 0
        for i in range(len(processData)):
            waitingTime = processData[i][4] - processData[i][2]
            totalWaitingTime = totalWaitingTime + waitingTime
            processData[i].append(waitingTime)
        averageWaitingTime = totalWaitingTime / len(processData)
        return averageWaitingTime

    def calculateResponseTime(self, processData):
        totalResponseTime = 0
        print(processData)
        for i in range(len(processData)):
            responseTime = processData[i][5]
            totalResponseTime = totalResponseTime + responseTime
            processData[i].append(responseTime)
        averageResponseTime = totalResponseTime / len(processData)
        return averageResponseTime


    def printData(self, processData, averageTurnaroundTime, averageWaitingTime, averageResponseTime):
        print(f'Average Turnaround Time: {averageTurnaroundTime}')
        print(f'Average Waiting Time: {averageWaitingTime}')
        print(f'Average Response Time: {averageResponseTime}')