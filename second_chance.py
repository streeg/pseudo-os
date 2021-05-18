def process_exists(process, pages):
    for page in pages:
        if page[0] == process:
            return True
    return False

def process_index(process, pages):
    for i, page in enumerate(pages):
        if page[0] == process:
            return i

def manage_rbit(pages):

    while pages[0][1] != 0:
        pages[0][2] += 1
        if pages[0][2] == 3:
            pages[0][1] = 0
        pages.append(pages[0])
        del(pages[0])
    
    del(pages[0])

fp = open('entrada.txt')

lines = fp.readlines()

total_frames = int(lines[0])

pages = []

fault = 0

# [no_pagina, r_bit, mem_ref]

for line in lines[1:]:
    process = int(line)
    # for i, page in enumerate(pages):
    #     pages[i][2] += 1
    #     if pages[i][2] == 3:
    #         pages[i][1] = 0

    if len(pages) < total_frames:
        if process_exists(process, pages):
            i = process_index(process, pages)
            pages[i][1] = 1
            pages[i][2] = 0
        else:
            fault += 1
            pages.append([process, 1, 0])
    
    else:
        if process_exists(process, pages):
            i = process_index(process, pages)
            pages[i][1] = 1
            pages[i][2] = 0
        else:
            fault += 1
            manage_rbit(pages)
            pages.append([process, 1, 0])
            

    print(pages)

print('SC ', fault)