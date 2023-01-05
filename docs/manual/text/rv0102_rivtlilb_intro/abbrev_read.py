print("start")
with open("abbrev2.txt", "r") as fP:
    readL = fP.readlines()
#print(readL)

abbL = []
for i2 in readL:
    i2L = i2.split("\t", 1)
    abbL.append(i2L)
#print(abbL)

with open("abbrev_tex.txt", "w") as fP:
    for i3 in abbL:
        print(i3)
        abbrS = "{" + i3[0] +"}"
        descripS = "{" + i3[1] +"}"
        iS = f"\\indent\\textbf{abbrS}         \\>  {descripS}\\\\"
        fP.write(iS)
