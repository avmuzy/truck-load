peso = float(input('Entre com o peso da carga:'))
volume = float(input('Entre com o volume da carga:'))
volume_vuc = (7.2*2.2*3.5)
carga_vuc = 3000
truck_vuc = (volume_vuc < 55.44), (carga_vuc < 3000)

volume_toco = (14*2.6*4.4)
carga_toco = 6000
trucktoco = (volume_toco < 160.16), (carga_toco < 6000)

volume_carreta =(18.15*2.6*4.4)
carga_carreta = 33000
carreta = (volume_carreta < 207.63), (carga_carreta < 33000)

if peso <= 3000 and volume < 55.44:
    print(' Usar truck VUC')

elif 3000 < peso <= 6000 and 55.44 < volume <= 160.16:
    print('Usar truck Toco')

elif 600 < peso <= 33000 and 160.16 < volume <= 207.63:
    print('Usar Carreta')

