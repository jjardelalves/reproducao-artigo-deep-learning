import matplotlib.pyplot as plt
import re

caminho_do_arquivo = 'logs_3a.txt'  

with open(caminho_do_arquivo, 'r', encoding='utf-8') as f:
    log_data = f.read()

iters, losses, test_accs, ic_accs, ic2_accs, iw_accs = [], [], [], [], [], []

pattern = re.compile(
    r"Iter \(x1000\): (\d+) Test loss: ([\d\.]+) Test acc: ([\d\.]+) IC acc: ([\d\.]+) IC2 acc: ([\d\.]+) IW acc: ([\d\.]+)"
)

for line in log_data.strip().split("\n"):
    match = pattern.search(line)
    if match:
        iters.append(int(match.group(1)) * 2)  
        losses.append(float(match.group(2)))
        test_accs.append(float(match.group(3)))
        ic_accs.append(float(match.group(4)))
        ic2_accs.append(float(match.group(5)))
        iw_accs.append(float(match.group(6)))

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Graph 1: Test Loss
ax1.plot(iters, losses, color='#2b2b2b', linewidth=2, label='Test Loss')
ax1.set_ylabel('Loss', fontsize=12, fontweight='bold')
ax1.set_ylim(-0.1, 3.8)
ax1.legend(loc='upper right', frameon=True)
ax1.grid(True, linestyle='--', alpha=0.6)

# Graph 2: Accuracies
# ax2.plot(iters, test_accs, color='black', linewidth=2, label='Test acc')
ax2.plot(iters, ic_accs, color='tab:red', linewidth=2, label='IC acc')
# ax2.plot(iters, ic2_accs, color='tab:green', linewidth=2, label='IC2 acc')
# ax2.plot(iters, iw_accs, color='tab:blue', linewidth=2, label='IW acc')

ax2.set_xlabel('Iterations (x500)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Accuracy', fontsize=12, fontweight='bold')
ax2.set_ylim(-0.05, 1.05)
ax2.legend(loc='center right', frameon=True)
ax2.grid(True, linestyle='--', alpha=0.6)

# plt.suptitle('Reprodução Figura 3b: Transição Abrupta no In-Context Learning', fontsize=14, fontweight='bold')
plt.tight_layout()

# Salvar e Exibir
plt.savefig('figura_3a.png', dpi=300)
plt.show()