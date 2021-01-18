def main():
  print("Keep it logically awesome.\n")

  f = open("quotes.txt",'r',encoding='utf-8')
  quotes = f.readlines()
  f.close()

  print(quotes[0])
  print(quotes[-1])

if __name__== "__main__":
  main()
