=== Register Operations (0x1-) === 
Use these to store data in any of the three registers.

0x10 - STRO
Stores following data in the RO register
Takes two cycles

0x11 - STRT
Stores following data in the RT register
Takes two cycles

0x12 - STRTT
Stores following data in the RTT register
Takes two cycles

0x13 - MVRO
Moves RT into RO
Takes 1 cycle



=== Arithmetic Operations (0x2-) ===
0x20 - ADD
Adds ro and rt and stores it in ro
Takes one cycle

0x21 - SUB
Subtracts ro and rt and stores it in ro
Takes one cycle

0x22 - MUL
Multiplies ro and rt and stores it in ro
Takes one cycle

0x23 - DIV
Divides ro and rt and stores it in ro
Takes one cycle



=== I/O Operations (0x3-) ===
0x30 - PRN
Prints ro
Takes one cycle

0x31 - WMEM
Write to memory
Address to write to will be RO
Data to write will be in RT
Takes one cycle

0x32 - RMEM
Read from memory
Address to write to will be RO
Data will be returned in RT
Takes one cycle



=== Miscellaneous Operations (0x--) ===
0xea - NOP
No operation
Takes one cycle
