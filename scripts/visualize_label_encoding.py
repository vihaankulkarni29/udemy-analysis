import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

# Create figure
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Label Encoding: Ordinal Data (Has Order)', 
        fontsize=18, fontweight='bold', ha='center')

# Ladder visualization
levels = ['All Levels', 'Beginner Level', 'Intermediate Level', 'Expert Level']
codes = [0, 1, 2, 3]
colors = ['#FFE5E5', '#FFE5CC', '#CCE5FF', '#CCFFCC']

for i, (level, code, color) in enumerate(zip(levels, codes, colors)):
    y_pos = 7 - i * 1.5
    
    # Level box
    box = FancyBboxPatch((0.5, y_pos - 0.5), 3.5, 0.9, 
                        boxstyle="round,pad=0.05", 
                        edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(2.25, y_pos, f'"{level}"', fontsize=11, ha='center', va='center')
    
    # Arrow
    if i < len(levels) - 1:
        arrow = FancyArrowPatch((2.25, y_pos - 0.6), (2.25, y_pos - 0.9),
                               arrowstyle='->', mutation_scale=20, linewidth=2, color='blue')
        ax.add_patch(arrow)
    
    # Encoding arrow
    arrow2 = FancyArrowPatch((4.2, y_pos), (5.3, y_pos),
                            arrowstyle='->', mutation_scale=25, linewidth=2.5, color='red')
    ax.add_patch(arrow2)
    
    # Encoded value
    code_box = FancyBboxPatch((5.5, y_pos - 0.4), 1.2, 0.8, 
                             boxstyle="round,pad=0.05", 
                             edgecolor='green', facecolor='#E5FFE5', linewidth=3)
    ax.add_patch(code_box)
    ax.text(6.1, y_pos, str(code), fontsize=16, ha='center', va='center', 
            fontweight='bold', family='monospace')

# Method box
method_box = FancyBboxPatch((7.2, 2), 2.5, 5.5, 
                           boxstyle="round,pad=0.1", 
                           edgecolor='purple', facecolor='#F5E6FF', linewidth=2)
ax.add_patch(method_box)
ax.text(8.45, 7, 'LabelEncoder', fontsize=13, ha='center', fontweight='bold', color='purple')
ax.text(8.45, 6.4, 'from sklearn', fontsize=9, ha='center', style='italic')
ax.text(8.45, 5.7, '✓ Preserves order', fontsize=10, ha='center')
ax.text(8.45, 5.2, '✓ Expert > Beginner', fontsize=10, ha='center')
ax.text(8.45, 4.7, '✓ Single column', fontsize=10, ha='center')
ax.text(8.45, 4.2, '✓ Memory efficient', fontsize=10, ha='center')
ax.text(8.45, 3.5, 'Use When:', fontsize=10, ha='center', fontweight='bold')
ax.text(8.45, 3, 'Data has natural', fontsize=9, ha='center')
ax.text(8.45, 2.6, 'ranking/hierarchy', fontsize=9, ha='center')

# Bottom explanation
ax.text(5, 0.7, 'WHY? The model learns that 3 (Expert) > 1 (Beginner) = Valid Math!', 
        fontsize=12, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7, pad=0.5))

plt.tight_layout()
plt.savefig('label_encoding.png', dpi=150, bbox_inches='tight')
print('✓ Saved: label_encoding.png')
