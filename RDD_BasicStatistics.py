from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

# Start the SparkSession
spark = SparkSession.builder.appName('Statistics').getOrCreate()

# Create sparkContext
sc = spark.sparkContext
# Create a list of tuple
data = [('ann', 'spring', 'math', 98),
        ('ann', 'fall', 'bio', 50),
        ('bob', 'spring', 'stats', 100),
        ('bob', 'fall', 'stats', 92),
        ('bob', 'summer', 'stats', 100),
        ('charles', 'spring', 'stats', 88),
        ('charles', 'fall', 'bio', 100)]
# Create a RDD from the list
rdd = sc.parallelize(data)
# Create a PySpark DataFrame from RDD
df = spark.createDataFrame(rdd, ['name', 'semester', 'subject', 'score'])
df.show()
df.describe()
df.select("score").describe().show()
# Filtering rows
df.filter(df['score'] > 90).show()
# Mutating values
df.select(df['name'], df['semester'], df['subject'], df['score'], (df['score'] - 10).alias('adj_score')).show()
df.withColumn('sqrt_socre', df['score'] / 2).show()
# Sorting
df.sort(df['score']).show()
df.sort(df['score'].desc()).show()
# Jo
data = [('ann', 'female', 23),
        ('bob', 'male', 19),
        ('charles', 'male', 22),
        ('david', 'male', 23)]

# Define PySpark DataFrame schema: the entire schema is stored as a StructType and individual columns are stored as
# StructFields
schema = StructType([StructField('name', StringType(), True), StructField('sex', StringType(), True),
                     StructField('age', IntegerType(), True)])
df_meta = spark.createDataFrame(data, schema)
df_meta.printSchema()
df.join(df_meta, on='name', how='inner').show()
