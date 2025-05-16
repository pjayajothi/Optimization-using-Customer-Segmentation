# Simulate revenue by segment (based on cluster)
np.random.seed(42)
revenue_map = {
    0: np.random.normal(500, 100, len(df[df['Cluster'] == 0])),
    1: np.random.normal(300, 80, len(df[df['Cluster'] == 1])),
    2: np.random.normal(200, 70, len(df[df['Cluster'] == 2])),
    3: np.random.normal(100, 50, len(df[df['Cluster'] == 3])),
}
df['Simulated_Revenue'] = df['Cluster'].map(revenue_map).explode().astype(float)

# Compare random targeting to cluster-based targeting
random_customers = df.sample(frac=0.25, random_state=1)
segment_customers = df[df['Cluster'] == 0].sample(frac=0.25, random_state=1)

random_revenue = random_customers['Simulated_Revenue'].sum()
segment_revenue = segment_customers['Simulated_Revenue'].sum()

# Create lift chart
plt.figure(figsize=(6, 4))
sns.barplot(x=['Random Targeting', 'Segment-Based Targeting'],
            y=[random_revenue, segment_revenue])
plt.title("Estimated Revenue Comparison")
plt.ylabel("Simulated Revenue")
plt.tight_layout()
plt.savefig("lift_chart.png")
plt.show()
