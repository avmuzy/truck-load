volume_toco = (14*2.6*4.4)
carga_toco = 6000
trucktoco = (volume_toco < 160.16), (carga_toco < 6000)
print('-' *80)
print("A capacidade maxima do Truck toco e de:", carga_toco, ", com um volume de:", volume_toco)
print('-' *80)

volume_pacote = 0
peso_pacote = 0
while peso_pacote < carga_toco and volume_pacote < volume_toco:
    print('\033[37m=' * 40, '\033[m')
    volume_pacote = float(input("Entre com o volume do pacote em metros:"))
    peso_pacote = float(input("Entre como peso do pacote em kg:"))

pacote = (volume_pacote, peso_pacote)
capacidade_rest = (volume_toco - volume_pacote, carga_toco - peso_pacote)
volume_rest = (((volume_toco-volume_pacote)*100)/volume_toco)
carga_rest = (((carga_toco-peso_pacote)*100)/carga_toco)
perc_volume = ((volume_pacote*100)/volume_toco)
perc_peso = ((peso_pacote*100)/carga_toco)

print('O pacote equivale a {:.2f}% da capcidade volumetrica e {:.2f}% da capacidade de carga'
      .format(perc_volume, perc_peso))
if volume_pacote > volume_toco:
    print('\033[0:31m O pacote excede o volume de carga em {:.2f}%\033[m'.format(abs(volume_rest)))
else:
    print('Ainda restam {:.2f}% de area util e {:.2f}% de capacidade de carga'.format(volume_rest, carga_rest))

if peso_pacote > carga_toco:
    print('\033[0:31m O pacote excede a capacidade de carga em {:.2f}%\033[m'.format(abs(carga_rest)))
