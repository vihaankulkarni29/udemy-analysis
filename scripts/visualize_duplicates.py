import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('udemy_courses.csv')
df_clean = df.drop_duplicates()

# Create visualization
fig, ax = plt.subplots(figsize=(10, 6))

categories = ['Before Cleaning', 'After Cleaning']
values = [len(df), len(df_clean)]

bars = ax.bar(categories, values, color=['#FF6B6B', '#51CF66'], alpha=0.8, edgecolor='black', linewidth=2)

ax.set_ylabel('Number of Rows', fontsize=14)
ax.set_title('Duplicate Removal: Before vs After', fontsize=16, fontweight='bold')
ax.set_ylim(3650, 3680)

# Add value labels on bars
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
            f'{val} rows', ha='center', fontsize=12, fontweight='bold')

# Add removed count
removed = len(df) - len(df_clean)
ax.text(0.5, 3665, f'Removed: {removed} duplicates', 
        ha='center', fontsize=12, color='darkred', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

plt.tight_layout()
plt.savefig('duplicate_removal.png', dpi=150, bbox_inches='tight')
print('✓ Saved: duplicate_removal.png')
