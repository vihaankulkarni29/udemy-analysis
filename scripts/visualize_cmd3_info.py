import pandas as pd
import matplotlib.pyplot as plt
import io

df = pd.read_csv('udemy_courses.csv')

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')

# Title
ax.text(0.5, 0.95, 'Command 3: df.info() - Dataset Information', 
        ha='center', fontsize=14, fontweight='bold', transform=ax.transAxes)

# Capture df.info() output
buffer = io.StringIO()
df.info(buf=buffer)
info_text = buffer.getvalue()

# Display info text
ax.text(0.5, 0.5, info_text, ha='center', va='center', fontsize=9, family='monospace',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='#ecf0f1', edgecolor='black'))

# Highlight key insight
insight_text = "Key: Shows data types, non-null counts, and memory usage"
ax.text(0.5, 0.08, insight_text, ha='center', fontsize=10, fontweight='bold',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='#2ecc71', edgecolor='black', alpha=0.8),
        color='white')

# Command box
ax.text(0.5, 0.02, 'Command: df.info()', ha='center', fontsize=10, family='monospace',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='#f39c12', edgecolor='black', alpha=0.8))

plt.tight_layout()
plt.savefig('cmd3_info.png', dpi=150, bbox_inches='tight')
print('✓ Saved: cmd3_info.png')
