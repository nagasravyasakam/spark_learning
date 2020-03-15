import pyspark
sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('input.txt')
print(txt.count())
