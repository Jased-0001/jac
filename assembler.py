import sys

args = sys.argv

asm = open(args[1],  "r")
#asm = open("hello.s", "r")
out = open("out.bin", "wb")

code = asm.read().split("\n")


print("Removing comments")
for i in range(len(code)):
    code[i] = code[i].split(";")[0]


print("Splitting code and data")
for i in range(len(code)):
    z = code[i].split(" ")


print("Replacing assembly with machine code")
for i in range(len(code)):
    code[i] = code[i].lower()
    code[i] = code[i].replace("stro", "0x10")
    code[i] = code[i].replace("strtt", "0x12")
    code[i] = code[i].replace("strt", "0x11")
    code[i] = code[i].replace("mvro", "0x13")

    code[i] = code[i].replace("add", "0x20")
    code[i] = code[i].replace("sub", "0x21")
    code[i] = code[i].replace("mul", "0x22")
    code[i] = code[i].replace("div", "0x23")

    code[i] = code[i].replace("int", "0x30")
    code[i] = code[i].replace("wmem", "0x31")
    code[i] = code[i].replace("rmem", "0x32")

    code[i] = code[i].replace("nop", "0xea")


_code = []
for i in range(len(code)):
    code[i] = code[i].split(" ")
    while("" in code[i]):
        code[i].remove("")

    for z in code[i]:
        _code.append(z)

code = _code
_code = None

while("" in code):
    code.remove("")

for i in code:
    out.write(int(i, 16).to_bytes(1, "big"))

asm.close()
out.close()