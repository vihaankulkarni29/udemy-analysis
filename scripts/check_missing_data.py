import pandas as pd
import matplotlib.pyplot as plt

# Load data and check missing values
df = pd.read_csv('udemy_courses.csv')
missing = df.isnull().sum()

# Create visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Filter only columns with missing values for better viz
missing_data = missing[missing > 0] if missing.sum() > 0 else pd.Series([0], index=['No Missing Values'])

colors = ['#FF6B6B' if val > 0 else '#51CF66' for val in missing_data.values]
bars = ax.barh(missing_data.index, missing_data.values, color=colors, alpha=0.8, edgecolor='black', linewidth=2)

ax.set_xlabel('Number of Missing Values', fontsize=14)
ax.set_title('Missing Data Analysis', fontsize=16, fontweight='bold')

# Add value labels
for i, (bar, val) in enumerate(zip(bars, missing_data.values)):
    ax.text(val + 0.5, i, f'{int(val)}', va='center', fontsize=12, fontweight='bold')

# Add total missing info
total_missing = missing.sum()
ax.text(0.5, 0.95, f'Total Missing Values: {total_missing}', 
        transform=ax.transAxes, ha='center', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('missing_data_check.png', dpi=150, bbox_inches='tight')
print('✓ Saved: missing_data_check.png')
print(f'\nMissing values per column:\n{missing}')
