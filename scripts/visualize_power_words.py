import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Hidden Value in Course Titles: Power Words', 
        fontsize=18, fontweight='bold', ha='center')

# Sample course titles with power words highlighted
titles = [
    ("The Complete Python Bootcamp", ["Complete", "Bootcamp"]),
    ("Ultimate Guide to Web Development", ["Ultimate", "Guide"]),
    ("Master JavaScript in 30 Days", ["Master"]),
    ("Learn Java Programming", []),
]

y_start = 8
for i, (title, power_words) in enumerate(titles):
    y_pos = y_start - i * 1.5
    
    # Title box
    box_color = '#E5FFE5' if power_words else '#FFE5E5'
    border_color = 'green' if power_words else 'red'
    box = FancyBboxPatch((0.5, y_pos - 0.4), 6, 0.8, 
                        boxstyle="round,pad=0.05", 
                        edgecolor=border_color, facecolor=box_color, linewidth=3)
    ax.add_patch(box)
    
    # Display title with power words highlighted
    ax.text(3.5, y_pos, f'"{title}"', fontsize=11, ha='center', va='center',
            fontweight='bold' if power_words else 'normal')
    
    # Power words indicator
    if power_words:
        power_text = ', '.join(power_words)
        ax.text(7.5, y_pos, f'💎 Power Words: {power_text}', 
                fontsize=9, ha='left', va='center', color='darkgreen',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.6))
    else:
        ax.text(7.5, y_pos, '❌ No power words', 
                fontsize=9, ha='left', va='center', color='darkred',
                bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.6))

# Power words list box
power_box = FancyBboxPatch((0.5, 0.5), 4, 2, 
                          boxstyle="round,pad=0.1", 
                          edgecolor='purple', facecolor='#F5E6FF', linewidth=2)
ax.add_patch(power_box)
ax.text(2.5, 2.2, 'Common Power Words', fontsize=12, ha='center', fontweight='bold', color='purple')
power_keywords = ['Complete', 'Bootcamp', 'Ultimate', 'Master', 'Guide', 
                 'Pro', 'Expert', 'Beginner', 'Course', '2024']
ax.text(2.5, 1.7, ' • '.join(power_keywords[:5]), fontsize=9, ha='center')
ax.text(2.5, 1.3, ' • '.join(power_keywords[5:]), fontsize=9, ha='center')
ax.text(2.5, 0.8, 'These words correlate with higher enrollments!', 
        fontsize=8, ha='center', style='italic')

# Why box
why_box = FancyBboxPatch((5, 0.5), 4.5, 2, 
                        boxstyle="round,pad=0.1", 
                        edgecolor='orange', facecolor='#FFF5E6', linewidth=2)
ax.add_patch(why_box)
ax.text(7.25, 2.2, 'WHY Extract Text Features?', fontsize=12, ha='center', fontweight='bold', color='darkorange')
ax.text(7.25, 1.7, '✓ Titles influence student decisions', fontsize=9, ha='center')
ax.text(7.25, 1.4, '✓ ML can learn which words = success', fontsize=9, ha='center')
ax.text(7.25, 1.1, '✓ Optimize titles BEFORE launch', fontsize=9, ha='center')
ax.text(7.25, 0.8, '✓ NLP bridges psychology & data', fontsize=9, ha='center')

plt.tight_layout()
plt.savefig('power_words.png', dpi=150, bbox_inches='tight')
print('✓ Saved: power_words.png')
