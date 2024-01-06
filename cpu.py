ro   = 0x00 
rt   = 0x00
rtt  = 0x00
hld  = 0x00

def run(instruction):
    global ro
    global rt
    global rtt
    global hld

    if hld != 0x00:
        rtt = instruction
        instruction = hld
        hld = 0xff

    match instruction:
        case 0x00:
            # NOP
            print("NOP", end="")
            pass

        case 0x01:
            # TST
            print("TST", end="")



        case 0x10:
            # STRO
            if hld == 0xff:
                ro = rtt
                rtt = 0x00
                hld = 0x00
            else:
                hld = 0x10

        case 0x11:
            # STRT
            if hld == 0xff:
                rt = rtt
                rtt = 0x00
                hld = 0x00
            else:
                hld = 0x11
            
        case 0x12:
            # STRTT (please never use)
            if hld == 0xff:
                hld = 0x00
            else:
                hld = 0x12


                
        case 0x20:
            # ADD

            ro = ro + rt

        case 0x21:
            # SUB

            ro = ro - rt

        
        case 0x30:
            #PRN
            print(chr(ro), end="")

        case _:
            # Nothing matched, do nothing
            pass




code = [
    0x10, 0xaa, #STRO  0xAA
    0x11, 0xbb, #STRT  0xBB
    0x12, 0xf0, #STRTT 0xF0
    0x20,       #ADD
    0x30,       #PRN
    0x11, 0xbb, #STRT  0xBB
    0x21,       #SUB
    0x30,       #PRN

    #run hello world
    0x10, 0x48, #STRO  0x48 
    0x30,       #PRN
    0x10, 0x65, #STRO  0x65
    0x30,       #PRN
    0x10, 0x6c, #STRO  0x6c
    0x30,       #PRN
    0x10, 0x6c, #STRO  0x6c
    0x30,       #PRN
    0x10, 0x6f, #STRO  0x6f
    0x30,       #PRN
]

for i in code:
    run(i)

    #print("     REGISTERS: " + str(ro)+" "+ str(rt)+" "+str(rtt)+" "+str(hld))
