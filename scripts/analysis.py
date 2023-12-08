
from ydata_profiling import ProfileReport
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


path = "data"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
# Create a new directory because it does not exist
    os.makedirs(path)
#columns as specified in wine.names plus the class
columns = ['Class','Alcohol','Malicacid','Ash','Alcalinity_of_ash','Magnesium','Total_phenols','Flavanoids','Nonflavanoid_phenols',
           'Proanthocyanins','Color_intensity','Hue','OD280/OD315_of_diluted wines','Proline']

df_wine = pd.read_csv(os.path.join(path,'wine/wine.data'), names=columns,
                              sep=',', engine='python')

results_path = "results/"
# Check whether the specified path exists or not
isExist = os.path.exists(results_path)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(results_path)

# Pairplot for pairwise relationships
sns.pairplot(df_wine[['Alcohol', 'Malicacid', 'Ash', 'Alcalinity_of_ash', 'Magnesium', 'Color_intensity']])
plt.suptitle('Pairplot of Selected Wine Features', y=1.02)
plt.savefig(os.path.join(results_path, 'pairplot.png'), bbox_inches='tight')
plt.close()

# Correlation heatmap
correlation_matrix = df_wine[['Alcohol', 'Malicacid', 'Ash', 'Alcalinity_of_ash', 'Magnesium', 'Color_intensity']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Selected Wine Features')
plt.savefig(os.path.join(results_path, 'correlation_heatmap.png'), bbox_inches='tight')
plt.close()

# Violin plot for Color_intensity
plt.figure(figsize=(10, 6))
sns.violinplot(x=df_wine['Color_intensity'])
plt.title('Violin Plot of Color_intensity')
plt.savefig(os.path.join(results_path, 'violin_plot.png'), bbox_inches='tight')
plt.close()

# Distribution plot for Alcohol
plt.figure(figsize=(10, 6))
sns.histplot(df_wine['Alcohol'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Alcohol Content in Wines')
plt.xlabel('Alcohol Content')
plt.ylabel('Frequency')
plt.savefig(os.path.join(results_path, 'distribution_plot.png'), bbox_inches='tight')
plt.close()

