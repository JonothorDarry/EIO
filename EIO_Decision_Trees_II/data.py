all_data=[]

#Confidence, Binary Splits, NumObj
for i in range(2, 11, 2):
    for j in range(0, 2):
        for ij in range(2, 5, 1):
            all_data.append([i/10, j==1, ij])

bonus=[[], []]

for i, x in enumerate(bonus):
    all_data[i].extend(bonus)


print(all_data)
