def pi():
    terms = eval(input("how many terms in the series?: "))
    sum = 0
    for i in range(terms):
      sum = ((i - 1) % 2 + i) * ((i +1) % 2 + i)
    print(sum)