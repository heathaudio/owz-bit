function umpire () {
    UDrolled = umpiredie._pickRandom()
    basic.showString(UDrolled)
    if (UDrolled == "not out") {
        ball += 1
    } else if (UDrolled == "no ball") {
        score = noballpenalty + score
    } else {
        ball += 1
        wicket += 1
    }
}
input.onButtonPressed(Button.A, function () {
    bowl()
})
function gameendcheck () {
    if (wicket == totalwicket) {
        basic.showString("All out")
        basic.showString("" + score)
    } else if (ball == ballover) {
        basic.showString("End of Over " + ("" + over))
        over += 1
        ball = 0
        if (over == totalover) {
            basic.showString("End of Innings")
            basic.showString("" + score)
        }
    }
}
function showscore () {
    basic.showString("S" + ("" + score) + "/" + ("" + wicket))
}
input.onButtonPressed(Button.AB, function () {
    basic.showString("" + over)
})
input.onButtonPressed(Button.B, function () {
    showscore()
})
function bowl () {
    BDrolled = batterdie._pickRandom()
    basic.showString("" + BDrolled)
    if (BDrolled != 0) {
        score = BDrolled + score
        ball += 1
    } else {
        umpire()
    }
    gameendcheck()
}
let batterdie: number[] = []
let BDrolled = 0
let umpiredie: string[] = []
let UDrolled = ""
let totalover = 0
let ballover = 0
let noballpenalty = 0
let totalwicket = 0
let wicket = 0
let over = 0
let ball = 0
let score = 0
score = 0
ball = 0
over = 1
wicket = 0
totalwicket = 10
noballpenalty = 1
ballover = 5
totalover = 20
basic.forever(function () {
    batterdie = [
    0,
    1,
    2,
    3,
    4,
    6
    ]
    umpiredie = [
    "not out",
    "caught",
    "bowled",
    "no ball",
    "stumped",
    "lbw"
    ]
})
