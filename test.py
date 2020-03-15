from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").master('local').enableHiveSupport().getOrCreate()
 

# text_file = spark.read.csv("input.txt")
myfile=spark.read.text('input')
myfile.show()
myfile.printSchema()
myfile.repartition(10)
myfile.write.csv('output.txt')
myfile.write.table()