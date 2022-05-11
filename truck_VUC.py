volume_vuc = (7.2*2.2*3.5)
carga_vuc = 3000
truck_vuc = (volume_vuc < 55.44), (carga_vuc < 3000)

print('-' *80)
print("A capacidade maxima do Truck VUC e de:{:.2f}Kg , com um volume de:{:.2f}m2".format(carga_vuc, volume_vuc))
print('-' *80)

volume_pacote = peso_pacote = somapeso = somavolume = cont = 0

r = 'S'