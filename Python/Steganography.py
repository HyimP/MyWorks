from PIL import Image

img = Image.open("test.png")



infoToencrypt = 'encrypt this into picture'.upper()




letterTonumber = []

# A=0, B=1, .... Z=25, Space=26
# Appends corresponding numbers from input to a list
for i in range(len(infoToencrypt)):
    if ord(infoToencrypt[i]) >= 65:
        letterTonumber.append(ord(infoToencrypt[i])-65)
    else:
        letterTonumber.append(26)


binary = []

# Changes numbers from list above into bit format, breaks each bit into 4 segments and appends segments to a list
for i in range(len(letterTonumber)):
    numberTobit = bin(letterTonumber[i])
    Eightdigbit = numberTobit[2:].rjust(8,"0")
    n = 0
    m = 2
    for j in range(4):
        binary.append(Eightdigbit[n:m])
        n += 2
        m += 2








pixels = list(img.getdata())


for i in range(len(binary)):
    for j in range(len(pixels[i])):
        pixels[i] = 100




    #print(pixels[i])


#for i in range(0,25):
