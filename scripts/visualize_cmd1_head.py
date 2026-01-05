import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

df = pd.read_csv('udemy_courses.csv')

fig, ax = plt.subplots(figsize=(14, 6))
ax.axis('off')

# Title
ax.text(0.5, 0.95, 'Command 1: df.head() - First 5 Rows', 
        ha='center', fontsize=14, fontweight='bold', transform=ax.transAxes)

# Create table visualization
head_data = df.head()
cell_text = []
for idx, row in head_data.iterrows():
    cell_text.append([
        row['course_title'][:25] + '...' if len(str(row['course_title'])) > 25 else row['course_title'],
        row['subject'],
        row['level'],
        f"${row['price']}"
    ])

columns = ['course_title', 'subject', 'level', 'price']
table = ax.table(cellText=cell_text, colLabels=columns, loc='center',
                cellLoc='left', colWidths=[0.4, 0.2, 0.2, 0.15])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2)

# Style header
for i in range(len(columns)):
    table[(0, i)].set_facecolor('#3498db')
    table[(0, i)].set_text_props(weight='bold', color='white')

# Command box
ax.text(0.5, 0.05, 'Command: df = pd.read_csv("udemy_courses.csv"); df.head()', 
        ha='center', fontsize=10, transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='#ecf0f1', edgecolor='black'))

plt.tight_layout()
plt.savefig('cmd1_head.png', dpi=150, bbox_inches='tight')
print('✓ Saved: cmd1_head.png')
