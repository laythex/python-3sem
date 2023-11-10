import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

students = pd.read_excel(os.path.join('students', 'students_info.xlsx'))
results = pd.read_html(os.path.join('students', 'results_ejudge.html'))[0]

merged = students.merge(results, left_on='login', right_on='User')
group_fac = merged.groupby('group_faculty')
fac_names, fac_mean_solved = list(map(str, group_fac.groups.keys())), group_fac['Solved'].mean()
group_out = merged.groupby('group_out')
out_names, out_mean_solved = list(map(str, group_out.groups.keys())), group_out['Solved'].mean()

_, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].grid()
axs[1].grid()
axs[0].set_axisbelow(True)
axs[1].set_axisbelow(True)
axs[0].bar(fac_names, fac_mean_solved)
axs[1].bar(out_names, out_mean_solved)
axs[0].set_xlabel('group')
axs[1].set_xlabel('group')
axs[0].set_ylabel('solved')
axs[1].set_ylabel('solved')
axs[0].set_title('Mean solved by faculty group')
axs[1].set_title('Mean solved by out group')

plt.savefig('mean-solved.png')

top = merged[(merged['G'] >= 10) | (merged['H'] >= 10)]

_, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].pie(**dict(zip(['labels', 'x'], np.unique(np.array(top['group_faculty']), return_counts=True))))
axs[1].pie(**dict(zip(['labels', 'x'], np.unique(np.array(top['group_out']), return_counts=True))))

axs[0].set_title('Faculty groups top students came from')
axs[1].set_title('Out groups top students went to')

plt.savefig('top-groups.png')

plt.show()
