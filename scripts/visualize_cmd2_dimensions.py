import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('udemy_courses.csv')

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

# Title
ax.text(0.5, 0.9, 'Command 2: Dataset Dimensions & Columns', 
        ha='center', fontsize=14, fontweight='bold', transform=ax.transAxes)

# Stats box
stats_text = f"Total Courses: {len(df)}\nTotal Columns: {len(df.columns)}"
ax.text(0.5, 0.75, stats_text, ha='center', fontsize=12, fontweight='bold',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='#3498db', edgecolor='black', alpha=0.8),
        color='white')

# Column list
columns_text = "Columns:\n" + "\n".join([f"  {i+1}. {col}" for i, col in enumerate(df.columns)])
ax.text(0.5, 0.45, columns_text, ha='center', fontsize=10, family='monospace',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='#ecf0f1', edgecolor='black'))

# Command box
cmd_text = "Command: print('Total Courses:', len(df))\n         print('Total Columns:', len(df.columns))\n         print('Columns:', list(df.columns))"
ax.text(0.5, 0.05, cmd_text, ha='center', fontsize=9, family='monospace',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='#f39c12', edgecolor='black', alpha=0.8))

plt.tight_layout()
plt.savefig('cmd2_dimensions.png', dpi=150, bbox_inches='tight')
print('✓ Saved: cmd2_dimensions.png')
