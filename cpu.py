# registers
ro   = 0x00 
rt   = 0x00
rtt  = 0x00
hld  = 0x00

# memory
RAM = []
for i in range(0xff): RAM.append(0x00)

def run(instruction):
    # get access to registers
    global ro
    global rt
    global rtt
    global hld
    global RAM

    # was hold changed?
    if hld != 0x00:
        # yes it was. Store the data in RTT and put the hld register in the instruction
        # so the held instruction actually gets run. Set hld to 0xff to signal that 
        # things were actually done
        rtt = instruction
        instruction = hld
        hld = 0xff

    # Huge match/case ladder for running the code
    match instruction:
        # === Misc. Operations ===
        case 0xea:
            # NOP
            # No operation. Pass and do nothing
            pass

        
        # === Register Operations ===
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
            # STRTT
            # This is easier because we dont need to do anything to RTT
            if hld == 0xff:
                hld = 0x00
            else:
                hld = 0x12

        case 0x13:
            # MVRO
            ro = rt


        # === Arithmetic Operations ===
        case 0x20:
            # ADD
            # Adds ro and rt and store it in ro
            ro = ro + rt

        case 0x21:
            # SUB
            # Subtracts ro and rt and store it in ro
            ro = ro - rt

        case 0x22:
            # MUL
            # Multiplies ro and rt and store it in ro
            ro = ro * rt

        case 0x23:
            # DIV
            # Divides ro and rt and store it in ro
            ro = ro / rt
        

        # === I/O Operations ===
        case 0x30:
            #INT
            # Interrupt
            
            if hld == 0xff:
                match rtt:
                    case 0x10:
                        print(chr(ro), end="")
                    
                    case _:
                        print("CPU Exception: invalid interrupt "+str(rtt), end="")
                hld = 0x00
            else:
                hld = 0x30

        case 0x31:
            #WMEM
            # Write to memory
            RAM[ro] = rt

        case 0x32:
            #RMEM
            # Read from memory
            rt = RAM[ro]


        case _:
            # Nothing matched, do nothing
            pass



code = []

with open("out.bin", "rb") as file:
    hex_string = file.read()

code = [byte for byte in hex_string]

for i in code:
    run(i)
    #print(RAM)
    #print("     REGISTERS: " + str(ro)+" "+ str(rt)+" "+str(rtt)+" "+str(hld))

with open("memdump.bin", "wb") as out:
    for i in RAM:
        out.write(i.to_bytes(1, "big"))