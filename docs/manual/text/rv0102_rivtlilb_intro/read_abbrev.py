with open(list.txt, r) as fP:
    readL = fP.readline()

abbL = []
for i2 in readL:
    i2.split()
    abbL.append(i2)

for i3 in abbL:
    iS = f"\\indent\\bf{{i3[0]}}         \\>  {{i3.[1]}}\\\\"