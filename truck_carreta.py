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
    cont += 1
    peso_pacote = float(input("Entre como peso do pacote em kg:"))
    somapeso += peso_pacote
    if peso_pacote < carga_carreta:
        r = str(input('Deseja inserir outro pacote? [S/N]')).strip().upper()
        if somavolume > volume_carreta:
            print('\033[31m Limite de volume excedido em {}m2!\033[m'.format(somavolume - volume_carreta))
        if somapeso > carga_carreta:
            print('\033[31m Limite de carga excedido em {}Kg\033[m'.format(somapeso - carga_carreta))
    print('Foram inseridos {} pacotes com um total de {}Kg em {}m2.'.format(cont, somapeso, somavolume))