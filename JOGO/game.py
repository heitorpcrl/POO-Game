import os
import time
import random

from JOGO.door import Door
from JOGO.question_manager import QuestionManager


class Game:
    def __init__(self):
        self.questions = {
            "Qual a Capital do Brasil?": ["brasilia", "Campo grande", "sao paulo"],
            "Qual o melhor carro existente?": ["mustang", "camaro", "civic"],
            "Qual o melhor poder?": ["gelo", "fogo", "agua"]
        }
        self.question_manager = QuestionManager(self.questions)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_intro(self):
        print("Bem-Vindo ao jogo das portas")
        time.sleep(1)
        print("""
Esse jogo funciona da seguinte forma:
Haverão perguntas sobre conhecimento gerais.
Na sua frente, terão 3 portas, cada uma com uma resposta.
Basta digitar 1, 2 ou 3 para escolher a porta com a resposta certa.
""")
        while True:
            try:
                understood = int(input("Você entendeu? 1- sim 2- não: "))
                if understood == 1:
                    break
                else:
                    self.clear_screen()
            except ValueError:
                print("Digite uma opção válida: 1 ou 2")

    def ask_question(self, question, answers, is_last=False):
        random.shuffle(answers)
        correct_answer = answers[0]

        print(f"A pergunta é: {question}")
        for i, answer in enumerate(answers, 1):
            door = Door(i, answer)
            print(door.display())

        try:
            choice = int(input("Digite o número da porta correta: "))
            if answers[choice - 1] == correct_answer:
                print("Parabéns, você acertou!")
                time.sleep(1)
                self.clear_screen()
                if is_last:
                    print("E com isso, chegou ao final do nosso desafio. Parabéns!!!")
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
                print("Porta errada!")
        except (ValueError, IndexError):
            print("Digite uma opção válida: 1, 2 ou 3")

    def start(self):
        self.display_intro()
        for i in range(3):
            question, answers = self.question_manager.get_random_question()
            self.ask_question(question, answers, is_last=(i == 2))
