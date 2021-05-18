class Inout():

    def printInout(self):
        print("In/Out")

    def scan(self, fileName):
        fp = open(fileName, 'r')

        lines = fp.readlines()

        max_cil = int(lines[0])
        cur_cil = int(lines[1])

        entries = []
        count = 0

        for line in lines[2:]:
            entries.append(int(line))

        # Esquerda pra direita
        # min_read = min(entries)

        # for i in range(cur_cil, max_cil + 1):
        #     count += 1
        #     if i in entries:
        #         entries.remove(i)
            
            
        # for i in range(max_cil, min_read - 1, -1):
        #     count += 1
        #     if i in entries:
        #         entries.remove(i)

        # Direita para esquerda
        max_read = max(entries)

        for i in range(cur_cil - 1, -1, -1):
            count += 1
            if i in entries:
                entries.remove(i)

        for i in range(1, max_read + 1):
            count += 1
            if i in entries:
                entries.remove(i)
            
        fp.close()
        print('SCAN ', count)
