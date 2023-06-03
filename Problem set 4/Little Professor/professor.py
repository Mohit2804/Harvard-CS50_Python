import random

def main():
     level = get_level()
     score = simulate_game(level)
     print("Score: ", score)

def get_level():
  while True:
    try:
      level = int(input("Level: "))
      if level in [1,2,3]:
        break
    except:
      pass
  return level

def generate_integer(level):
  if level == 1:
    x = random.randint(0, 9)
    y = random.randint(0, 9)
  elif level == 2:
    x = random.randint(10, 99)
    y = random.randint(10, 99)
  else:
    x = random.randint(100, 999)
    y = random.randint(100, 999)
  return x, y

def game_try(x, y):
  cnt_tries = 1
  while cnt_tries <= 3:
    try:
      ans = int(input(f"{x} + {y} = "))
      if ans == (x + y):
        return True
      else:
        cnt_tries += 1
        print("EEE")
    except:
      cnt_tries += 1
      print("EEE")
  print(f"{x} + {y} = {x+y}")
  return False

def simulate_game(level):
  cnt_round = 1
  score = 0
  while cnt_round <= 10:
    x, y = generate_integer(level)
    reply = game_try(x, y)
    if reply == True:
      score += 1
    cnt_round += 1
  return score

if __name__ == "__main__":
    main()
