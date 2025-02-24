import sys

answers = []

while True:

    answer = 0
    triangles = []
    for i in range(6):
        triangles.append(list(map(int, sys.stdin.readline().split())))


    def f(triangles, left, right, v):
        if not triangles and left == right:
            global answer
            answer = max(answer, v)
        for i in triangles:
            for j in range(3):
                if left == i[j]:
                    new_triangles = triangles[:]
                    new_triangles.remove(i)
                    f(new_triangles, i[(j - 1) % 3], right, v + i[(j + 1) % 3])
                if right == i[j]:
                    new_triangles = triangles[:]
                    new_triangles.remove(i)
                    f(new_triangles, left, i[(j + 1) % 3], v + i[(j - 1) % 3])
    for i in triangles:
        for j in range(3):
            new_triangles = triangles[:]
            new_triangles.remove(i)
            f(new_triangles, i[j], i[(j + 1) % 3], i[(j + 2) % 3])
    
    if answer == 0:
        answers.append('none')
    else:
        answers.append(answer)

    if sys.stdin.readline().split()[0] == '$':
        break

for answer in answers:
    print(answer)