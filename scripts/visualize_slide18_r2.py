import matplotlib.pyplot as plt

r2_score_value = 0.92

fig, ax = plt.subplots(figsize=(6, 6))

ax.bar(['R2 Score'], [r2_score_value], color='#2ecc71')
ax.set_ylim(0, 1.05)
ax.set_ylabel('Variance Explained')
ax.set_title('Slide 18: Model Performance (R2)', fontsize=14, fontweight='bold')
ax.text(0, r2_score_value + 0.02, f'{r2_score_value:.2f}', ha='center', fontsize=12, fontweight='bold')
ax.text(0, 0.4, 'Measures how well the model\nexplains new course trends', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='#ecf0f1', edgecolor='black'))

plt.tight_layout()
plt.savefig('slide18_r2.png', dpi=150)
print('✓ Saved: slide18_r2.png')
