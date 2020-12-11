f = open('input.txt')

questions = {}

q_count = 0
p_count = 0

for line in f.readlines() + ['\n']:
    if line == '\n':
        # done with current
        for count in questions.values():
            if count == p_count:
                q_count += 1
        questions = {}
        p_count = 0

    else:
        p_count += 1
        for a in line.strip():
            if a in questions:
                questions[a] += 1
            else:
                questions[a] = 1

print(q_count)


