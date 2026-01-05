import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')
ax.set_title('Slide 19: Strategy Engine (Streamlit)', fontsize=14, fontweight='bold')

# App frame
ax.add_patch(Rectangle((0.1, 0.2), 0.8, 0.6, linewidth=2, edgecolor='black', facecolor='#f7f9fb'))
ax.text(0.5, 0.75, 'Streamlit App', ha='center', va='center', fontsize=12, fontweight='bold')

# Input field
ax.add_patch(Rectangle((0.2, 0.55), 0.6, 0.08, linewidth=1.5, edgecolor='#2980b9', facecolor='white'))
ax.text(0.23, 0.59, 'Course title: "Java Masterclass"', ha='left', va='center', fontsize=10)

# Button
ax.add_patch(Rectangle((0.2, 0.45), 0.2, 0.08, linewidth=1.5, edgecolor='#27ae60', facecolor='#2ecc71'))
ax.text(0.3, 0.49, 'Predict', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Output panel
a_output = Rectangle((0.2, 0.25), 0.6, 0.16, linewidth=1.5, edgecolor='#8e44ad', facecolor='white')
ax.add_patch(a_output)
ax.text(0.23, 0.36, 'Predicted subscribers: 18,500', ha='left', va='center', fontsize=10, fontweight='bold')
ax.text(0.23, 0.30, 'Advice: Add "Beginner" keyword, keep price < $50', ha='left', va='center', fontsize=10)

ax.text(0.5, 0.1, 'From analysis to product: live predictions for new courses', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='#ecf0f1', edgecolor='black'))

plt.tight_layout()
plt.savefig('slide19_strategy_engine.png', dpi=150)
print('✓ Saved: slide19_strategy_engine.png')
