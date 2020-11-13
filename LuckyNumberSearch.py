l, r = [int(i) for i in input().split()]

def lucky(number):
    digits = set(str(number))
    if '6' in digits and '8' in digits:
        return False
    if '6' in digits or '8' in digits:
        return True
    return False

y = []
ans = 0

for counter in range(l, r + 1):
    if '6' in set(str(counter)) or '8' in set(str(counter)):
        y.append(counter)
    else: pass

for k in y:
    ans += lucky(k)

print(ans)