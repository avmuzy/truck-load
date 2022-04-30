volume_vuc = (7.2*2.2*3.5)
carga_vuc = 3000
truck_vuc = (volume_vuc < 55.44), (carga_vuc < 3000)
print('A capacidade maxima de carga do Truck VUC  e de {}kg com volume de {:.2f}m2'.format(carga_vuc,volume_vuc))

