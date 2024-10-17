import sys

N = sys.stdin.readline()
lsum = 0
rsum = 0
for i in range(int(len(N) / 2)):
    lsum += int(N[i])
    rsum += int(N[i + int(len(N) / 2)])
if lsum == rsum:
    print("LUCKY")
else:
    print("READY")