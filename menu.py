print('MENU PRINCIPAL')
print('=' * 40)
print('''Escolha o veiculo que pretende utilizar:
\033[32m[1] VUC
[2] Toco (2 eixos)
[3] Carreta
[4] Entrar com o peso(Kg) e o volumme:(m2)\033[m ''')

opcao = int(input('Entre com a opcao desejada:'))

if opcao == 4:

    peso = float(input('Entre com o peso da carga:'))
    volume = float(input('Entre com o volume da carga:'))
    if peso <= 3000 or volume < 55.44:
        print(' Usar truck VUC')

    elif 3000 < peso <= 6000 or 55.44 < volume <= 160.16:
        print('Usar truck Toco')

    elif 600 < peso <= 33000 or 160.16 < volume <= 207.63:
        print('Usar Carreta')

    volume_vuc = (7.2 * 2.2 * 3.5)
    carga_vuc = 3000
    truck_vuc = (volume_vuc < 55.44), (carga_vuc < 3000)

    volume_toco = (14 * 2.6 * 4.4)
    carga_toco = 6000
    trucktoco = (volume_toco < 160.16), (carga_toco < 6000)

    volume_carreta = (18.15 * 2.6 * 4.4)
    carga_carreta = 33000
    carreta = (volume_carreta < 207.63), (carga_carreta < 33000)

    print('''\033[32m
[1] Voltar ao menu incial
[2] Sair''')
    opcao2 = int(input('[1 ou 2]\033[m'))
    if opcao2 == 1:
        print('volta menu')

if opcao == 1:
    from truck_VUC import *

if opcao == 2:
    from truck_toco import *
if opcao == 3:
    from truck_carreta import *
