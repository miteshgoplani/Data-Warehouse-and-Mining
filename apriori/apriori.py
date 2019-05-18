from itertools import combinations, permutations
import pandas as pd
import numpy as np
items = ['T-shirt','Trousers','Belt','Jacket','Gloves','Sneakers']
c = []
support = []

df = pd.read_csv("basket.csv")


for i in range(1,len(items)+1):
    comb = combinations(items, i)
    c.append(list(comb))
    


for i in range(len(c)):
    supp = []
    for j in range(len(c[i])):
        count=0
        for k in range(len(df)):
            arr = np.array(df["List"].loc[[k]])[0]  
            if all(eachitem in arr for eachitem in c[i][j]):
                count+=1
        supp.append(count)
    support.append(supp)

min_support = 2
pruned = []

for i in range(len(c)):
    for j in range (len(c[i])):
        pruned.append([c[i][j],support[i][j]])

i=0
while True:
    try:
        if pruned[i][1] < min_support:
            del pruned[i]
            i = i-1
        else:
            i = i+1
    except:
        break

for i in range(len(pruned)):
    print(pruned[i][0],pruned[i][1])

n = len(pruned)-1
m = len(pruned[n][0])
last = []

for i in range(len(pruned)):
    if len(pruned[i][0]) == m:
        last.append(list(pruned[i][0]))



def getConfidence(last,min_conf):
    for ls in last:
        left = []
        right = []

        for i in range(1, len(ls)):
            comb = list(combinations(ls,i))

        print("comb is",comb)

        for c in comb:
            left.append(c)
            temp = [x for x in ls if x not in c]
            right.append(tuple(temp))


        print("left is",left)
        print("right is",right)

        for A,B in zip(left,right):
            for i in range(len(pruned)):

                if A == pruned[i][0]:
                    suppA = pruned[i][1]

                s = A + B
                if s == pruned[i][0]:
                    suppAB = pruned[i][1]
            
            confpercent = (suppAB/suppA)*100
            if (confpercent>= min_conf):
                print(A,"->",B, "Confidence =", round(confpercent, 2),"%")
                

getConfidence(last,50)