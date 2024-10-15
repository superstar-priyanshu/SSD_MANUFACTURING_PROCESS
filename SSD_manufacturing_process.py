import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate mock manufacturing data
np.random.seed(42)

# Sample data: 100 batches of SSDs with varying yields and costs
data = {
    'Batch': np.arange(1, 101),
    'Defect_Rate': np.random.normal(loc=0.03, scale=0.01, size=100),  # Defect rate around 3%
    'Yield': np.random.normal(loc=97, scale=2, size=100),  # Yield percentage
    'Cost_Per_Batch': np.random.normal(loc=50000, scale=5000, size=100),  # Manufacturing cost
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate sigma level (Six Sigma quality)
def sigma_level(yield_percent):
    return (yield_percent - 50) / 15  # Simplified Six Sigma formula

df['Sigma_Level'] = df['Yield'].apply(sigma_level)

# Visualizing the data
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Batch', y='Defect_Rate', data=df, label='Defect Rate')
plt.axhline(y=df['Defect_Rate'].mean(), color='r', linestyle='--', label='Average Defect Rate')
plt.title('Defect Rate per Batch')
plt.xlabel('Batch Number')
plt.ylabel('Defect Rate')
plt.legend()
plt.show()

# Yield vs Cost analysis
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Cost_Per_Batch', y='Yield', data=df, label='Yield per Batch')
plt.title('Yield vs. Manufacturing Cost')
plt.xlabel('Cost Per Batch ($)')
plt.ylabel('Yield (%)')
plt.show()

# Analyze cost per yield
df['Cost_Per_Unit'] = df['Cost_Per_Batch'] / (df['Yield'] * 1000)  # Assuming 1000 units per batch
average_cost_per_unit = df['Cost_Per_Unit'].mean()

# Output optimization suggestions
print(f'Average cost per unit: ${average_cost_per_unit:.2f}')
print('Optimization Strategy:')
if average_cost_per_unit > 50:
    print('- Investigate process improvements to reduce manufacturing costs per batch.')
if df['Defect_Rate'].mean() > 0.02:
    print('- Focus on reducing defect rates to improve yield and lower cost per unit.')

# Control chart for Defect Rate (Basic SPC)
plt.figure(figsize=(10, 6))
sns.lineplot(x='Batch', y='Defect_Rate', data=df, label='Defect Rate')
plt.axhline(y=df['Defect_Rate'].mean(), color='r', linestyle='--', label='Mean Defect Rate')
plt.axhline(y=df['Defect_Rate'].mean() + 3*df['Defect_Rate'].std(), color='g', linestyle='--', label='Upper Control Limit')
plt.axhline(y=df['Defect_Rate'].mean() - 3*df['Defect_Rate'].std(), color='g', linestyle='--', label='Lower Control Limit')
plt.title('Defect Rate Control Chart')
plt.xlabel('Batch Number')
plt.ylabel('Defect Rate')
plt.legend()
plt.show()
