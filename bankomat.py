def bankomat(n):
   moneys = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
   d = len(str(n))
   reversed_n = reversed(str(n))
   count = 1
   l = []
   result = ''
   for i in reversed_n:
      wholes = int(i) * count
      l.append(wholes)
      count *= 10
      count = 0
   while n != 0:
      if n // moneys[count] > 0:  # 12 521 yes -->2
         a = n // moneys[count]  # 2
         b = moneys[count]  # 5000
         n -= a * b
         result += a * (str(b) + " ")
      count += 1
   return result

i = int(input('money: '))
print(bankomat(i))