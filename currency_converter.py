rates = {
    'uah':  1.00,
    'usd': 24.33,
    'eur': 26.44,
    'rub':  0.32,
    'gbp': 34.83,
    'chf': 23.51,
    'cad': 16.41,
    'pln':  5.73
}

def main():
  uin = input('>>> ').split()
  if len(uin) != 4:
    print("too many or too few arguments")
  else:
    try:
      cash = float(uin[0])
    except ValueError:
      print("wrond amount of cash")
    else:
      if uin[1] == uin[3]:
        print("<<< {0:.2f} {1}".format(cash, uin[3]))
      elif (uin[1] in rates and 
            uin[3] in rates):
        uah_rate = rates[uin[1]]
        rate     = rates[uin[3]]
        cash     = cash*uah_rate/rate
        print("<<< {0:.2f} {1}".format(cash, uin[3]))
      else:
        print("can\'t find such rate")

if __name__ == '__main__':
  print("\n\t\tCurrency converter")
  print("Enter your expression in format: \'25 usd to uah\'")
  print("Available currencies:", " ".join(rates.keys()))
  answer = "y"
  while answer != "n":
    main()
    answer = input(">>> continue? (y/n) ")