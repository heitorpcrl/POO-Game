import os
import time
import random

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_pista(posicao_carro, comprimento=20):
    pista = ['-'] * comprimento
    pista[posicao_carro] = '🚗'
    return ''.join(pista)

def main():
    posicao = 0
    comprimento_pista = 30
    pontos = 0
    velocidade = 0.5
    
    print("Bem-vindo à Corrida Terminal!")
    print("Use 'a' para ir para esquerda e 'd' para direita")
    print("Pressione Enter para começar...")
    input()
    
    while True:
        limpar_tela()
        
        # Mostra a pista e o carro
        print("\n" * 3)
        print(f"Pontos: {pontos}")
        print(criar_pista(posicao, comprimento_pista))
        
        # Gera obstáculos aleatórios
        if random.random() < 0.3:
            if posicao > 0:
                posicao -= 1
        
        # Recebe input do jogador
        try:
            import msvcrt
            if msvcrt.kbhit():
                tecla = msvcrt.getch().decode().lower()
                if tecla == 'a' and posicao > 0:
                    posicao -= 1
                elif tecla == 'd' and posicao < comprimento_pista - 1:
                    posicao += 1
        except:
            # Para sistemas que não são Windows
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                tecla = sys.stdin.read(1).lower()
                if tecla == 'a' and posicao > 0:
                    posicao -= 1
                elif tecla == 'd' and posicao < comprimento_pista - 1:
                    posicao += 1
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        pontos += 1
        time.sleep(velocidade)

if __name__ == "__main__":
    main()



