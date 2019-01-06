n = int(input())
lucky_number = [4, 7, 44, 77, 47, 74, 444, 447, 474, 477, 744, 747, 774, 777]
print("YNEOS"[all([n % i for i in lucky_number])::2])