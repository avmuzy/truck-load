volume_toco = (14*2.6*4.4)
carga_toco = 6000
trucktoco = (volume_toco > 160.16), (carga_toco < 6000)
print("A capacidade maxima do Truck toco e de:", carga_toco, ", com um volume de:", volume_toco)

volume_pacote = float(input("Entre com o volume do pacote em metros:"))
peso_pacote = float(input("Entre como peso do pacote em kg:"))
pacote = (volume_pacote, peso_pacote)