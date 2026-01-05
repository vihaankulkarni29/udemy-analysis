import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9, 'Date Conversion: String → Integer', 
        fontsize=18, fontweight='bold', ha='center')

# Before box
before_box = FancyBboxPatch((0.5, 5), 3, 2.5, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='red', facecolor='#FFE5E5', linewidth=3)
ax.add_patch(before_box)
ax.text(2, 7, 'BEFORE', fontsize=14, fontweight='bold', ha='center', color='darkred')
ax.text(2, 6.5, 'Data Type: String', fontsize=11, ha='center')
ax.text(2, 6, '"2017-01-15"', fontsize=13, ha='center', family='monospace', 
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='black'))

# Arrow
arrow = FancyArrowPatch((3.7, 6.25), (6.3, 6.25),
                       arrowstyle='->', mutation_scale=30, linewidth=3, color='blue')
ax.add_patch(arrow)
ax.text(5, 6.7, 'pd.to_datetime()', fontsize=11, ha='center', 
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# After box
after_box = FancyBboxPatch((6.5, 5), 3, 2.5, 
                           boxstyle="round,pad=0.1", 
                           edgecolor='green', facecolor='#E5FFE5', linewidth=3)
ax.add_patch(after_box)
ax.text(8, 7, 'AFTER', fontsize=14, fontweight='bold', ha='center', color='darkgreen')
ax.text(8, 6.5, 'Data Type: Integer', fontsize=11, ha='center')
ax.text(8, 6, '2017', fontsize=13, ha='center', family='monospace',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='black'))

# Bottom section - extraction
extract_box = FancyBboxPatch((1, 1.5), 8, 2.5, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='purple', facecolor='#F0E5FF', linewidth=2)
ax.add_patch(extract_box)
ax.text(5, 3.5, 'Feature Extraction from Date', fontsize=13, fontweight='bold', ha='center')
ax.text(5, 2.9, 'df["year"] = df["published_timestamp"].dt.year', 
        fontsize=10, ha='center', family='monospace')
ax.text(5, 2.4, 'df["month"] = df["published_timestamp"].dt.month', 
        fontsize=10, ha='center', family='monospace')
ax.text(5, 1.9, '→ Creates numeric features the ML model can use', 
        fontsize=10, ha='center', style='italic')

# Why box
why_text = 'WHY? ML models need numbers, not text!'
ax.text(5, 0.5, why_text, fontsize=12, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='orange', alpha=0.6, pad=0.5))

plt.tight_layout()
plt.savefig('date_conversion.png', dpi=150, bbox_inches='tight')
print('✓ Saved: date_conversion.png')
