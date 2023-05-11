##EXPLICAÇÃO DE FOR----------------------------------------------------------------
for i in range(0, 101):
    print("i")

##ATIVIDADE 01---------------------------------------------------------------------
for i in range(1,10,2):
    print(i)

##ATIVIDADE 02---------------------------------------------------------------------
for i in range(1,20,2):
    print(i)

##ATIVIDADE 03---------------------------------------------------------------------
for d in range(1,11):
    num = int(input("insira o número {}: " .format(d)))
    trip = num * 3

    if trip >= 0:
        print( ,trip)
        print("É positivo")

    else:
        print( ,trip)
        print("É negativo")

##ATIVIDADE 04---------------------------------------------------------------------
count1 = 0
count2 = 0

for e in range (1,16):
    op = int(input("Você gosta de beterraba ? 1-sim 2-não"))
    
    if op == 1:
        count1 = count1 +1
    if op == 2:
        count2 = count2 +1

print("Pessoas que votaram em sim:{}" .format(count1))
print("Pessoas que votaram em não:{}" .format(count2))

##ATIVIDADE 05---------------------------------------------------------------------
alto = 0
for x in range (1,11):
    preço = int(input("Insira o preço do produto: "))

    if preço >= alto:
        alto = preço

print("O mais caro custa:R${}" .format(alto))

##ATIVIDADE 06---------------------------------------------------------------------
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