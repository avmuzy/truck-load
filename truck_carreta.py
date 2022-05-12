volume_carreta =(18.15*2.6*4.4)
carga_carreta = 33000
carreta = (volume_carreta < 207.63), (carga_carreta < 33000)
print('-' *80)
print("A capacidade maxima da carreta e de:", carga_carreta, ", com um volume de:", volume_carreta)
print('-' *80)
volume_pacote = peso_pacote = cont = somapeso = somavolume =0

r = 'S'

while r == 'S' and peso_pacote < carga_carreta and volume_pacote < volume_carreta:
    print('\033[37m=' * 40, '\033[m')
    volume_pacote = float(input("Entre com o volume do pacote em metros:"))
    somavolume += volume_pacote