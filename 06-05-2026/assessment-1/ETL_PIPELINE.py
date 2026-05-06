import dlt
from pyspark.sql.functions import *


# Inline Source Data


data = [
(1,1001,"Hyderabad","Cardiology",5200),
(2,1002,"Bengaluru","Dermatology",2800),
(3,1003,"Mumbai","Orthopedics",7500),
(4,1004,"Delhi","Pediatrics",2900),
(5,1005,"Hyderabad","Neurology",5300),
(6,1006,"Chennai","Cardiology",10000),
(7,1007,"Kolkata","Dermatology",2850),
(8,1008,"Bengaluru","Orthopedics",5400),
(9,1009,"Kochi","Neurology",3200),
(10,1010,"Pune","General Medicine",4800)
]

columns = [
"visit_id",
"patient_id",
"city",
"specialization",
"bill_amount"
]

df = spark.createDataFrame(data, columns)


# 88. Bronze Table

@dlt.table(name="bronze_patient_visits")
def bronze_patient_visits():
    return df



# 89–91 Silver Table

@dlt.table(name="silver_patient_visits")
def silver_patient_visits():
    return (
        dlt.read("bronze_patient_visits")
        .withColumn("total_bill", col("bill_amount") * 1.10)  # total bill
        .filter(col("bill_amount").isNotNull())               # remove invalid
    )



# 92 Gold City Revenue

@dlt.table(name="gold_city_revenue")
def gold_city_revenue():
    return (
        dlt.read("silver_patient_visits")
        .groupBy("city")
        .agg(sum("total_bill").alias("city_revenue"))
    )



# 93 Gold Specialization Revenue

@dlt.table(name="gold_specialization_revenue")
def gold_specialization_revenue():
    return (
        dlt.read("silver_patient_visits")
        .groupBy("specialization")
        .agg(sum("total_bill").alias("specialization_revenue"))
    )