import random

tipo = input("===BEM VINDO A FORCA===\n1 - Iniciar a Forca\n2 - Sair\n=======================\n")
while(tipo != '1' and tipo != '2'):
    tipo = input("===BEM VINDO A FORCA===\n1 - Iniciar a Forca\n2 - Sair\n=======================\n")
win = 0
loss = 0
fim = 0

while(tipo != '2'):
    fim = 1
    letras = []
    resp = []
    lista = ['banana','abacaxi','pera','uva','carambola','laranja','melancia']
    lista1 = ['corolla','fusca','camaro','uno','celta','subaru','supra']
    lista2 = ['faca','colher','garfo','dado','cama','ventilador','panela']
    lista3 = ['cavalo','elefante','pato','cachorro','gato','rato','girafa']
    tema = ['Frutas','Carros','Objetos','Animais']

    r_tema = random.choice(tema)

    if(r_tema == 'Frutas'):
        palavra = random.choice(lista)
    elif (r_tema == 'Carros'):
        palavra = random.choice(lista1)
    elif(r_tema == 'Objetos'):
        palavra = random.choice(lista2)
    else:
        palavra = random.choice(lista3)

    cont = 0

    des_forca = ['''
     +---+
     |   |
         |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========''']

    for i in range(0,len(palavra)):
        resp.append('_')

    while cont < 6 and '_' in resp:
        print("=========================================")
        print('===TEMA===\n',r_tema)
        if (r_tema == 'Frutas'):
            if (palavra == 'banana' and cont == 3):
                print("===DICA===\nTem casca e um animal ama comer com casca!")
            elif (palavra == 'abacaxi' and cont == 3):
                print("===DICA===\nÉ uma casa em um desenho infantil!")
            elif (palavra == 'pera' and cont == 3):
                print("===DICA===\nAmarela com semente dentro!")
            elif (palavra == 'uva' and cont == 3):
                print("===DICA===\nEla é feita a colheita em cachos!")
            elif (palavra == 'carambola' and cont == 3):
                print("===DICA===\nA fruta de sabor agridoce possui formato comprido, ligeiramente ovalado e com cinco gomos salientes!")
            elif (palavra == 'laranja' and cont == 3):
                print("===DICA===\nNão tem sorvete no sabor da fruta!")
            elif (palavra == 'melancia' and cont == 3):
                print("===DICA===\nÉ feita sua colheita no solo!")
        elif (r_tema == 'Carros'):
            if (palavra == 'corolla' and cont == 3):
                print("===DICA===\nConhecido por ser usado por idosos ricos!")
            elif (palavra == 'fusca' and cont == 3):
                print("===DICA===\nUm carro antigo porem ainda muito utilizado!")
            elif (palavra == 'camaro' and cont == 3):
                print("===DICA===\nFamoso por uma cor!")
            elif (palavra == 'uno' and cont == 3):
                print("===DICA===\nTem a fama por ser utilizado em firmas!")
            elif (palavra == 'celta' and cont == 3):
                print("===DICA===\nMuito comum na sociedade!")
            elif (palavra == 'subaru' and cont == 3):
                print("===DICA===\nDrift!")
            elif (palavra == 'supra' and cont == 3):
                print("===DICA===\nVeio do Japão e é muito famoso e utilizado em animes e filmes!")
        elif (r_tema == 'Objetos'):
            if (palavra == 'faca' and cont == 3):
                print("===DICA===\nMuito afiado!")
            elif (palavra == 'colher' and cont == 3):
                print("===DICA===\nGeralmente utilizado para liquidos!")
            elif (palavra == 'garfo' and cont == 3):
                print("===DICA===\nUtilizado para espetar alimentos!")
            elif (palavra == 'dado' and cont == 3):
                print("===DICA===\n usado para tabuleiros!")
            elif (palavra == 'cama' and cont == 3):
                print("===DICA===\nRepouso!")
            elif (palavra == 'ventilador' and cont == 3):
                print("===DICA===\nRefrescar!")
            elif (palavra == 'panela' and cont == 3):
                print("===DICA===\nPreparar o alimento!")
        else:
            if (palavra == 'cavalo' and cont == 3):
                print("===DICA===\nO corpo é coberto por pelos curtos e lisos de coloração variada!")
            elif (palavra == 'elefante' and cont == 3):
                print("===DICA===\nÉ um mamífero herbívoro que se destaca pelo seu tamanho, grandes presas e tromba muscular característica!")
            elif (palavra == 'pato' and cont == 3):
                print("===DICA===\nTem um pescoço longo e um bico que pode ser amarelo, laranja e até preto!")
            elif (palavra == 'cachorro' and cont == 3):
                print("===DICA===\nTemos o seu faro excepcional, a audição como um fator de maior sensibilidade do que os humanos, além dos dentes afiados!")
            elif (palavra == 'gato' and cont == 3):
                print("===DICA===\nEste animal conta com ouvidos e olfações bem aguçadas, unhas retráteis, visão noturna avantajada e um corpo bastante flexível!")
            elif (palavra == 'rato' and cont == 3):
                print("===DICA===\nFocinho afilado e a cauda comprida!")
            elif (palavra == 'girafa' and cont == 3):
                print("===DICA===\nÉ o animal mais alto do mundo!")

        print(des_forca[cont], end=' ')
        for i in range(0, len(palavra)):
            print('%c' % resp[i], end=' ')
        print("\nLETRAS CHUTADAS!!!")
        for i in range(0, len(letras)):
            print('',letras[i])
        chute = input('Digite uma letra ou a resposta: ')


        # USAR ESSE ESPAÇO PARA FAZER OS SWITCHS E DAR AS DICAS DE CADA ELEMENTO
        # lista = ['banana', 'abacaxi', 'pera', 'uva', 'carambola', 'laranja', 'melancia']
        # lista1 = ['corolla', 'fusca', 'camaro', 'uno', 'celta', 'subaru', 'supra']
        # lista2 = ['faca', 'colher', 'garfo', 'dado', 'cama', 'ventilador', 'panela']
        # lista3 = ['cavalo', 'elefante', 'pato', 'cachorro', 'gato', 'rato', 'girafa']



        chute = chute.lower()

        if len(chute) == 1:
            if chute not in letras:
                letras.append(chute)
                if chute in palavra:
                    for i in range(0,len(palavra)):
                        if palavra[i] == chute:
                            resp[i] = chute
                else:
                    cont = cont+1
            else:
                cont = cont + 1
        else:
            if chute == palavra:
                for i in range(0,len(palavra)):
                    resp[i] = chute[i]
            else:
                cont = cont+6


    if cont < 6:
        win = win + 1
        print("Parabéns você acertou!\nA palavra era: ", palavra.capitalize())
    else:
        print(des_forca[cont])
        loss = loss + 1
        print("Que pena você errou!\nA palavra era: ", palavra.capitalize())

    tipo = input("\nDeseja continuar(Digite 1) ou sair(Digite 2) \n")
    while(tipo != '1' and tipo != '2'):
        tipo = input("Digita 1 para continuar ou 2 para sair!!! \n")

if(fim == 1):
    if win > loss:
        print("Você foi muito bem e teve mais acerto do que derrotas! :)\nVitórias %d\nDerrotas %d\n"% (win,loss))
        print("Obrigado por jogar!!!")
    elif loss > win:
        print("Você teve desempenho baixo e acabou perdendo :(\nVitórias %d\nDerrotas %d\n"%(win,loss))
        print("Obrigado por jogar!!!")
    else:
        print("Você acabou tendo um empate :/\nVitórias %d\nDerrotas %d\n"%(win,loss))
        print("Obrigado por jogar!!!")