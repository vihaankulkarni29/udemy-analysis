import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Feature Fusion: Numerical + Text Data', 
        fontsize=18, fontweight='bold', ha='center')

# LEFT: Numerical Features
num_box = FancyBboxPatch((0.5, 5), 3.5, 3.5, 
                        boxstyle="round,pad=0.1", 
                        edgecolor='blue', facecolor='#E5F5FF', linewidth=3)
ax.add_patch(num_box)
ax.text(2.25, 8.2, 'Numerical Features', fontsize=13, ha='center', fontweight='bold', color='darkblue')

num_features = ['price', 'num_reviews', 'num_lectures', 'year', 'month', 'level_encoded']
for i, feat in enumerate(num_features):
    y_pos = 7.6 - i * 0.4
    ax.text(2.25, y_pos, f'• {feat}', fontsize=10, ha='center')

ax.text(2.25, 5.3, 'Shape: (3672, 6)', fontsize=9, ha='center', 
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='blue'))

# RIGHT: Text Features (TF-IDF)
text_box = FancyBboxPatch((6, 5), 3.5, 3.5, 
                         boxstyle="round,pad=0.1", 
                         edgecolor='green', facecolor='#E5FFE5', linewidth=3)
ax.add_patch(text_box)
ax.text(7.75, 8.2, 'Text Features (TF-IDF)', fontsize=13, ha='center', fontweight='bold', color='darkgreen')

text_features = ['txt_0 (python)', 'txt_1 (bootcamp)', 'txt_2 (complete)', '...', 'txt_99 (guide)']
for i, feat in enumerate(text_features):
    y_pos = 7.6 - i * 0.4
    ax.text(7.75, y_pos, f'• {feat}', fontsize=10, ha='center')

ax.text(7.75, 5.3, 'Shape: (3672, 100)', fontsize=9, ha='center', 
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='green'))

# CENTER: Merge operation
merge_circle = plt.Circle((5, 6.75), 0.6, color='orange', ec='black', linewidth=3, zorder=10)
ax.add_patch(merge_circle)
ax.text(5, 6.75, 'concat', fontsize=12, ha='center', va='center', fontweight='bold', zorder=11)

# Arrows
arrow1 = FancyArrowPatch((4.2, 6.75), (4.4, 6.75),
                        arrowstyle='->', mutation_scale=25, linewidth=3, color='blue')
ax.add_patch(arrow1)

arrow2 = FancyArrowPatch((5.8, 6.75), (5.6, 6.75),
                        arrowstyle='->', mutation_scale=25, linewidth=3, color='green')
ax.add_patch(arrow2)

# BOTTOM: Combined Dataset
combined_box = FancyBboxPatch((1.5, 1.5), 7, 2.5, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='purple', facecolor='#F5E6FF', linewidth=3)
ax.add_patch(combined_box)
ax.text(5, 3.7, 'Combined "Super-Dataset"', fontsize=14, ha='center', fontweight='bold', color='purple')

combined_features = ['price', 'reviews', 'lectures', 'year', 'month', 'level_enc', 
                    'txt_0', 'txt_1', '...', 'txt_99']
feature_text = ' | '.join(combined_features)
ax.text(5, 3.2, feature_text, fontsize=9, ha='center', family='monospace')

ax.text(5, 2.7, 'Shape: (3672, 106)', fontsize=11, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

ax.text(5, 2.2, 'Physical Stats (price, date) + Psychological Stats (keywords)', 
        fontsize=10, ha='center', style='italic')

ax.text(5, 1.8, '= Complete feature set for ML model training!', 
        fontsize=10, ha='center', fontweight='bold')

# Arrow down
arrow_down = FancyArrowPatch((5, 4.8), (5, 4.1),
                            arrowstyle='->', mutation_scale=30, linewidth=3, color='purple')
ax.add_patch(arrow_down)

# Code snippet
code_box = FancyBboxPatch((0.5, 0.2), 9, 0.9, 
                         boxstyle="round,pad=0.05", 
                         edgecolor='black', facecolor='#F0F0F0', linewidth=2)
ax.add_patch(code_box)
ax.text(5, 0.65, 'Code: pd.concat([numerical_df, text_df], axis=1)', 
        fontsize=11, ha='center', family='monospace', fontweight='bold')

plt.tight_layout()
plt.savefig('feature_fusion.png', dpi=150, bbox_inches='tight')
print('✓ Saved: feature_fusion.png')
