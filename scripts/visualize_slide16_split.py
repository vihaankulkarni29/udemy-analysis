import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))

sizes = [80, 20]
labels = ['Training (80%)', 'Testing (20%)']
colors = ['#3498db', '#e67e22']

ax.pie(sizes, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90,
       wedgeprops=dict(edgecolor='white', linewidth=2))
ax.set_title('Slide 16: Train/Test Split', fontsize=16, fontweight='bold')

# Why we split
ax.text(0, -1.2, 'Why split?\nHold out data tests if model learns vs memorizes.',
        ha='center', va='top', fontsize=12, bbox=dict(boxstyle='round', facecolor='#ecf0f1', edgecolor='black'))

# Seed 42 note
ax.text(1.3, 1.1, 'Seed = 42\nReproducible every run',
        ha='right', va='top', fontsize=12, bbox=dict(boxstyle='round', facecolor='#dff9fb', edgecolor='black'))

plt.tight_layout()
plt.savefig('slide16_split.png', dpi=150)
print('✓ Saved: slide16_split.png')
