volume_carreta =(18.15*2.6*4.4)
carga_carreta = 33000
carreta = (volume_carreta < 207.63), (carga_carreta < 33000)
print('-' *80)
print("A capacidade maxima da carreta e de:", carga_carreta, ", com um volume de:", volume_carreta)
print('-' *80)
volume_pacote = peso_pacote  = somapeso = somavolume =0
cont = 1
r = 'S'

while r == 'S' and peso_pacote < carga_carreta and volume_pacote < volume_carreta:
    print('\033[37m=' * 40, '\033[m')
    volume_pacote = float(input("Entre com o volume do pacote em metros:"))
    somavolume += volume_pacote
    cont += 1
    peso_pacote = float(input("Entre como peso do pacote em kg:"))
    somapeso += peso_pacote
    if peso_pacote < carga_carreta:
        r = str(input('Deseja inserir outro pacote? [S/N]')).strip().upper()
        if somavolume > volume_carreta:
            print(f'\033[31m Limite de volume excedido em {somavolume-volume_carreta}m2!\033[m')
        if somapeso > carga_carreta:
            print('\033[31m Limite de carga excedido em {}Kg\033[m'.format(somapeso - carga_carreta))
    print(f'Foram inseridos {cont} pacotes com um total de {somapeso}Kg em {somavolume}m2.')

pacote = (volume_pacote, peso_pacote)
capacidade_rest = (volume_carreta - volume_pacote, carga_carreta - peso_pacote)
volume_rest = (((volume_carreta-volume_pacote)*100)/volume_carreta)
carga_rest = (((carga_carreta-peso_pacote)*100)/carga_carreta)
perc_volume = ((volume_pacote*100)/volume_carreta)
perc_peso = ((peso_pacote*100)/carga_carreta)

print('Os pacotes equivalem a {:.2f}% da capcidade volumetrica e {:.2f}% da capacidade de carga'
      .format(perc_volume, perc_peso))
if volume_pacote > volume_carreta:
    print('\033[0:31m O pacote excede o volume de carga em {:.2f}%\033[m'.format(abs(volume_rest)))
else:
    print('Ainda restam {:.2f}% de area util e {:.2f}% de capacidade de carga'.format(volume_rest, carga_rest))

if peso_pacote > carga_carreta:
    print('\033[0:31m O pacote excede a capacidade de carga em {:.2f}%\033[m'.format(abs(carga_rest)))
