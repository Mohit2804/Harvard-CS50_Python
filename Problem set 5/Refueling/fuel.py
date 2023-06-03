def main():
  fraction = input("Fraction: ")
  converted = convert(fraction)
  output = gauge(converted)
  print(output)

def convert(fraction):
  while True:
    X, Y = fraction.split("/")
    try:
      n_X = int(X)
      n_Y = int(Y)
      f = n_X / n_Y
      if f <= 1:
        percent = int(f * 100)
        return percent
      else:
        fraction = input("Fraction: ")
        pass
    except (ValueError,ZeroDivisionError):
      raise

def gauge(percentage):

  if percentage <= 1:
    return "E"
  elif percentage >= 99:
    return "F"
  else:
    return str(percentage) + "%"

if __name__ == "__main__":
    main()
