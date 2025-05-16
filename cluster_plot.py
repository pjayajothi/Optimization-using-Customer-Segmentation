import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load your cleaned data
df = pd.read_csv("cleaned_CC_GENERAL.csv")

# Standardize features
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)

# PCA for dimensionality reduction
pca = PCA(n_components=2)
reduced = pca.fit_transform(df_scaled)

# Plot clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x=reduced[:, 0], y=reduced[:, 1], hue=df['Cluster'], palette="tab10")
plt.title("Customer Segments (PCA-Reduced)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend(title="Cluster")
plt.tight_layout()
plt.savefig("cluster_plot.png")
plt.show()
