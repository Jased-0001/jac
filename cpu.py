ro   = 0x00 
rt   = 0x00
rtt  = 0x00
hld  = 0x00

def run(instruction):
    # get access to registers
    global ro
    global rt
    global rtt
    global hld

    # was hold changed?
    if hld != 0x00:
        # yes it was. Store the data in RTT and put the hld register in the instruction
        # so the held instruction actually gets run. Set hld to 0xff to signal that 
        # things were actually done
        rtt = instruction
        instruction = hld
        hld = 0xff

    match instruction:
        case 0x00:
            # NOP
            # No operation. Pass and do nothing
            pass


        case 0x10:
            # STRO
            # Store whatever is in RTT in RO.
            # Takes two cycles, one to set up and one to store
            if hld == 0xff:
                ro = rtt
                rtt = 0x00
                hld = 0x00
            else:
                hld = 0x10

        case 0x11:
            # STRT
            # Store whatever is in RTT in RT
            # Same as 0x10
            if hld == 0xff:
                rt = rtt
                rtt = 0x00
                hld = 0x00
            else:
                hld = 0x11
            
        case 0x12:
            # STRTT (please never use)
            # This is easier because we dont need to do anything to RTT
            if hld == 0xff:
                hld = 0x00
            else:
                hld = 0x12


                
        case 0x20:
            # ADD
            # Adds ro and rt and store it in ro
            ro = ro + rt

        case 0x21:
            # SUB
            # Subtracts ro and rt and stores it in ro
            ro = ro - rt

        
        case 0x30:
            #PRN
            # Print RO's character
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
