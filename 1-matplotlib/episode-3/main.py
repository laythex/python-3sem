import matplotlib.pyplot as plt

with open('students.csv') as file:
    data = [list(entry.split(';')) for entry in file.readlines()]

marks = list(range(3, 11))

preps = sorted(list(set([entry[0] for entry in data])))
groups = sorted(list(set([entry[1] for entry in data])))
marks_per_prep = []
marks_per_group = []

fig, axs = plt.subplots(2, 4, figsize=(12, 8))

for i in range(len(preps)):
    cur_marks = [int(entry[2]) for entry in data if entry[0] == preps[i]]
    marks_per_prep.append(sum(cur_marks) / len(cur_marks))
    cur_marks = [[cur_marks.count(mark), mark] for mark in marks]

    sizes, labels = zip(*[cur_mark for cur_mark in cur_marks if cur_mark[0] > 0])
    axs[i // 4][i % 4].pie(sizes, labels=labels)
    axs[i // 4][i % 4].set_title(preps[i])

axs[1][3].axis('off')

fig.suptitle('Marks per prep')

plt.savefig('episode-3a.png')
plt.show()

fig, axs = plt.subplots(2, 3, figsize=(12, 8))

for i in range(len(groups)):
    cur_marks = [int(entry[2]) for entry in data if entry[1] == groups[i]]
    marks_per_group.append(sum(cur_marks) / len(cur_marks))
    cur_marks = [[cur_marks.count(mark), mark] for mark in marks]

    sizes, labels = zip(*[cur_mark for cur_mark in cur_marks if cur_mark[0] > 0])
    axs[i // 3][i % 3].pie(sizes, labels=labels)
    axs[i // 3][i % 3].set_title(groups[i])

fig.suptitle('Marks per group')

plt.savefig('episode-3b.png')
plt.show()

print(f'Самый халявный преп: {preps[marks_per_prep.index(max(marks_per_prep))]}')
print(f'Самая раздолбайская группа: {groups[marks_per_group.index(min(marks_per_group))]}')
