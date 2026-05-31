#Реклама в кино
# a = int(input())
# b = int(input())
# n = int(input())
#
# x = n//a
#
# if a*x == n:
#     x -= 1
#
# print(x*b + n)


#Детишки и качели

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# weights = [a,b,c]
# weight = max(weights)
# stone = abs(sum(weights) - weight * 2) - d
# if stone < 0:
#     stone = 0
# print(stone)

# import time
#
# N = int(input())
# A = int(input())
# X = int(input())
# B = int(input())
# Y = int(input())
#
# start = time.time()
# if N <= A*(2*X + 1) + B*(2*Y + 1):
#     if X >= Y:
#         i = 0
#         while i < N:
#             if A > 0:
#                 A -= 1
#                 i += X + 1
#                 print(min(i, N), X)
#                 i += X
#                 continue
#             if B > 0:
#                 B -= 1
#                 i += Y + 1
#                 print(min(i, N), Y)
#                 i += Y
#     else:
#         i = 0
#         while i < N:
#             if B > 0:
#                 B -= 1
#                 i += Y + 1
#                 print(min(i, N), Y)
#                 i += Y
#                 continue
#             if A > 0:
#                 A -= 1
#                 i += X + 1
#                 print(min(i, N), X)
#                 i += X
#
#
#
# else:
#     print(-1)
# end = time.time()
# print(end - start)

# from random import randint, seed
# seed(1)
# E = randint(1,10**2)
# N = randint(1,10)
#
# k = tuple(randint(-10, 10) for _ in range(N))
# print (E, N)
# print (k)
#
# ind = 0
# value = k[0] -1
#
# for i in range(N):
#     if E > i:

from random import randint

#


# N = int(input())
# M = int(input())
#
# massiv = [[int(input()) for _ in range (N)] for _ in range (M)]
# for x in range(N):
#     for y in range(M):
#         for i in range (N):
#             for j in range (M):
#                 if (massiv[x][y] + massiv[i][j]) % 10 == 0:
#                     print(massiv[x][y] + massiv[i][j])
# print(0)



# N = int(input())
# M = int(input())
#
# massiv = [[int(input()) for _ in range (N)] for _ in range (M)]

N, M = map(int, input().split())
massiv = tuple(tuple(map(int, input().split())) for _ in range(N))

x = int(input())
k = 1337
g = -1337

for i in range(N):
    for j in range(M):
        if x < massiv[i][j]:
            if k > massiv[i][j]:
                k = massiv[i][j]

for i in range(N):
    for j in range(M):
        if x > massiv[i][j]:
            if g < massiv[i][j]:
                g = massiv[i][j]

if k == 1337:
    print(-1)
else:
    print(k)
if g == - 1337:
    print(-1)
else:
    print(g)

'''
3 3
8 1 2
100 2 19
3 91 1
8
'''
