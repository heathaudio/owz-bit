def umpire():
    global UDrolled, ball, score, wicket
    UDrolled = umpiredie._pick_random()
    basic.show_string(UDrolled)
    if UDrolled == "not out":
        ball += 1
    elif UDrolled == "no ball":
        score = noballpenalty + score
    else:
        ball += 1
        wicket += 1

def on_button_pressed_a():
    bowl()
input.on_button_pressed(Button.A, on_button_pressed_a)

def gameendcheck():
    global over, ball
    if wicket == totalwicket:
        basic.show_string("All out")
        basic.show_string("" + str(score))
    elif ball == ballover:
        basic.show_string("End of Over " + ("" + str(over)))
        over += 1
        ball = 0
        if over == totalover:
            basic.show_string("End of Innings")
            basic.show_string("" + str(score))
def showscore():
    basic.show_string("S" + ("" + str(score)) + "/" + ("" + str(wicket)))

def on_button_pressed_ab():
    basic.show_string("" + str(over))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    showscore()
input.on_button_pressed(Button.B, on_button_pressed_b)

def bowl():
    global BDrolled, score, ball
    BDrolled = batterdie._pick_random()
    basic.show_string("" + str(BDrolled))
    if BDrolled != 0:
        score = BDrolled + score
        ball += 1
    else:
        umpire()
    gameendcheck()
batterdie: List[number] = []
BDrolled = 0
umpiredie: List[str] = []
UDrolled = ""
totalover = 0
ballover = 0
noballpenalty = 0
totalwicket = 0
wicket = 0
over = 0
ball = 0
score = 0
score = 0
ball = 0
over = 1
wicket = 0
totalwicket = 10
noballpenalty = 1
ballover = 5
totalover = 20

def on_forever():
    global batterdie, umpiredie
    batterdie = [0, 1, 2, 3, 4, 6]
    umpiredie = ["not out", "caught", "bowled", "no ball", "stumped", "lbw"]
basic.forever(on_forever)
