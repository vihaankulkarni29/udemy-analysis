import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Linear model visual
x = np.linspace(0, 10, 50)
y = 2 * x + 5
axes[0].plot(x, y, color='#3498db', linewidth=3)
axes[0].scatter([2, 5, 8], [3, 30, 18], color='red', zorder=5)
axes[0].set_title('Linear Regression (too simple)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Features')
axes[0].set_ylabel('Predicted subscribers')
axes[0].text(0.5, 0.1, 'Assumes straight line\nMisses nonlinear course patterns', transform=axes[0].transAxes,
             fontsize=10, bbox=dict(boxstyle='round', facecolor='#ecf0f1', edgecolor='black'))

# Decision tree / forest visual
axes[1].axis('off')
axes[1].set_title('Random Forest (many trees)', fontsize=12, fontweight='bold')

# Draw simple tree boxes
axes[1].add_patch(plt.Rectangle((0.25, 0.75), 0.5, 0.15, fill=False, linewidth=2))
axes[1].text(0.5, 0.825, 'Is it Free?', ha='center', va='center', fontsize=11)

axes[1].add_patch(plt.Rectangle((0.05, 0.45), 0.35, 0.15, fill=False, linewidth=2))
axes[1].text(0.225, 0.525, 'Yes -> High Subs', ha='center', va='center', fontsize=10)

axes[1].add_patch(plt.Rectangle((0.6, 0.45), 0.35, 0.15, fill=False, linewidth=2))
axes[1].text(0.775, 0.525, 'No -> Check Title', ha='center', va='center', fontsize=10)

axes[1].add_patch(plt.Rectangle((0.6, 0.15), 0.35, 0.15, fill=False, linewidth=2))
axes[1].text(0.775, 0.225, 'Has "Beginner"?\nMedium Subs', ha='center', va='center', fontsize=10)

axes[1].add_patch(plt.Rectangle((0.05, 0.15), 0.35, 0.15, fill=False, linewidth=2))
axes[1].text(0.225, 0.225, 'Niche Topic\nLower Subs', ha='center', va='center', fontsize=10)

axes[1].text(0.5, -0.05, 'Forest = hundreds of these trees\nEnsembled for robust predictions', ha='center', fontsize=10,
             bbox=dict(boxstyle='round', facecolor='#dff9fb', edgecolor='black'))

plt.tight_layout()
plt.savefig('slide17_model_choice.png', dpi=150)
print('✓ Saved: slide17_model_choice.png')
