import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Load data
df = pd.read_csv('udemy_courses.csv')

# Create visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Before dropping column
columns_before = list(df.columns)
colors_before = ['#FF6B6B' if col == 'url' else '#4ECDC4' for col in columns_before]

ax1.barh(range(len(columns_before)), [1]*len(columns_before), 
         color=colors_before, alpha=0.8, edgecolor='black', linewidth=2)
ax1.set_yticks(range(len(columns_before)))
ax1.set_yticklabels(columns_before, fontsize=10)
ax1.set_xlim(0, 1.2)
ax1.set_title('BEFORE: df.drop()', fontsize=14, fontweight='bold')
ax1.set_xlabel('Columns', fontsize=12)
ax1.text(0.6, len(columns_before)-1, '← Target for removal', 
         fontsize=10, color='darkred', fontweight='bold')

# After dropping column
df_after = df.drop(['url'], axis=1)
columns_after = list(df_after.columns)
colors_after = ['#51CF66' for _ in columns_after]

ax2.barh(range(len(columns_after)), [1]*len(columns_after), 
         color=colors_after, alpha=0.8, edgecolor='black', linewidth=2)
ax2.set_yticks(range(len(columns_after)))
ax2.set_yticklabels(columns_after, fontsize=10)
ax2.set_xlim(0, 1.2)
ax2.set_title('AFTER: df.drop([\'url\'], axis=1)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Columns', fontsize=12)

# Add legend
before_patch = mpatches.Patch(color='#FF6B6B', label='Column to Remove')
keep_patch = mpatches.Patch(color='#4ECDC4', label='Kept Columns')
after_patch = mpatches.Patch(color='#51CF66', label='Final Columns')
fig.legend(handles=[before_patch, keep_patch, after_patch], 
           loc='upper center', ncol=3, fontsize=11, bbox_to_anchor=(0.5, 0.98))

# Add summary text
fig.text(0.5, 0.02, f'Result: {len(columns_before)} columns → {len(columns_after)} columns (removed: url)', 
         ha='center', fontsize=12, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

plt.tight_layout(rect=[0, 0.04, 1, 0.96])
plt.savefig('column_removal.png', dpi=150, bbox_inches='tight')
print('✓ Saved: column_removal.png')
print(f'\nColumns before: {len(columns_before)}')
print(f'Columns after: {len(columns_after)}')
print(f'Removed: url')
