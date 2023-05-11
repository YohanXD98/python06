count1 = 0
count2 = 0
count3 = 0

for e in range (1,16):
    op = int(input("Qual foi a sua opinião em relação ao filme ? 1-ótimo 2-bom 3-regular"))
    
    if op == 1:
        count1 = count1 +1
    if op == 2:
        count2 = count2 +1
        
    if op == 3:
        count3 = count3 +1

print("Pessoas que votaram em ótimo:{}" .format(count1))
print("Pessoas que votaram em bom:{}" .format(count2))
print("Pessoas que votaram em regular:{}" .format(count3))