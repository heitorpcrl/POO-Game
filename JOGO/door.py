class Door:
    def __init__(self, number, answer):
        self.number = number
        self.answer = answer

    def display(self):
        return f"""
         __________________
        |                  |
        |   porta {self.number} |
        |                  |
        |    {self.answer}   |
        |       ____       |
        |      |    |      |
        |      |    |      |
        |      |    |      |
        |      |    |      |
        |      |    |      |
        |      |    |    o |
        |______|____|______|
"""