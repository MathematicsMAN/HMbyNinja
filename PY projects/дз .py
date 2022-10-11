# a = int(input(" Введите число 1 "))
# b = int(input(" Введите число 2 "))
# if a % 2 == 0:
#     a = str(a)
#     b = str(b)
#     print(a + b)
# elif   b % 2 == 0:
#     a = str(a)
#     b = str(b)
#     print(a + b)
#
# else:
#     print(a + b)

# a = int(input(" Введите число "))
# b = int(a ** 0.5)
# if a == b ** 2:
#     c = int((b + 1) ** 2)
#     print(c)
# else:
#     print(-1)

# sum = 1
# n = int(input(" Введите число "))
# for i in range(1,n):
#     sum /= i
# print(sum / n)

# sum = 0
# n = int(input(" Введите число "))
# for i in range(n):
#     sum += i
# print(sum + n)


# a = 0
# n = int(input(" Введите число "))
# b = 1 + n
# for i in range(1,b):
#     a += i ** i
# print(a)




# n = int(input(" Введите число n "))
# sum = 0
# for i in range(1,n + 1):
#     if i % 2 == 0:
#         sum -= i ** i
#     else:
#         sum += i ** i
# print(sum)





n = int(input(" Введите число n "))
sum = 1
i = 1
while sum < n:
    print(sum, end=' ')
    sum = 2 ** i
    i += 1
