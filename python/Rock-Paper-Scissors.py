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


## Best Practices ##
# 1.
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

# 2.
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

# 3. 
def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
        