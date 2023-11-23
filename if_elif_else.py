trabalho_terminado = False
if trabalho_terminado == True:
    print('Bora dar uma saída!')

else:
    print('Não posso sair agora!')

    '''
    if condição:
        # comandos a serem executados
    '''

    numero_de_atrasos = 2
    if numero_de_atrasos >= 3:
        print('Vá para diretoria')
    elif numero_de_atrasos == 2:
        print('Essa é sua segunda falta!')
    elif numero_de_atrasos == 1:
        print('Essa é sua primeira falta')
    else:
        print('Pode entrar')


#    A velocidade máxima para essa rua é 50km
#    *Cruzou entre 51km a 60km, levou multa de 2 pontos
#    *Cruzou entre 61km a 75km, levou multa de 3 pontos
#    *Cruzou acima de 75kmkm, levou multa de 7 pontos
   
velocidade = 55
if velocidade <= 50:
    print('Não foi multado')
elif velocidade >= 51 and velocidade<=60:
    print('Multa de 2 pontos!')
elif velocidade >= 61 and velocidade<=75:
    print('Levou multa de 3 pontos!')
else:
    print('Levou multa de 7 pontos!')

# Chaining
velocidade = 55
if velocidade <= 50:
    print('Não foi multado')
elif 51 <= velocidade <=60:
    print('Multa de 2 pontos!')
elif velocidade >= 61 and velocidade<=75:
    print('Levou multa de 3 pontos!')
else:
    print('Levou multa de 7 pontos!')

#Desafio

# Monte o seguinte cenário usando condicionais: Você está montando um sistema para um salão de beleza para calcular o
# preço do corte de cabelos grandes que irá seguir as seguintes regras:

#   *Se seu cabelo estiver com ou abaixo de 20cm, você paga o valor de R$50,00
#   *Se seu cabelo estiver entre 21cm a 30cm, você paga o valor de R$70,00
#   *Se seu cabelo estiver entre 31cm a 50cm, você paga o valor de R$100,00
#   *acima de 50cm, favor consultar a recepção
# Declare uma variável que represente o tamanho atual do cabelo
# Apenas imprima na tela a mensagem apropriada, nada além disso é nescessário


tamanho_atual_cabelo = 50


if tamanho_atual_cabelo <= 20:
    print('R$50,00')
elif tamanho_atual_cabelo >= 21 and tamanho_atual_cabelo <= 30:
    print('R$ 70,00')
elif tamanho_atual_cabelo >= 31 and tamanho_atual_cabelo <= 50:
    print('R$ 100,00')
else:
    print("Favor passar na recepção")

tamanho_atual_cabelo = 50


if tamanho_atual_cabelo < 20:
    print('R$50,00')
elif 21 <= tamanho_atual_cabelo <= 30:
    print('R$ 70,00')
elif 31 <= tamanho_atual_cabelo <= 50:
    print('R$ 100,00')
else:
    print("Favor passar na recepção")