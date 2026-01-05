import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# LEFT SIDE: TF-IDF Concept
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.text(5, 9.5, 'TF-IDF: Smart Word Weighting', fontsize=16, fontweight='bold', ha='center')

# Example words with scores
words_scores = [
    ("the", 0.1, "Common, Low Value", '#FFE5E5'),
    ("a", 0.15, "Common, Low Value", '#FFE5E5'),
    ("python", 0.85, "Rare, High Value", '#E5FFE5'),
    ("bootcamp", 0.78, "Rare, High Value", '#E5FFE5'),
    ("complete", 0.72, "Descriptive, Medium-High", '#FFF5E6'),
]

y_start = 8
for i, (word, score, desc, color) in enumerate(words_scores):
    y_pos = y_start - i * 1.5
    
    # Word label
    ax1.text(1.5, y_pos, f'"{word}"', fontsize=12, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='black'))
    
    # Score bar
    bar_width = score * 4
    bar = Rectangle((3, y_pos - 0.25), bar_width, 0.5, 
                    facecolor=color, edgecolor='black', linewidth=2)
    ax1.add_patch(bar)
    ax1.text(3 + bar_width + 0.2, y_pos, f'{score:.2f}', 
            fontsize=11, va='center', fontweight='bold')
    
    # Description
    ax1.text(8.5, y_pos, desc, fontsize=9, va='center', style='italic')

# Formula box
formula_box = FancyBboxPatch((1, 0.5), 8, 1.5, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='blue', facecolor='#E5F5FF', linewidth=2)
ax1.add_patch(formula_box)
ax1.text(5, 1.7, 'TF-IDF = Term Frequency × Inverse Document Frequency', 
        fontsize=11, ha='center', fontweight='bold')
ax1.text(5, 1.2, '↑ More frequent in THIS doc', fontsize=9, ha='center')
ax1.text(5, 0.8, '↓ Less frequent ACROSS all docs = Higher Score', fontsize=9, ha='center')

# RIGHT SIDE: Matrix Visualization
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.text(5, 9.5, 'Text → Numbers: TF-IDF Matrix', fontsize=16, fontweight='bold', ha='center')

# Sample matrix
features = ['python', 'java', 'bootcamp', 'guide', 'complete']
courses = ['Course 1', 'Course 2', 'Course 3', 'Course 4']

# Create matrix visualization
matrix_data = np.array([
    [0.85, 0.00, 0.78, 0.00, 0.72],
    [0.00, 0.82, 0.00, 0.65, 0.70],
    [0.75, 0.00, 0.80, 0.55, 0.00],
    [0.00, 0.00, 0.00, 0.88, 0.75],
])

# Headers
header_y = 8.2
for i, feat in enumerate(features):
    x_pos = 2 + i * 1.3
    ax2.text(x_pos, header_y, feat, fontsize=9, ha='center', 
            rotation=25, fontweight='bold')

# Matrix cells
for row_idx, course in enumerate(courses):
    y_pos = 7.2 - row_idx * 1.2
    
    # Row label
    ax2.text(0.8, y_pos, course, fontsize=10, ha='right', fontweight='bold')
    
    for col_idx, value in enumerate(matrix_data[row_idx]):
        x_pos = 2 + col_idx * 1.3
        
        # Cell color based on value
        if value > 0.7:
            cell_color = '#E5FFE5'
        elif value > 0.4:
            cell_color = '#FFF5E6'
        elif value > 0:
            cell_color = '#FFE5E5'
        else:
            cell_color = '#F0F0F0'
        
        cell = Rectangle((x_pos - 0.5, y_pos - 0.4), 1, 0.8, 
                        facecolor=cell_color, edgecolor='black', linewidth=1.5)
        ax2.add_patch(cell)
        ax2.text(x_pos, y_pos, f'{value:.2f}' if value > 0 else '0', 
                fontsize=9, ha='center', va='center', fontweight='bold')

# Legend
legend_y = 2.5
ax2.text(5, legend_y + 0.5, 'Score Intensity', fontsize=11, ha='center', fontweight='bold')
colors = ['#E5FFE5', '#FFF5E6', '#FFE5E5', '#F0F0F0']
labels = ['High (>0.7)', 'Medium (0.4-0.7)', 'Low (>0)', 'Zero']
for i, (color, label) in enumerate(zip(colors, labels)):
    x_pos = 2.5 + i * 1.8
    box = Rectangle((x_pos - 0.3, legend_y - 0.3), 0.6, 0.6, 
                   facecolor=color, edgecolor='black', linewidth=1.5)
    ax2.add_patch(box)
    ax2.text(x_pos, legend_y - 0.8, label, fontsize=8, ha='center')

# Result box
result_box = FancyBboxPatch((1.5, 0.3), 7, 1, 
                           boxstyle="round,pad=0.1", 
                           edgecolor='green', facecolor='#E5FFE5', linewidth=2)
ax2.add_patch(result_box)
ax2.text(5, 0.9, '✓ Each course becomes a vector of 100+ keyword scores', 
        fontsize=10, ha='center', fontweight='bold')
ax2.text(5, 0.5, 'ML model uses these to predict subscriber count!', 
        fontsize=9, ha='center', style='italic')

plt.tight_layout()
plt.savefig('tfidf_vectorization.png', dpi=150, bbox_inches='tight')
print('✓ Saved: tfidf_vectorization.png')
