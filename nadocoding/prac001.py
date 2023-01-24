# 신조어 퀴즈 클래스를 만드시오
class Word:
    def __init__(self, word, ex1, ex2, 정답):
        self.word = word
        self.ex1 = ex1
        self.ex2 = ex2
        self.정답 = 정답

    def show_question(self):
        print(f"{self.word}의 뜻은?\n1.{self.ex1}\n2.{self.ex2}")

    def check_answer(self, answer):
        if self.정답 == answer:
            print("정답입니다.")
        else:
            print("틀렸습니다.")


word = Word('"얼죽아"', "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer(int(input("=>")))
