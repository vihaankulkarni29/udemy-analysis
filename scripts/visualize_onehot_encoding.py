import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'One-Hot Encoding: Nominal Data (No Order)', 
        fontsize=18, fontweight='bold', ha='center')

# Original column
subjects = ['Web Development', 'Business Finance', 'Musical Instruments', 'Graphic Design']
colors_orig = ['#FFE5E5', '#E5F5FF', '#FFF5E5', '#E5FFE5']

ax.text(1.5, 8.5, 'Original Column', fontsize=12, ha='center', fontweight='bold')
for i, (subj, color) in enumerate(zip(subjects, colors_orig)):
    y_pos = 7.5 - i * 0.9
    box = FancyBboxPatch((0.2, y_pos - 0.35), 2.6, 0.7, 
                        boxstyle="round,pad=0.05", 
                        edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(1.5, y_pos, subj, fontsize=9, ha='center', va='center')

# Arrow
arrow = FancyArrowPatch((3, 6), (4.5, 6),
                       arrowstyle='->', mutation_scale=30, linewidth=3, color='blue')
ax.add_patch(arrow)
ax.text(3.75, 6.5, 'get_dummies()', fontsize=11, ha='center', 
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# One-hot encoded columns
encoded_cols = ['subject_Business Finance', 'subject_Graphic Design', 'subject_Musical Instruments']
ax.text(7, 8.5, 'After One-Hot Encoding', fontsize=12, ha='center', fontweight='bold')

# Header row
header_y = 7.7
for i, col in enumerate(encoded_cols):
    x_pos = 5 + i * 1.6
    ax.text(x_pos, header_y, col.replace('subject_', ''), fontsize=7, ha='center', 
            rotation=15, fontweight='bold')

# Data rows - show binary values
data_rows = [
    [0, 0, 0],  # Web Dev (dropped as reference)
    [1, 0, 0],  # Business Finance
    [0, 0, 1],  # Musical Instruments
    [0, 1, 0],  # Graphic Design
]

for row_idx, values in enumerate(data_rows):
    y_pos = 7 - row_idx * 0.9
    for col_idx, val in enumerate(values):
        x_pos = 5 + col_idx * 1.6
        cell_color = '#E5FFE5' if val == 1 else '#FFE5E5'
        box = FancyBboxPatch((x_pos - 0.25, y_pos - 0.35), 0.5, 0.7, 
                            boxstyle="round,pad=0.02", 
                            edgecolor='black', facecolor=cell_color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x_pos, y_pos, str(val), fontsize=12, ha='center', va='center', 
                fontweight='bold', family='monospace')

# Why box
why_box = FancyBboxPatch((0.5, 0.5), 9, 2, 
                        boxstyle="round,pad=0.1", 
                        edgecolor='purple', facecolor='#F5E6FF', linewidth=2)
ax.add_patch(why_box)
ax.text(5, 2, 'WHY One-Hot Encoding?', fontsize=13, ha='center', fontweight='bold', color='purple')
ax.text(5, 1.5, '✗ NO natural order: "Music" is NOT > "Business"', fontsize=10, ha='center')
ax.text(5, 1.1, '✓ Binary columns prevent mathematical bias (each gets 0 or 1)', fontsize=10, ha='center')
ax.text(5, 0.7, '✓ Model treats each subject independently', fontsize=10, ha='center')

# Note about drop_first
ax.text(5, 3.2, 'Note: "Web Development" is dropped (drop_first=True) to avoid multicollinearity', 
        fontsize=9, ha='center', style='italic',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('onehot_encoding.png', dpi=150, bbox_inches='tight')
print('✓ Saved: onehot_encoding.png')
