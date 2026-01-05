import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Create figure
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.7, 'Data Transformation: Raw → ML-Ready', 
        fontsize=20, fontweight='bold', ha='center')

# LEFT SIDE: Raw Data
left_box = FancyBboxPatch((0.3, 3), 3.8, 5.5, 
                         boxstyle="round,pad=0.1", 
                         edgecolor='red', facecolor='#FFE5E5', linewidth=3)
ax.add_patch(left_box)
ax.text(2.2, 8.2, 'RAW DATA', fontsize=14, ha='center', fontweight='bold', color='darkred')
ax.text(2.2, 7.8, '(Human Readable)', fontsize=10, ha='center', style='italic')

# Raw data sample
raw_data = [
    ('Title:', '"Ultimate Java Course"'),
    ('Subject:', '"Business Finance"'),
    ('Level:', '"Beginner Level"'),
    ('Date:', '"2017-07-05"'),
    ('Price:', '$50'),
    ('Reviews:', '250'),
]

y_start = 7.2
for i, (label, value) in enumerate(raw_data):
    y_pos = y_start - i * 0.7
    ax.text(0.7, y_pos, label, fontsize=10, ha='left', fontweight='bold')
    ax.text(2.5, y_pos, value, fontsize=10, ha='left', family='monospace',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

# Problems box
problem_box = FancyBboxPatch((0.5, 3.2), 3.4, 0.6, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='darkred', facecolor='#FFCCCC', linewidth=2)
ax.add_patch(problem_box)
ax.text(2.2, 3.5, '❌ Cannot do math with text!', fontsize=9, ha='center', fontweight='bold')

# CENTER: Transformation Arrow
arrow = FancyArrowPatch((4.3, 6), (5.7, 6),
                       arrowstyle='->', mutation_scale=40, linewidth=4, color='blue')
ax.add_patch(arrow)

# Transformation label
transform_box = FancyBboxPatch((4.2, 6.3), 1.6, 1.2, 
                              boxstyle="round,pad=0.1", 
                              edgecolor='blue', facecolor='#E5F5FF', linewidth=2)
ax.add_patch(transform_box)
ax.text(5, 7.2, 'Vectorization', fontsize=11, ha='center', fontweight='bold')
ax.text(5, 6.9, '&', fontsize=10, ha='center')
ax.text(5, 6.6, 'Encoding', fontsize=11, ha='center', fontweight='bold')

# RIGHT SIDE: ML-Ready Data
right_box = FancyBboxPatch((6, 3), 3.8, 5.5, 
                          boxstyle="round,pad=0.1", 
                          edgecolor='green', facecolor='#E5FFE5', linewidth=3)
ax.add_patch(right_box)
ax.text(7.9, 8.2, 'ML-READY DATA', fontsize=14, ha='center', fontweight='bold', color='darkgreen')
ax.text(7.9, 7.8, '(Math Readable)', fontsize=10, ha='center', style='italic')

# ML-ready data sample
ml_data = [
    ('Title TF-IDF:', '[0.42, 0.0, 0.81, ...]'),
    ('Subject_Business:', '1'),
    ('Subject_Finance:', '0'),
    ('level_encoded:', '0'),
    ('year:', '2017'),
    ('month:', '7'),
    ('price:', '50.0'),
    ('num_reviews:', '250'),
]

y_start = 7.2
for i, (label, value) in enumerate(ml_data[:6]):
    y_pos = y_start - i * 0.7
    ax.text(6.4, y_pos, label, fontsize=9, ha='left', fontweight='bold')
    ax.text(8.5, y_pos, value, fontsize=9, ha='left', family='monospace',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

# Success box
success_box = FancyBboxPatch((6.2, 3.2), 3.4, 0.6, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='darkgreen', facecolor='#CCFFCC', linewidth=2)
ax.add_patch(success_box)
ax.text(7.9, 3.5, '✓ All numbers, ready for algorithms!', fontsize=9, ha='center', fontweight='bold')

# BOTTOM: Transformation Details
detail_box = FancyBboxPatch((0.5, 0.3), 9, 2.5, 
                           boxstyle="round,pad=0.1", 
                           edgecolor='purple', facecolor='#F5E6FF', linewidth=2)
ax.add_patch(detail_box)
ax.text(5, 2.5, 'The Transformation Process', fontsize=13, ha='center', fontweight='bold', color='purple')

transformations = [
    '• Text (Titles): → TF-IDF vectors (100 numerical features)',
    '• Categorical (Subject): → One-Hot encoding (binary 0/1 columns)',
    '• Ordinal (Level): → Label encoding (0, 1, 2, 3)',
    '• Temporal (Date): → Year/Month integers (2017, 7)',
]

y_pos = 2
for i, text in enumerate(transformations):
    ax.text(0.8, y_pos - i * 0.35, text, fontsize=9, ha='left')

ax.text(5, 0.6, 'WHY? Algorithms require a Numerical Matrix to perform calculations!', 
        fontsize=10, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7, pad=0.4))

plt.tight_layout()
plt.savefig('data_transformation_comparison.png', dpi=150, bbox_inches='tight')
print('✓ Saved: data_transformation_comparison.png')
