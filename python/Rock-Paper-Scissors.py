# Game gunting-batu-kertas
def rps(p1, p2):
    # Dictionary yang menyimpan apa yang dikalahkan setiap pilihan
    dominan = {
        "rock" : "scissors",  # rock mengalahkan scissors
        "scissors" : "paper",  # scissors mengalahkan paper
        "paper" : "rock"  # paper mengalahkan rock
    }
    if p1 == p2:  # Jika pilihan sama
        return "Draw!"
    if p2 == dominan[p1]:  # Jika p1 mengalahkan p2
        return "Player 1 won!"
    if p1 == dominan[p2]:  # Jika p2 mengalahkan p1
        return "Player 2 won!"
