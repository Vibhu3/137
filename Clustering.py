import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("dwarf_stars.csv")

fig = px.scatter(x=df["Mass"].tolist(), y=df["Radius"].tolist())
#fig.show()


X = df.iloc[:, [2, 3]].values
#print(X[1])
wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

"""
plt.figure(figsize=(10,5))
sns.lineplot(range(1,11), wcss, markers="o", color="red")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()
"""

kmeans = KMeans(n_clusters=3, init="k-means++", random_state=42)
kmeans.fit(X)
y_kmeans = kmeans.fit_predict(X)

plt.figure(figsize=(15,7))
sns.scatterplot(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], color='yellow', label='Cluster 1')
sns.scatterplot(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], color='blue', label='Cluster 2')
sns.scatterplot(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], color='green', label='Cluster 3')

sns.scatterplot(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], color="red", label="Centroids", s=100, marker=",")

plt.title("Cluster of Stars")
plt.xlabel("Mass")
plt.ylabel("Radiuses")
plt.show()
