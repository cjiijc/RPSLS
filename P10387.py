from RPSLS_player import RPSLS_player
import random


class P10387(RPSLS_player):
  def __init__(self):
    pass

  def shoot(self):
    MyScore = [0, 0]
    if self._result == "win":
        MyScore[0] += 1
    elif self._result == "lose":
        MyScore[1] += 1
    else: 
        pass
    
    a = "spock"

    
    if MyScore[0] - MyScore[1] < -3 :
        ShootList = ["rock", "paper", "scissors", "lizard", "spock"]
        a = random.choice(ShootList)
        return a 
    
    elif MyScore[0] - MyScore[1] == 0: 
        if self._result == "win":
            WinSpock = ["paper", "lizard"]
            a = random.choice(WinSpock)  
        else:
            ElseSpock = ["spock", "rock"]
            a = random.choice(ElseSpock)  
        return a
    
    else: 
        if self._result == "win":
            a = self._competitor_shot
        elif self._result == "draw":
            DrawSpock = ["paper", "rock"]
            a = random.choice(DrawSpock)
        else: 
            a = "lizard"
        return a 

      
  def update(self, result: str, competitor_shot: str):
    self._result = result
    self._competitor_shot = competitor_shot