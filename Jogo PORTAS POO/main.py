import time
import os
import random 

while True: #looping para o jogador entender a lógica
    print("")
    print("Bem-Vindo ao jogo das portas")
    time.sleep(1)
    print("""
Esse jogo funciona da seguinte forma:
Haverão perguntas sobre conecimento gerais. 
Na sua frente, terão 3 portas, cada uma com uma resposta. 
Basta digitar 1, 2 ou 3 para escolher a porta com a resposta certa.
""")

    pergunta = int(input("Voce entendeu? 1- sim 2-nao: "))
   
    if pergunta == 2:
        os.system('cls')
        
    else: #exemplo da porta
        print("Otimo, a porta sera nesse estilo:")
        time.sleep(2)
        os.system('cls')
        print("""
         __________________
        |                  |
        |                  |
        |     EXEMPLO      |
        |                  |
        |       ____       |
        |      |    |      |
        |      |    |      |
        |      |    |      |
        |      |    |      |
        |      |    |      |
        |      |    |    o |
        |______|____|______|
        
        """)
        break

time.sleep(2)
os.system('cls')

print("Então. Vamos as Perguntas!!")
time.sleep(1)

dicionario_perguntas = {  #dicionario, onde a chave é a pergunta, e no valor, possui uma lista com as alternativas.
"Qual a Capital do Brasil?" : ["brasilia" , "Campo grande" , "sao paulo" ],
"Qual o melhor carro existente? " : ["mustang", "camaro" , "civic"],
"Qual o melhor poder? " : ["gelo", "fogo" , "agua"] 
}

def portas(numero, respostas):  #função para mostrar as portas, baseando no modelo la em cima. Colocando o numero (indice) e respostas (valor do dicionario)
    return f"""
         __________________
        |                  |
        |   porta {numero} |
        |                  |
        |    {respostas}   |
        |       ____       |
        |      |    |      |
        |      |    |      |
        |      |    |      |
        |      |    |      |
        |      |    |      |
        |      |    |    o |
        |______|____|______|  
"""

def criar_pergunta(dicionario, ultima_pergunta=False):          #função para criar as perguntas das portas e sortear aleatoriamente.
    pergunta_sorteada = random.choice(list(dicionario.keys()))
    respostas = dicionario[pergunta_sorteada]
    resposta_correta = dicionario[pergunta_sorteada][0]
    random.shuffle(respostas)

    if not ultima_pergunta:
        print("Proxima pergunta....")
        time.sleep(2)

    print(f"A pergunta é: {pergunta_sorteada}")

    for i, resposta in enumerate(respostas, 1):
        print(portas(i, resposta))

    try:
        escolha = int(input("Digite o numero da porta correta: "))
        if respostas[escolha - 1] == resposta_correta:
            time.sleep(2)
            print("Parabens, voce acertou")
            time.sleep(1)
            os.system('cls')
            if ultima_pergunta:
                print("E com isso, chegou ao final do nosso desafio. Parabens!!!")
                print("""           (\__/)
            (•ㅅ•) 
          ＿ノヽ ノ＼＿
        `/　`/ ⌒Ｙ⌒ Ｙ  ヽ
       ( 　(三ヽ人　 /　  |
       |　ﾉ⌒＼ ￣￣ヽ   ノ
         ヽ＿＿＿＞､＿_／
            ｜( 王 ﾉ〈   
             /ﾐ`ー―彡\  
            / ╰    ╯ \ /    
         \     /---\     /
        |    |      |    |
        |    |      |    |
        |    |      |    |
        |    |      |    |
        |    |      |    |
        |    |      |    |
        |    |      |    |
        |    |      |    |
          👠        👠""")
        else:
            if ultima_pergunta:
                print("Porta errada, começe do 0 HAHAHAHAHAHAHAHA")
            else:
                print("Porta errada")
    except:
        print("Digite uma opção valida: 1, 2 ou 3")

    dicionario.pop(pergunta_sorteada)
    return dicionario

# Primeira pergunta
dicionario_perguntas = criar_pergunta(dicionario_perguntas)

# Segunda pergunta
dicionario_perguntas = criar_pergunta(dicionario_perguntas)

# Terceira pergunta
criar_pergunta(dicionario_perguntas, True)