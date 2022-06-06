# import random
# even = 0
# odd = 0
# for I in range(1000):
#     temp = random.randint(0, 1000)
#     if temp % 2 == 0:
#         even += 1
#
# even = even // 10
#
# print("Even: %d, odd: %d" % (even, odd))

a = int(input('enter a number: '))
res = list(map(int, str(a)))
maxi = max(res)
mini = min(res)
print(f"the maximun digit is {maxi}")
print(f"the minimum digit is {mini}")
# text = "Sanjar"
# text2 = text[::-1]
# print(text)
# print(text2)

# def fib (n):    # write Fibonacci series up to n
#     a, b = 0, 1
#     while a < n:
#         print(a)
#         a, b = b, a+b
#     print(fib(10))
# fib(10)