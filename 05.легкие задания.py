#1
#n = int(input())
# print(n + 1)
from pickletools import string1

#2
# n = int(input())
# a = int(input())
# print(n+a)

#3
# n = int(input())
# a = int(input())
# print(n*a)

#4
# n = int(input())
# print(n+1, n-1, n*2)

#5
# n = int(input())
# a = int(input())
# print(n*a, n*2 + a*2)

#6
# n = int(input())
# print(n*n)

#7
# n = int(input())
# print(n*n+5)

#8
# n = int(input())
# k = int(input()) + 1
# print(n//k)

#9
# n = int(input())
# print(n % 10, n % 100, n % 1000)

#10
# n = int(input())
# print(n%10)

#11
# n = int(input())
# print(n%10 + n//10)

#12
# n = int(input())
# a = n // 10
# print(a%10)

#13
# n = int(input())
# print((n%1000) // 100)

# #14
# n = int(input())
# a = n//100
# b = (n%100)//10
# c = n%10
# print(a*b*c)

#15
# n = int(input())
# a = int(input())
# b = int(input())
# print(n + a*b)

#16
# n = float(input())
# m = int(input())
# print(n-m)

# #17
# n1, n2, n3 = map(int, input().split())
# print((n1 + n2 + n3)/3)

#18
# N, M = map(float, input().split())
# k, j = map(int, input().split())
# a = N/k
# b = M/j
# print(a + b)

#19
# p = float(input())
# m = float(input())
# a = p/100
# print(m*a)

#20
# L = float(input())
# D = float(input())
# print((D*100)/L)

#21
# a, b, c = map(float, input().split())
# x = (a + b + c) / 3
# y = a - b - c
# z = a + b + c
# print((x-y)*z)

#22
# n = float(input())
# m = float(input())
# a = n*(m/100)
# print(n-a)

#23
# T = float(input())
# F = 9/5 * T + 32
# print(F)

#24
# Name = input()
# print("Hello,", Name)

#25
# word = input()
# print(3 * word)

#26
# word = input()
# print("t" + word + "bot")

#27
# country = input()
# city = input()
# number = input()
# print("+" + country + " (" + city + ") " + number)

#28
# numbers = int(input())
# n1 = str(numbers//10000)
# n2 = str(numbers//100 % 100)
# n3 = str(numbers % 100)
# print(n1 + "-" + n2 + "-" + n3)
# print(n1, n2, n3, sep="-")

#29
# free = input()
# a = int(input())
# z = 0
# for i in range(a):
#     z = (free + " ") * (i + 1)
#     print(z)
# print(free, free + " " + free, free + " " + free + " " + free, sep= "\n")

#30
# time = int(input())
# hours = time//3600
# minets = (time - (hours * 3600)) //60
# second = (time - (hours * 3600)) % 60
# if minets // 10 == 0:
#     minets = "0" + str(minets)
# if second // 10 == 0:
#     second = "0" + str(second)
# print(hours, minets, second, sep=':')

#31
# name = input()
# surname = input()
# city = input()
# job = input()
# print("****ANKETA****\nNAME: ", name, "\n", "SURNAME: ", surname, "\n", "****\n", "CITY: ", city, "\n", "JOB: ", job, "\n", "****", sep="")

#32
# x = input()
# y = input()
# print("https://", x, "/", y, sep="")

#33
# x = input()
# y = input()
# z = input()
#
# print('city: ', x, '\n', 'street: ', y, '\n', "house: ", z, sep="")

#34
# x = int(input())
# y = int(input())
# if x < y:
#     print("<")
# elif x > y:
#     print(">")
# else:
#     print("=")

#35
# r = int(input())
# n = int(input())
# m = int(input())
#
# if r * n <= m:
#     print(1)
# else:
#     print(0)

#36
# x1 = int(input())
# x2 = int(input())
# x3 = int(input())
# x4 = int(input())
# y = int(input())
#
# if x1 >= y and x2 >= y and x3 >= y and x4 >= y:
#     print("Happy")
# else:
#     print("Angry")

#37
# n = int(input())
# k = int(input())
# m = int(input())
# r = int(input())
#
# if m*r + k >= n:
#     print("1")
# else:
#     print("0")

#38
# x = input()
# y = input()
# kx = len(x)
# ky = len(y)
#
# if kx != 4 or ky != 4:
#     print("NO")
# else:
#     x = int(x)
#     y = int(y)
#
#     fx1 = x //1000
#     fx2 = x//100 %10
#     fx3 = x//10 %10
#     fx4 = x%10
#
#     fy1 = x //1000
#     fy2 = x//100 %10
#     fy3 = x//10 %10
#     fy4 = x%10
#
#     if fx1 + fx2 + fx3 + fx4 == fy1 + fy2 + fy3 + fy4:
#         print("YES")
#     else:
#         print("NO")

#39
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a < b + c and  c < b + a and b < c + a:
#     print("YES")
# else:
#     print("NO")

#40
# n = int(input())
# if n >= 14:
#     if n >= 30:
#         print("bad")
#     else:
#         print("good")
# elif n < 14:
#     print("great")

#41
# h = int(input())
# m = int(input())
# n = int(input())
# h = h * 60
# if h + m + n <= 480:
#     print(1)
# else:
#     print(0)

#42
# k = int(input())
# for z in range(1, k + 1):
#     print(z)
# print(k//2)
# print(k//2 + k % 2)

#43
# n = int(input())
# m = int(input())
# for i in range(n, m + 1):
#     if i % 52 == 0:
#         print(i)

#44
# A, B = map(int,input().split()) # Для считывания с одной строки!!!
# k = 0
# for i in range(A, B + 1):
#     if i % 5 != 0:
#         k += i
# print(k)

#45
# k = int(input())
# for z in range(1, k + 1):
#     print(z, z -1)

#46
# A, B = map(int,input().split())
# for i in range(A, B + 1):
#     if i % 2 == 0:
#         print("right")
#     if i % 5 == 0:
#         print("up")
#     if i % 7 == 0:
#         print("down")
#     if i % 9 == 0:
#         print("left")

#47
# n = int(input())
# k = ''
# for i in range(n):
#     simbol = input()
#     k += simbol
# print(k)

#48
# n = int(input())
# k = 0
# for i in range(n):
#     dish, time = input().split()
#     time = int(time)
#     k += time
#
# print(k)

#49
# n = int(input())
# maxk = 0
# mink = 10**6 + 1
# for i in range(n):
#     k = int(input())
#     if k > maxk:
#         maxk = k
#     if k < mink:
#         mink = k
# print(maxk - mink)

#50
# n, k = map(int,input().split())
# name = "Goroshek"
# a = 0
# for i in range(n):
#     names = input()
#     if a < k:
#         if names == name:
#             a += 1
#         else:
#             a = 0
# if a == k:
#     print("Yes")
# elif names == name:
#     print("Yes")
# elif a < k:
#     print("No")

#51
#n = int(input())
# k = 0
# chet = 0
# neChet = 0
# r = 0
# for i in range(1, n + 1):
#     a = int(input())
#     if i % 2 != 0:
#         neChet = a
#     elif i % 2 == 0:
#         chet = a
#     if neChet >= 1 and chet >= 1:
#         k = chet + neChet
#         print(k)
#     if k == a:
#         r += 1
#     else:
#         r -= (10**6)
# if r > 0:
#     print("Yes")
# else:
#     print("No")
#######
# a = int(input())
# b = int(input())
# result = 1
# for i in range(n - 2):
#     c = int(input())
#     if a + b != c:
#         result = 0
#     a = b
#     b = c
# if result == 1:
#     print("YES")
# else:
#     print("NO")

#52
# n = int(input())
# b = int(input())
# result = 1
# for i in range(n - 1):
#     c = int(input())
#     if b < c:
#         result = 0
#     b = c
# if result == 1:
#     print("YES")
# else:
#     print("NO")

#53
# n = int(input())
# k = 0
# while n % 2 == 0:
#     n = n / 2
#     k += 1
# print(k)

#54
# n, x = map(int,input().split())
# i = 0
# while x < n:
#     x = x + i
#     i += 1
# print(i)

#55
# n = int(input())
# k = 0
# while n % 2 == 0:
#     n = n / 2
#     k += 1
# if k == 0:
#     print("NO")
# else:
#     print(k)

#56
# n = int(input())
# b = int(input())
# k = 0
# for i in range(n - 1):
#     a = int(input())
#     if a < b:
#         k += 1
#     b = a
# print(k)

#57
# n = int(input())
# k = 0
# for i in range(n):
#     a = int(input())
#     if a % 10 == 0:
#         k += a
#     else:
#         k += a % 10
# print(k)

#58
# n = int(input())
# a = input()
# b = input()
# k = 0
# for i in range(n-2):
#     c = input()
#     if c != a and c != b:
#         k += 1
# print(k)

#59
# n, x = map(int,input().split())
# k = 1
# i = 1
# while n >= k:
#     print(k, end=" ")
#     k = x**i
#     i += 1

#60
# n = int(input())
# k = 0
# d = 2**k
# while d < n:
#     k += 1
#     d = 2**k
# print(k)

#61
# n = int(input())
# k = 0
# i = 1
# while i < n:
#     if n % i == 0:
#         k = i
#     i += 1
# print(k)

#62
# n = int(input())
#
# k = 0
# while n % 2 == 0:
#     k += 1
#     n = n / 2
#
# g = 0
# while n % 3 == 0:
#     g += 1
#     n = n / 3
#
# print(k, g)

#63
# k = 0
# a = int(input())
#
# while a != 0:
#     if a % 3 == 0:
#         k += 1
#     a = int(input())
# print(k)

#64
# p = int(input())
# d = p % 10
# a = int(input())
# while a != 0:
#     s = a % 10
#     if s == d:
#         print("CLOSE")
#     if a == p:
#         print("WELCOME")
#         break
#     a = int(input())
# else:
#     print("NO ATTEMPTS")

#65
# k = 0
# a, b = 0, 1
# while a != b :
#     a, b = map(int, input().split())
#     if a + b >= 8:
#         k += 1
# print(k)

#66
# k = 0
# a = int(input())
# s = a
# n = 0
# while a != 0:
#     n += 1
#     if s / n == 4:
#         k += 1
#     a = int(input())
#     s += a
# if k == 0:
#     print(s//n)
# else:
#     print(n)

#67
# n = int(input())
# i = 0
# k = 0
# while n != 3**i :
#     if n < 3**i:
#         k += 1
#         break
#     i += 1
# if k == 0:
#     print("YES")
# else:
#     print("NO")

#68
# k, n = map(int,input().split())
# g = 0
# if k % 6 == 0:
#     g += 1
# else:
#     print("NO")
# i = 0
# while n >= k:
#     if g == 0:
#         break
#     k += i
#     if i == 2:
#         i = 3
#     else:
#         i = 2
# if k % 6 == 0:
#     print(k)

#69
# n = int(input())
# k = 0
# while n // 10 != 0:
#     if n % 10 == 0:
#         k += 1
#     n //= 10
# print(k)

#70
# n = int(input())
# k = 0
# g = 0
# while n > 0:
#     if n % 10 == 3:
#         k += 1
#     if n % 10 == 9:
#         g += 1
#     n //= 10
#
# if g >= 1 and k >= 1:
#     print("double")
# elif k >= 1:
#     print("three")
# elif g >= 1:
#     print("nine")
# else:
#     print("zero")

#71
# n, k = map(int,input().split())
# f = -1
# while n > 0:
#     if k == n % 10:
#         f = 0
#     if f > -1:
#         f += 1
#     n //= 10
# print(f)

#72
# n = int(input())
# k = int(input())
# g = 1
# while n > 0:
#     if n % 10 > k:
#         g *= n % 10
#     n //= 10
# if g == 1:
#     print(0)
# else:
#     print(g)

#73
# n = int(input())
# f = n
# k = 0
#
# while n > 0:
#     k = k * 10 + n % 10
#     n //= 10
# print(k)
# if f == k:
#     print("YES")
# else:
#     print("NO")

#74
# n = int(input())
# k = 0
# while n > 0:
#     if n // 10 == 0:
#         print(n)
#     k = (n % 100) // 10
#     if k != n % 10 and k != 0:
#         print("NO")
#         break
#     n //= 10

#75
# n, k = map(int,input().split())
# g = n
# f = 0
# while g > 0:
#     f += g % 10
#     g //= 10
# if f < k:
#     count = ((k - f + 9 - 1)//9)
#     print(n, end="")
#     for i in range(count):
#         print(9, end="")
# else:
#     print(n)

#76
# n = int(input())
# p = 1
#
# for i in range(2,n + 1):
#     p *= 1/i
# print(p)

#77
# n = int(input())
# summ = 0
# for i in range(1, n + 1):
#     summ += (-1)**(i - 1) * 1/i
# print(round(summ, 2))

#78
# n = int(input())
# s = 0
# d = 1
#
# for i in range(1, n + 1):
#     d = i*d
#     s += 1/d
# print(s)

#79
# n = int(input())
# s = 1
# k = 0
#
# for i in range(2, n + 1):
#     k += i * s
#     s += i**2
# print(k)

#80
#n = int(input())
# s = list(map(int,input().split()))
#
# for i in range(n):
#     if i % 2 == 0:
#         print(s[i])

#81
# n = int(input())
# s = list(map(int,input().split()))
# k = 0
#
# for i in range(n):
#     if s[i] % 10 == 2:
#         print(s[i], end=" ")
#         k += 1
# print()
# print(k)

#82
# n = int(input())
# s = list(map(int,input().split()))
# k = 0
#
# for i in range(n):
#     if i % 2 == 0 and s[i] % 2 != 0:
#         k += 1
#         print(s[i], end=" ")
#
# if k == 0:
#     print("no stars today")

#83
# n = int(input())
# s = list(map(int,input().split()))
# m = int(input())
# k1 = 0
# k2 = 0
#
# for i in range(n):
#     if m == s[i]:
#         k1 += 1
#     if m - 1 == s[i]:
#         k2 += 1
#
# print(k1, k2)

#84
# n = int(input())
# s = list(map(int,input().split()))
# x = int(input())
#
# for i in range(n - 1, n - x - 1, -1):
#     print(s[i], end=" ")

#85
# n = int(input())
# s = list(map(int,input().split()))
#
# for i in range(len(s)//2, len(s)):
#     k = s[i]
#     print(k, end=' ')
# for i in range(len(s)//2):
#     print(s[i], end=" ")

#86
# n = int(input())
# s = list(map(int,input().split()))
#
# for i in range(len(s)):
#     if s[i] > 0:
#         print(s[i], end=' ')
# for i in range(len(s)):
#     if s[i] < 0:
#         print(s[i], end=" ")

#87
# n = int(input())
# s = list(map(int,input().split()))
# a, b = map(int,input().split())
#
# for i in range(len(s)):
#     if s[i] < a:
#         print(s[i]*2, end=" ")
#     elif s[i] > b:
#         print(s[i]//2, end=" ")
#     else:
#         print(s[i] + 1, end=" ")

#88
# n = int(input())
# s = list(map(int,input().split()))
#
# for i in range(len(s)):
#     print(s[i]//(i + 1), end=' ')

#89
# n = int(input())
# s = list(map(int,input().split()))
# maxim = -1
# maximum = 0
#
# for i in range(len(s)):
#     if maxim < s[i]:
#         maxim = s[i]
#         maximum = 0
#     if maxim == s[i]:
#         maximum += 1
# print(maximum)

#90
# a = input()
#
# print(ord(a))

#91
# a = int(input())
#
# print(chr(a))

#92
# k = input()
# a = ord(k)
#
# if 65 <= a <= 90 or 97 <= a <= 122:
#     print("YES")
# else:
#     print("NO")

#93
# a = ord(input())
# b = ord(input())
#
# print(abs(a-b))

#94
# place = ord(input())
# r = int(input())
#
# for i in range(place - r, place + r + 1):
#     if  65 <= i <= 90:
#         print(chr(i), end=" ")

#95
# a = ord(input())
# b = ord(input())
#
# for i in range(65, 91):
#     if i < a or i > b:
#         print(chr(i), end=" ")

#96
# a, b = input().split()
# a = ord(a)
# b = int(b)
#
# if a + b >= 97 and a + b <= 122:
#     print("lvlup", chr(a + b))
# elif 65 <= a + b <= 90:
#     print("same", chr(a + b))
# else:
#     print("out of range")

#97
# n = int(input())
# s = list(map(int,input().split()))
# k = sum(s)
#
# for i in range(n):
#
#     if k // n > s[i]:
#         print('+', end="")
#     print(k // n - s[i], end=" ")

#98
# n = int(input())
# s = []
# hight = -1
# low = 10**5 + 1
# s = list(map(int, input().split()))
#
# for i in range(n):
#
#     if s[i] < low:
#         low = s[i]
#         lowindex = i + 1
#
#     if s[i] > hight or hight == s[i]:
#         hight = s[i]
#         hightindex = i + 1
#
# print(lowindex, hightindex)

#99
# s = list(map(int, input().split()))
# k = 0
# result = True
#
# for i in range(7):
#     if s[i] != 0:
#         if k == 0:
#             k = s[i]
#         elif k * s[i] > 0:
#             result = False
#
# if result:
#     print("YES")
# else:
#     print("NO")

#100!!!!!!!!!!
# n = int(input())
# c = input()
# s = input()
# k = 0
#
# for i in range(len(s)):
#     if s[i] == c:
#         print(i + 1, end=" ")
#         k += 1
#
# if k == 0:
#     print(0)

#101
# n = int(input())
# s = input()
#
# if s[:n] == s[-n:]:
#     print("YES")
# else:
#     print("NO")

#102
# n = int(input())
# s = input()
#
# print(s.replace(" ", "_"))

#103
# s = int(input())
# print(chr(s + 64))

#104
# a, b = map(str, input().split())
# a, b = ord(a), ord(b)
#
# k = (a + b)//2
# print(chr(k))

#105
# a = input()
# b = input()
# a, b = ord(a), ord(b)
# k = b - a
# s = ""
#
# if k <= 0:
#     print("ERROR")
# else:
#     for i in range(k + 1):
#         s += chr(a + i)
#
# print(s)
# с юбилеем!!!)

#106
# b = ord(input())
# a, c = chr(b - 1), chr(b + 1)
# a1, c1 = b - 1, b + 1
#
# z, x = chr(97 + 26 - (a1 - 96)), chr(97 + 26 - (c1 - 96))
#
# print(a, c)
# print(z, x)

#Текстовый файл
#107
# with open("input.txt") as file:
#     text = file.read()
#     s = text.split()
#
# with open("output.txt", "w") as file:
#     for i in range(len(s)):
#         file.write(s[i][:1] + " ")

#108 <----
# k = 0
# with open("input.txt") as file:
#     s = file.readlines()
#
#     with open("output.txt", "w") as file:
#         for i in range(len(s)):
#             if "0" in s[i]:
#                 k += 1
#         k = str(k)
#         file.write(k)

#109
# k = ""
# with open("input.txt") as file:
#     text = file.read()
#     s = text.split()
#
#     with open("output.txt", "w") as file:
#         file.write(''.join(s))

#110
# h, w = map(int, input().split())
# def rectangle(h, w):
#     for i in range(h):
#         if h - 1 == i or i == 0:
#             print("* " * w)
#         else:
#             print("* " + "  "*(w-2) + "*")
# rectangle (h, w)


#111
# n = int(input())
# d = n//2
# def romb(n) :
#     for i in range(d):
#         print("  "*(d - i) + "* "*(2*i + 1))
#     print(d*"* " + "  " + d*"* ")
#     for i in range(d - 1, -1, -1):
#         print("  "*(d - i) + "* "*(2*i + 1))
#romb (n)

#112 <----
# n = int(input())
# d = n//2
# def square(n):
#     print("*" * n)
#     for i in range((n-2)//2):
#         print(("*" + " "*i + "*") + (" "*(n-4-2*i) + "*") + " "*i + "*")
#     if n % 2 != 0:
#         print(("*" + " " * ((n-3)//2) + "*") + " "*((n-3)//2) + "*")
#     for i in range((n-2)//2):
#         print(("*" + " "*(n-2-i) + "*") + (" "*(2*i-n) + "*") + " "*(n-i-2) + "*") # <---- переписать
#     print("*" * n)
# square(n)

#113
# h, w = map(int, input().split())
# def snake(h, w):
#     count = 1
#     v = w - 1
#     for i in range(h):
#         if i == 0:
#             print(":" + "0"*(v))
#         elif i % 2 == 0:
#             print("0" * w)
#         else:
#             if count % 2 == 0:
#                 print("0")
#                 count += 1
#             else:
#                 print(" " * v + "0")
#                 count += 1
# snake(h, w)

#114
# h = int(input())
# def two_triangle(h) :
#     for i in range(1, h):
#         print("*"*i + " "*(2*h - 2*i) + "*"*i)
#     print("*"*(2*h))
#     for i in range(h-1,-1,-1):
#         print("*"*i + " "*(2*h - 2*i) + "*"*i)
#
# two_triangle(h)

#115
# n = int(input())
# d = n//2
# def square(n):
#     for i in range(n):
#         if n - 1 == i or i == 0:
#             print("*" * 2 *n + "*")
#         else:
#             print(("*" + " "*(n - i - 2) + "*") + " "*i + "*" + " "*i + "*" + " "*(n - i - 2) + "*")
# square(n)

#Процедура(функция которая ничего не возвращает)

#116
# a, b = map(int, input().split())
#
# def digital(a, b):
#     while b % a == 0:
#         b = b // a
#     if b == 1:
#         print("YES")
#     else:
#         print("NO")
#
# digital(a, b)

#117
# a, b = map(int, input().split())
#
# def digital(a, b):
#     s = [6, 28, 496, 8128]
#     for i in range(len(s)):
#         if a < s[i] < b:
#             print(s[i], end=" ")
# digital(a, b)

#118
# n = input()
# slovar = "aeyuioAEUIOY"
#
# def sting(n):
#     for i in range(len(n)):
#         if n[i] in slovar:
#             print(n[i], end="")
#     for i in range(len(n)):
#         if n[i] not in slovar:
#             print(n[i], end="")
# sting(n)

#119
# n = input()
# slovar = "abcdefghijklmnopqrstuvwxyz"
# def sting(n):
#     result = []
#     for i in range(len(n)):
#         if n[i].lower() in slovar and n[i].lower() not in result:
#             result.append(n[i])
#     if len(result) == 26:
#         print("YES")
#     else:
#         print("NO")
# sting(n)

#120
# t = int(input())
#
# def time(t):
#     k = 0
#     while t >= 1:
#         k += t
#         t = t//2
#     print(k)
# time(t)


#Сортировка

#121
# n = int(input())
# s = list(map(int, input().split()))
# s.sort()
#
# print(s[(len(s)//2)])

#122
# n = int(input())
# s = []
#
# for i in range(1, n+1):
#     a = input()
#     s.append(a)
#
# s.sort()
#
# for i in range(n):
#     print(str(i + 1) + ". " + s[i])

#123
# n = int(input())
# s = []
# result = []
#
# for i in range(1, n+1):
#     a = input()
#     s.append(a)
#
# s.sort(reverse=True)
# for i in range(n - 1):
#     if s[i] != s[i + 1] and s[i] != s[i - 1]:
#         result.append(s[i])
# if s[n-1] != s[n-2]:
#     result.append(s[n-1])
# print(*result) # -----> * - распаковка

#124     !!!Доделать!!!
# n = int(input())
# k = int(input())
# m = int(input())
# s = list(map(int, input().split()))
#
# for i in range(0, n-1, k):
#     if m in s[i:i+k]:
#         print(i//k + 1)
#         break

#125
# n = input()
# k = 0
#
# for i in range(len(n)-1):
#     if abs(int(n[i]) - int(n[i + 1])) == 1:
#         k += 1
# print(k)

#126
# n = input()
# numbers_sum = 0
# result = 0
#
# for i in range(len(n)):
#     numbers_sum += int(n[i])
#
# numbers_sum = str(numbers_sum)
# for i in range(len(numbers_sum)):
#     if numbers_sum[i] not in n:
#         result += 1
#         break
# if result >= 1:
#     print("NO")
# else:
#     print("YES")

#127w21dewfcfre
# n = input()
# hight = 1
# lowght = 1
#
# for i in range(len(n) - 1):
#     if n[i] > n[i+1]:
#         hight = 0
#     if n[i] < n[i+1]:
#         lowght = 0
#
# if hight == 1 or lowght == 1 :
#     print('YES')
# else:
#     print("NO")

#128
# n = input()
# k = 0
# g = 0
#
# for i in range(6):
#     if i >= 3:
#         k += int(n[i])
#     else:
#         g += int(n[i])
# if k == g:
#     print("HAPPY")
# else:
#     print("SAD")

#129
# f = int(input())
# n = input()
# n = n.replace(" ", "")
# k = 0
#
# for i in range(f):
#      for j in range(i+1, f):
#          if n[i] == n[j]:
#              k += 1
# print(k)

#130
# n = int(input())
# s = []
# k = []
#
# for _ in range(n):
#     c = list(map(int, input().split()))
#     s.append(c)
#
# for _ in range(n):
#     u = list(map(int, input().split()))
#     k.append(u)
#
# for i in range(n):
#     for j in range(n):
#         print(s[i][j] + k[i][j], end=" ")
#     print()

#131
# a, b = map(int, input().split())
# s = []
#
# for i in range(a, b+1):
#     k = 0
#     while i > 0:
#         k += i%10
#         i //= 10
#     s.append(k)
#
# result = []
#
# for i in s:
#     result.append(s.count(i))
#
# print(max(result))

#132
# n = int(input())
#
# for i in range(1, n+1):
#     c = []
#     for j in range(1, n + 1):
#         f = i * j
#         c.append(str(i) + "*" + str(j) + "=" + str(f))
#     for i in range(len(c)):
#         print(str(c[i]), end=" ")
#     print()

#133
# n, m = map(int, input().split())
# x = int(input())
# s = []
# f = 0
#
# for i in range(n):
#     c = list(map(int, input().split()))
#     s.append(c)
#
# for i in range(n):
#     if f == 1:
#         break
#     for j in range(m):
#         if s[i][j] == x:
#             print(i, j)
#             f += 1
#             break
# if f == 0:
#     print("Not found")

#134
# n, m = map(int, input().split())
# s = []
# summ = 0
#
# for i in range(n):
#     c = list(map(int, input().split()))
#     s.append(c)
#
# for i in range(n):
#     for j in range(m):
#         summ += s[i][j]
# print(summ)

#135
# n, m = map(int, input().split())
# s = []
#
# for i in range(n):
#     c = list(map(int, input().split()))
#     s.append(c)
#
# i, j = map(int, input().split())
# summJ = 0
# summI = 0
#
# for x in range(n):
#     summJ += s[x][j-1]
# for y in range(m):
#     summI += s[i-1][y]
#
# if summJ > summI:
#     print("column")
# elif summI > summJ:
#     print("row")
# else:
#     print("draw")

#136
# n, m = map(int, input().split())
# s = []
#
# for i in range(1, n+1):
#     c = []
#     for j in range(1, m+1):
#         c.append(j*i)
#     print(*c)

#137
# n, m = map(int, input().split())
# s = []
#
# for i in range(n):
#     c = list(map(int, input().split()))
#     s.append(c)
#
# for i in range(n):
#     f = ''
#     for j in range(m):
#         if s[i][j] % 2 == 0:
#             s[i][j] = '0'
#         f += str(s[i][j]) + " "
#     print(f)

#138
# n, m = map(int, input().split())
# s = []
# summ1 = 0
# summ2 = 0
#
# for i in range(n):
#     c = list(map(int, input().split()))
#     s.append(c)
#
# for i in range(n//2):
#     for j in range(m):
#         summ1 += s[i][j]
#
# for i in range(n//2, n):
#     for j in range(m):
#         summ2 += s[i][j]
#
# if summ1 > summ2:
#     print(1)
#
# elif summ1 < summ2:
#     print(2)
#
# else:
#     print(0)

#139
n = int(input())
s = []

d1 = []
d2 = []

for i in range(n):
    c = list(map(int, input().split()))
    s.append(c)

for i in range(n):
    d1.append(s[i][i])
    d2.append(s[i][n - 1 - i])

print(*d1)
print(*d2)



















