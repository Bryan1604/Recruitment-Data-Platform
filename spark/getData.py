from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

# khoi tao spark session 
spark = SparkSession.builder.appName("KafkaSparkIntegration").getOrCreate()

# doc du lieu tu kafka
df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "job_topic").load()
  
# Chuyển đổi dữ liệu nhị phân sang chuỗi
value_df = df.selectExpr("CAST(value AS STRING)")


# Hiển thị dữ liệu
query = value_df.writeStream.outputMode("append").format("console").start()
