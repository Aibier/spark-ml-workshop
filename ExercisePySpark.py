from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Start the SparkSession
spark = SparkSession.builder.appName('ExercisePySpark').getOrCreate()

# Create sparkContext
sc = spark.sparkContext
# Create a list of tuple
data = [
    ("James", "Sales", "SG", 70000, 34, 10000),
    ("Michael", "Sales", "SG", 66000, 56, 20000),
    ("Robert", "Sales", "MY", 61000, 30, 23000),
    ("Maria", "Finance", "MY", 60000, 24, 23000),
    ("Raman", "Finance", "USA", 79000, 40, 24000),
    ("Scott", "Finance", "USA", 63000, 36, 19000),
    ("Jen", "Finance", "UK", 89000, 53, 15000),
    ("Jeff", "Marketing", "UK", 70000, 25, 18000),
    ("Alice", "Marketing", "UK", 78000, 50, 21000),
    ("Ada", "IT", "SG", 83000, 35, 11000),
    ("Jackson", "IT", "MY", 71000, 30, 21000),
    ("Cooper", "IT", "UK", 91000, 40, 21000)
]

# a. create rdd
rdd = sc.parallelize(data)

# b. show data frame
schema = StructType(
    [
        StructField('employee_name', StringType(), True),
        StructField('department', StringType(), True),
        StructField('country', StringType(), True),
        StructField('salary', IntegerType(), True),
        StructField('age', IntegerType(), True),
        StructField('bonus', IntegerType(), True),
    ]
)
df = spark.createDataFrame(rdd, schema)
df.show()
df.printSchema()
# c. max, min, avg, sum salary by department
depSalary = df.groupBy('department')
depSalary.agg({'salary': 'max'}).show()
depSalary.agg({'salary': 'min'}).show()
depSalary.agg({'salary': 'avg'}).show()
depSalary.agg({'salary': 'sum'}).show()

# d. max, min, avg, sum salary by country
countrySalary = df.groupBy('country')
countrySalary.agg({'salary': 'max'}).show()
countrySalary.agg({'salary': 'min'}).show()
countrySalary.agg({'salary': 'avg'}).show()
countrySalary.agg({'salary': 'sum'}).show()
