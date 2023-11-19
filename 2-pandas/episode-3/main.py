import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

students = pd.read_excel(os.path.join('students', 'students_info.xlsx'))
results = pd.read_html(os.path.join('students', 'results_ejudge.html'))[0]
merged = students.merge(results, left_on='login', right_on='User')

_, axs = plt.subplots(1, 2, figsize=(10, 5))

plt.sca(axs[0])
merged.groupby('group_faculty')['Solved'].mean().plot.bar()
plt.sca(axs[1])
merged.groupby('group_out')['Solved'].mean().plot.bar()


axs[0].grid()
axs[1].grid()
axs[0].set_axisbelow(True)
axs[1].set_axisbelow(True)
axs[0].set_xlabel('faculty group')
axs[1].set_xlabel('out group')
axs[0].set_ylabel('solved')
axs[1].set_ylabel('solved')
axs[0].set_title('Mean solved by faculty group')
axs[1].set_title('Mean solved by out group')

plt.savefig('mean-solved.png')

top = merged[(merged['G'] >= 10) | (merged['H'] >= 10)]

_, axs = plt.subplots(1, 2, figsize=(10, 5))
plt.sca(axs[0])
top['group_faculty'].value_counts().plot.pie(ylabel='')
plt.sca(axs[1])
top['group_out'].value_counts().plot.pie(ylabel='')

axs[0].set_title('Faculty groups top students came from')
axs[1].set_title('Out groups top students went to')

plt.savefig('top-groups.png')

plt.show()
