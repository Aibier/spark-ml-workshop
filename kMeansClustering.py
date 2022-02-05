# Initializing Spark Session
from pyspark.sql import SparkSession
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.clustering import KMeans

spark = SparkSession.builder.appName('kmeansCluster').getOrCreate()

dataset = spark.read.format("libsvm").load("sample_kmeans_data.txt")
# Training a kmeans model
kmeans = KMeans().setK(2).setSeed(1)
model = kmeans.fit(dataset)
# Making predictions
predictions = model.transform(dataset)
# Evaluate clustering by computing silhouette score
evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))
# Print cluster centers

centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)
