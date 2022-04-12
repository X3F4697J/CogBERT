from matplotlib import pyplot as plt
import pandas as pd

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax2 = ax1.twinx()
lns1 = ax1.plot(range(1, 13), sst_12layers, color='lightcoral', marker='o', linestyle='dashed', label='SST2')
lns2 = ax1.plot(range(1, 13), mrpc_12layers, color='darkgreen', marker='v', linestyle='dashed', label='MRPC')
lns3 = ax1.plot(range(1, 13), qnli_12layers, color='fuchsia', marker='^', linestyle='dashed', label='QNLI')
lns4 = ax1.plot(range(1, 13), stsb_12layers, color='steelblue', marker='*', linestyle='dashed', label='STS-B')
#lns4 = ax2.plot(range(1, 13), Geco_12layers, color='steelblue', marker='*', linestyle='dashed', label='Geco(EN)')
lns = lns1+lns2+lns3+lns4
labs = [l.get_label() for l in lns]
ax1.set_xlabel('Layer')
ax1.set_ylabel('Performances of NLP tasks', fontsize=13)
#ax2.set_ylabel('Performance of Eye-tracking prediction', fontsize=13)
ax1.legend(loc='lower left')
ax1.legend(lns, labs, loc='lower left')
ax1.grid()
ax1.set_title('Performances across layers')
fig.tight_layout()
plt.savefig('layer_study_no_Geco.pdf', bbox_inches='tight')
plt.show()
