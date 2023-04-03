print(f"Bem vindo a Mega Promoção do mercadinho BigBom!")

precoContra = float(input('Insira o preço do contra filé: R$ '))
qMinContra = float(input('Qual a quantidade miníma do contra filé a ser comprado: '))
qMaxContra = float(input('Qual a quantidade maxíma do contra filé a ser comprado: '))
if qMinContra > qMaxContra:
    qMinContra = float(input('Qual a quantidade miníma do contra filé a ser comprado: '))
    qMaxContra = float(input('Qual a quantidade maxíma do contra filé a ser comprado: '))
descVinteContra = float(input('Informe o valor minímo para o desconto de 20% para o contra filé: ')) 
if descVinteContra > qMaxContra or descVinteContra < qMinContra:
    descVinteContra = float(input('Informe o valor minímo para o desconto de 20% para o contra filé: ')) 

precoPanceta = float(input('Insira o preço da panceta: R$ '))
qMinPanceta = float(input('Qual a quantidade miníma da panceta a ser comprado: '))
qMaxPanceta = float(input('Qual a quantidade maxíma da panceta a ser comprado: '))
if qMinPanceta > qMaxPanceta:
    qMinPanceta = float(input('Qual a quantidade miníma da panceta a ser comprado: '))
    qMaxPanceta = float(input('Qual a quantidade maxíma da panceta a ser comprado: '))
descVintePanceta = float(input('Informe o valor minímo para o desconto de 20% para a panceta: '))
if descVintePanceta > qMaxPanceta or descVintePanceta < qMinPanceta:
    descVintePanceta = float(input('Informe o valor minímo para o desconto de 20% para a panceta: ')) 

precoPao = float(input('Insira o preço do pão de alho: R$ '))
qMinPao = float(input('Qual a quantidade miníma do pão de alho a ser comprado: '))
qMaxPao = float(input('Qual a quantidade maxíma do pão de alho a ser comprado: '))
if qMinPao > qMaxPao:
    qMinPao = float(input('Qual a quantidade miníma do pão de alho a ser comprado: '))
    qMaxPao = float(input('Qual a quantidade maxíma do pão de alho a ser comprado: '))
descVintePao = float(input('Informe o valor minímo para o desconto de 20% para o pão de alho: '))
if descVintePao > qMaxPao or descVintePao < qMinPao:
    descVintePao = float(input('Informe o valor minímo para o desconto de 20% para o pão de alho: '))

precoCerveja = float(input('Insira o preço da cerveja lata: R$ '))
qMinCerveja = float(input('Qual a quantidade miníma da cerveja lata a ser comprado: '))
qMaxCerveja = float(input('Qual a quantidade maxíma da cerveja lata a ser comprado: '))
if qMinCerveja > qMaxCerveja:
    qMinCerveja = float(input('Qual a quantidade miníma da cerveja lata a ser comprado: '))
    qMaxCerveja = float(input('Qual a quantidade maxíma da cerveja lata a ser comprado: '))
descVinteCerveja = float(input('Informe o valor minímo para o desconto de 20% para a cerveja: '))
if descVinteCerveja > qMaxCerveja or descVinteCerveja < qMinCerveja:
    descVinteCerveja = float(input('Informe o valor minímo para o desconto de 20% para a cerveja: '))

precoRefri = float(input('Insira o preço do refrigerante lata: R$ '))
qMinRefri = float(input('Qual a quantidade miníma do refrigerante lata a ser comprado: '))
qMaxRefri = float(input('Qual a quantidade maxíma do refrigerante lata a ser comprado: '))
if qMinRefri > qMaxRefri:
    qMinRefri = float(input('Qual a quantidade miníma do refrigerante lata a ser comprado: '))
    qMaxRefri = float(input('Qual a quantidade maxíma do refrigerante lata a ser comprado: '))
descVinteRefri = float(input('Informe o valor minímo para o desconto de 20% para o refrigerante: '))
if descVinteRefri > qMaxRefri or descVinteRefri < qMinRefri:
    descVinteRefri = float(input('Informe o valor minímo para o desconto de 20% para o refrigerante: '))

precoCarvao = float(input('Insira o preço do carvão: R$ '))
qMinCarvao = float(input('Qual a quantidade miníma do carvão a ser comprado: '))
qMaxCarvao = float(input('Qual a quantidade maxíma do carvão a ser comprado: '))
if qMinCarvao > qMaxCarvao:
    qMinCarvao = float(input('Qual a quantidade miníma do carvão a ser comprado: '))
    qMaxCarvao = float(input('Qual a quantidade maxíma do carvão a ser comprado: '))
descVinteCarvao = float(input('Informe o valor minímo para o desconto de 20% para o carvão: '))
if descVinteCarvao > qMaxCarvao or descVinteCarvao < qMinCarvao:
    descVinteCarvao = float(input('Informe o valor minímo para o desconto de 20% para o carvão: '))

valorDescDez = float(input('Qual deve ser o valor total minímo para conseguir o desconto de 10%?: '))

qCliContra = float(input('Qual foi a quantidade de contra filé que seu cliente comprou?: '))
qCliPanceta = float(input('Qual foi a quantidade de panceta que seu cliente comprou?: '))
qCliPao = float(input('Qual foi a quantidade de pão de alho que seu cliente comprou?: '))
qCliCerveja = float(input('Qual foi a quantidade de cerveja que seu cliente comprou?: '))
qCliRefri = float(input('Qual foi a quantidade de refrigerante lata que seu cliente comprou?: '))
qCliCarvao = float(input('Qual foi a quantidade de carvão que seu cliente comprou?: '))

#Verificando se o cliente poderá ou não levar o produto pela quantidade.:
if qMinContra > qCliContra:
    qCliContra = 0
    print('O cliente não poderá levar o contra filé por não atingir a quantidade miníma!')
elif qMaxContra < qCliContra:
    qCliContra = 0 
    print('O cliente não poderá levar o contra filé por exceder a quantidade maxíma!')

if qMinPanceta > qCliPanceta:
    qCliPanceta = 0
    print('O cliente não poderá levar a panceta por não atingir a quantidade miníma!')
elif qMaxPanceta < qCliPanceta:
    qCliPanceta = 0 
    print('O cliente não poderá levar a panceta por exceder a quantidade maxíma!')

if qMinPao > qCliPao:
    qCliPao = 0
    print('O cliente não poderá levar o pão de alho por não atingir a quantidade miníma!')
elif qMaxPao < qCliPao:
    qCliPao = 0 
    print('O cliente não poderá levar o pão de alho por exceder a quantidade maxíma!')

if qMinCerveja > qCliCerveja:
    qCliCerveja = 0
    print('O cliente não poderá levar a cerveja por não atingir a quantidade miníma!')
elif qMaxCerveja < qCliCerveja:
    qCliCerveja = 0 
    print('O cliente não poderá levar a cerveja por exceder a quantidade maxíma!')

if qMinRefri > qCliRefri:
    qCliRefri = 0
    print('O cliente não poderá levar o refrigerante por não atingir a quantidade miníma!')
elif qMaxRefri < qCliRefri:
    qCliRefri = 0 
    print('O cliente não poderá levar o refrigerante por exceder a quantidade maxíma!')

if qMinCarvao > qCliCarvao:
    qCliCarvao = 0
    print('O cliente não poderá levar o carvão por não atingir a quantidade miníma!')
elif qMaxCarvao < qCliCarvao:
    qCliCarvao = 0 
    print('O cliente não poderá levar o carvão por exceder a quantidade maxíma!')

#Valor a ser pago em cada quantidade:
qCliContra = qCliContra * precoContra
qCliPanceta = qCliPanceta  * precoPanceta
qCliPao = qCliPao * precoPao
qCliCerveja = qCliCerveja * precoCerveja
qCliRefri = qCliRefri * precoRefri
qCliCarvao = qCliCarvao * precoCarvao

valorSemDesc = qCliContra + qCliPanceta + qCliPao + qCliCerveja + qCliRefri + qCliCarvao

#Com o valor já pago inicia-se as validações das promoções:
if descVinteContra < qCliContra:
    descVinteContra = 0.2 * qCliContra
    qCliContra = qCliContra - descVinteContra 
else:
    descVinteContra = 0

if descVintePanceta < qCliPanceta:
    descVintePanceta = 0.2 * qCliPanceta
    qCliPanceta = qCliPanceta - descVintePanceta
else: 
    descVintePanceta = 0

if descVintePao < qCliPao:
    descVintePao = 0.2 * qCliPao
    qCliPao = qCliPao - descVintePao
else:
    descVintePao = 0

if descVinteCerveja < qCliCerveja:
    descVinteCerveja = 0.2 * qCliCerveja
    qCliCerveja = qCliCerveja - descVinteCerveja
else:
    descVinteCerveja = 0

if descVinteRefri < qCliCerveja:
    descVinteRefri = 0.2 * qCliRefri
    qCliRefri = qCliRefri - descVinteRefri
else:
    descVinteRefri = 0

if descVinteCarvao < qCliCarvao:
    descVinteCarvao = 0.2 * qCliCarvao
    qCliCarvao = qCliCarvao - descVinteCarvao
else:
    descVinteCarvao = 0

if valorSemDesc > valorDescDez:
    descDez = valorSemDesc * 0.1
else:
    descDez = 0

valorComDesc = (qCliContra + qCliPanceta + qCliPao + qCliCerveja + qCliRefri + qCliCarvao) - descDez

valorDesc = descVinteContra + descVintePanceta + descVintePao + descVinteCerveja + descVinteRefri + descVinteCarvao + descDez

print(f"A compra total do cliente foi de R${valorSemDesc:.2f}, porém, graças a promoção do Churras, o valor do desconto foi de {valorDesc:.2f}, portanto o total a se pagar é de {valorComDesc:.2f}")
