from math import *
from manimlib import *

class Word2Vec(Scene):
    def construct(self):
        king = Vector([1, 0, 0])
        man = Vector([0, 1, 0])
        # (1, 1) + (0, 1) - (1, 0) = (0, 2)
        woman = Arrow([3, 0, 0], [3, 1, 0], buff=0)
        queen = Arrow([3, 0, 0], [3 + 1, 0, 0], buff=0)

        king_text = Text("king", font_size=15)
        man_text = Text("man", font_size=15)
        always(king_text.next_to, king, RIGHT)
        always(man_text.next_to, man, UP)
        self.play(ShowCreation(king), ShowCreation(king_text))
        self.play(ShowCreation(man), ShowCreation(man_text))

        woman_text = Text("woman", font_size=15)
        queen_text = Text("queen", font_size=15)

        always(queen_text.next_to, queen, RIGHT)
        always(woman_text.next_to, woman, UP)
        self.play(ShowCreation(woman), ShowCreation(woman_text))
        self.play(ShowCreation(queen), ShowCreation(queen_text))

        self.wait()
        delta = Arrow(start=[1, 0, 0], end=[0, 1, 0], color='#FF0000', fill_opacity=0.1)
        delta.set_color(RED)
        self.play(ShowCreation(delta))

        self.wait()
        # self.embed()


        # self.play(ReplacementTransform(square, circle))
        # self.wait()

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
