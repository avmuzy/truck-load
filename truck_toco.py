volume_toco = (14*2.6*4.4)
carga_toco = 6000
trucktoco = (volume_toco == 160.16), (carga_toco == 6000)
print('-' *80)
print("A capacidade maxima do Truck toco e de:", carga_toco, ", com um volume de:", volume_toco)
print('-' *80)

volume_pacote = peso_pacote  = somapeso = somavolume =0
cont = 1
r = 'S'

while r == 'S' and peso_pacote < carga_toco and volume_pacote < volume_toco:
    print('\033[37m=' * 40, '\033[m')
    volume_pacote = float(input("Entre com o volume do pacote em metros:"))
    somavolume += volume_pacote
    cont += 1
    peso_pacote = float(input("Entre como peso do pacote em kg:"))
    somapeso += peso_pacote
    if peso_pacote < carga_toco:
        r = str(input('Deseja inserir outro pacote? [S/N]')).strip().upper()
    if somavolume > volume_toco:
        print(f'\033[31m Limite de volume excedido em {somavolume - volume_toco}m2!\033[m')
    if somapeso > carga_toco:
        print(f'\033[31m Limite de carga excedido em {somapeso - carga_toco}Kg\033[m')
print(f'Foram inseridos {cont} pacotes com um total de {somapeso}Kg em {somavolume}m2.')

pacote = (volume_pacote, peso_pacote)
capacidade_rest = (volume_toco - volume_pacote, carga_toco - peso_pacote)
volume_rest = (((volume_toco-volume_pacote)*100)/volume_toco)
carga_rest = (((carga_toco-peso_pacote)*100)/carga_toco)
perc_volume = ((volume_pacote*100)/volume_toco)
perc_peso = ((peso_pacote*100)/carga_toco)

print(f'Os pacotes equivalem a {perc_volume:.2f}% da capcidade volumetrica e {perc_peso:.2f}% da capacidade de carga')
if volume_pacote > volume_toco:
    print(f'\033[0:31m O pacote excede o volume de carga em {abs(volume_rest):.2f}%\033[m')
else:
    print(f'Ainda restam {volume_rest:.2f}% de area util e {carga_rest:.2f}% de capacidade de carga')

if peso_pacote > carga_toco:
    print(f'\033[0:31m O pacote excede a capacidade de carga em {abs(carga_rest):.2f}%\033[m')
