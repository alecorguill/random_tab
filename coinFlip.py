import random as r;

def userChoice(p):
    return (r.random() > p)

def bankChoice():
    return (r.random() > 0.5)


def coinFlip(nb_round):
    bankPoint = 0
    userPoint = 0
    for i in range(nb_round):
        bankRes = bankChoice()
        userRes = userChoice(0.5)
        if (userRes == bankRes):
            userPoint += 1
        else:
            bankPoint += 1
    return bankPoint,userPoint


print(coinFlip(50))
