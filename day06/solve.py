f = open('input.txt')

questions = {}

q_count = 0

for line in f.readlines() + ['\n']:
    if line == '\n':
        # done with current
        q_count += len(questions)
        questions = {}

    else:
        for a in line.strip():
            if a in questions:
                questions[a] += 1
            else:
                questions[a] = 1

print(q_count)


