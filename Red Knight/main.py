def red_knight(N, P):
    return ("White", P*2) if (P-N) % 2 == 0 else ("Black", P*2)


print(red_knight(0, 8) == ('White', 16))
