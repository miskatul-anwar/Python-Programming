# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Create a Spark session
spark = SparkSession.builder.appName("PySparkExample").getOrCreate()

# Load a CSV file into a DataFrame
df = spark.read.csv(
    "./file.csv",
    header=True,
    inferSchema=True,
)

# Show the first few rows of the DataFrame
df.show()

# Filter the DataFrame based on a condition
filtered_df = df.filter(col("column_name") > 10)

# Group by a column and calculate the average
grouped_df = filtered_df.groupBy("group_column").agg(
    avg("value_column").alias("average_value")
)

# Show the resulting DataFrame
grouped_df.show()

# Stop the Spark session
spark.stop()
