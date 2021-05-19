# -*- coding: utf-8 -*-

class elevator:

    def processData(self, fileName):
        fp = open(fileName, 'r')
        lines = fp.readlines()
        maxCil = int(lines[0])
        curCil = int(lines[1])
        entries = []
        count = 0
        for line in lines[2:]:
            entries.append(int(line))

        # Direita para esquerda
        maxRead = max(entries)

        for i in range(curCil - 1, -1, -1):
            count += 1
            if i in entries:
                entries.remove(i)

        for i in range(1, maxRead + 1):
            count += 1
            if i in entries:
                entries.remove(i)
            
        fp.close()
        print('SCAN ', count)
