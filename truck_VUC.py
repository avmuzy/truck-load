volume_vuc = (7.2*2.2*3.5)
carga_vuc = 3000
truck_vuc = (volume_vuc < 55.44), (carga_vuc < 3000)

print('-' *80)
print("A capacidade maxima do Truck VUC e de:{:.2f}Kg , com um volume de:{:.2f}m2".format(carga_vuc, volume_vuc))
print('-' *80)
volume_pacote = peso_pacote = somapeso = somavolume  = 0
cont = 1
r = 'S'

while r == 'S' and peso_pacote < carga_vuc and volume_pacote < volume_vuc:
    print('\033[37m=' * 40, '\033[m')
    print('{} pacote'.format(cont))
    volume_pacote = float(input("Entre com o volume do pacote em metros:"))
    somavolume += volume_pacote
    cont += 1
    peso_pacote = float(input("Entre como peso do pacote em kg:"))
    somapeso += peso_pacote
    if peso_pacote < carga_vuc:
        r = str(input('Deseja inserir outro pacote? [S/N]')).strip().upper()


    if somavolume > volume_vuc:
        print('\033[31m Limite de volume excedido em {:.2f}m2!\033[m'.format(somavolume - volume_vuc))
    if somapeso > carga_vuc:
        print('\033[31m Limite de carga excedido em {}Kg\033[m'.format(somapeso - carga_vuc))

print('Foram inseridos {} pacotes com um total de {:.2f}Kg em {:.2f}m2.'.format(cont, somapeso, somavolume))

pacote = (volume_pacote, peso_pacote)
capacidade_rest = (volume_vuc - volume_pacote, carga_vuc - peso_pacote)
volume_rest = (((volume_vuc-volume_pacote)*100)/volume_vuc)
carga_rest = (((carga_vuc-peso_pacote)*100)/carga_vuc)
perc_volume = ((volume_pacote*100)/volume_vuc)
perc_peso = ((peso_pacote*100)/carga_vuc)

print('Os pacotes equivalem a {:.2f}% da capcidade volumetrica e {:.2f}% da capacidade de carga'
      .format(perc_volume, perc_peso))
if volume_pacote > volume_vuc:
    print('\033[0:31m O pacote excede o volume de carga em {:.2f}%\033[m'.format(abs(volume_rest)))
else:
    print(f'Ainda restam {volume_rest:.2f}% de area util e {carga_rest:.2f}% de capacidade de carga')

if peso_pacote > carga_vuc:
    print('\033[0:31m O pacote excede a capacidade de carga em {:.2f}%\033[m'.format(abs(carga_rest)))
