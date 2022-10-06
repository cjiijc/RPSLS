N = 50000

from RPSLS_game import RPSLS_game

from P10387 import P10387
from P99999 import P99999


game = RPSLS_game(P10387, P99999)
for i in range(1, N+1):
    print(f"[Round {i}]")
    game.proceed_match()

print(game.get_score()) 