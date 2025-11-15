def rps(p1, p2):
    dominan = {
        "rock" : "scissors",
        "scissors" : "paper",
        "paper" : "rock"
    }
    if p1 == p2:
        return "Draw!"
    if p2 == dominan[p1]:
        return "Player 1 won!"
    if p1 == dominan[p2]:
        return "Player 2 won!"