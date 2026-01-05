import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv('udemy_courses.csv')

# Create figure with larger size
fig, ax = plt.subplots(figsize=(14, 8))

# Plot histogram of prices
prices = df['price'].dropna()
n, bins, patches = ax.hist(prices, bins=50, alpha=0.7, color='skyblue', 
                           edgecolor='black', linewidth=0.5)

# Define bin boundaries
bin_edges = [0, 0.01, 50, prices.max()]
bin_labels = ['Free', 'Budget (<$50)', 'Premium (≥$50)']
bin_colors = ['#2ecc71', '#3498db', '#9b59b6']

# Draw vertical lines for bin boundaries
for i, edge in enumerate(bin_edges[1:-1], 1):
    ax.axvline(x=edge, color='red', linestyle='--', linewidth=3, 
               label=f'Bin Edge: ${edge}' if i == 1 else '')
    
    # Add arrow and label
    y_pos = ax.get_ylim()[1] * 0.85
    ax.annotate(f'Split at ${edge}', 
                xy=(edge, y_pos), 
                xytext=(edge + 20, y_pos),
                fontsize=12, fontweight='bold', color='red',
                arrowprops=dict(arrowstyle='->', color='red', lw=2))

# Shade the regions for each bin
y_max = ax.get_ylim()[1]
for i in range(len(bin_edges) - 1):
    start = bin_edges[i]
    end = bin_edges[i + 1]
    
    # Add colored rectangle background
    ax.axvspan(start, end, alpha=0.2, color=bin_colors[i])
    
    # Add bin label in the middle
    mid_point = (start + end) / 2
    ax.text(mid_point, y_max * 0.95, bin_labels[i], 
            fontsize=14, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=bin_colors[i], 
                     alpha=0.8, edgecolor='black', linewidth=2))

# Add annotations showing the problem and solution
problem_text = (
    "PROBLEM: Continuous Noise\n"
    "• $19.99, $21.50, $19.95 all treated differently\n"
    "• Model overfits to exact prices\n"
    "• Unstable predictions"
)
ax.text(0.02, 0.97, problem_text, transform=ax.transAxes,
        fontsize=11, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='#e74c3c', alpha=0.9, 
                 edgecolor='black', linewidth=2),
        color='white', fontweight='bold', family='monospace')

solution_text = (
    "SOLUTION: Binning (Discretization)\n"
    "• Group prices into strategic buckets\n"
    "• Model learns macro-trends (e.g., 'Free → Viral')\n"
    "• Robust categorical features"
)
ax.text(0.98, 0.97, solution_text, transform=ax.transAxes,
        fontsize=11, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='#2ecc71', alpha=0.9, 
                 edgecolor='black', linewidth=2),
        color='white', fontweight='bold', family='monospace')

# Count courses in each bin
free_count = len(df[df['price'] == 0])
budget_count = len(df[(df['price'] > 0) & (df['price'] < 50)])
premium_count = len(df[df['price'] >= 50])

# Add counts at the bottom
count_text = f"Distribution: Free={free_count} | Budget={budget_count} | Premium={premium_count}"
ax.text(0.5, -0.15, count_text, transform=ax.transAxes,
        fontsize=12, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8, 
                 edgecolor='black', linewidth=2))

# Styling
ax.set_xlabel('Price ($)', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Courses', fontsize=14, fontweight='bold')
ax.set_title('Feature Engineering: Binning Continuous Data into Strategic Categories', 
             fontsize=16, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
ax.set_xlim(left=-5)

# Add example transformation box
example_text = (
    "TRANSFORMATION EXAMPLE:\n"
    "Before: price = 19.99, 21.50, 19.95 (3 different features)\n"
    "After:  price_bin = 'Budget', 'Budget', 'Budget' (1 feature)\n\n"
    "Result: Model identifies pattern \"Budget courses popular\" instead of\n"
    "        getting confused by minor price differences"
)
ax.text(0.5, -0.30, example_text, transform=ax.transAxes,
        fontsize=10, ha='center', verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='#f39c12', alpha=0.9, 
                 edgecolor='black', linewidth=2),
        family='monospace', fontweight='bold')

plt.tight_layout()
plt.subplots_adjust(bottom=0.25)  # Make room for bottom text
plt.savefig('binning_technique.png', dpi=150, bbox_inches='tight')
print("✓ Saved: binning_technique.png")
