from allpairspy import AllPairs

data = [
    ["DELL", "ACER", "ASUS"],
    ["WIN7", "XP", "WIN10"],
    ["AMD", "INTEL", "ARM"],
]

res = AllPairs(data)

for i, el in enumerate(res):
    print(i+1, el)

print("=" * 20)

i = 1
for comp in data[0]:
    for oper in data[1]:
        for proc in data[2]:
            print(i, [comp, oper, proc])
            i =+ 1
