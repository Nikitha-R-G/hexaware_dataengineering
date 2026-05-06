import dlt
from pyspark.sql.functions import *
#Question 88 — Bronze Table

@dlt.table(
    name="bronze_orders",
    comment="Raw daily order data"
)
def bronze_orders():

    daily_orders_data = [
        (1,101,1001,"2024-03-01",5,"Completed"),
        (2,102,1002,"2024-03-01",2,"Completed"),
        (3,103,1003,"2024-03-02",-1,"Cancelled"),
        (4,104,1001,"2024-03-02",3,"Completed"),
        (5,105,1004,"2024-03-03",0,"Pending")
    ]

    daily_orders_columns = [
        "order_id",
        "product_id",
        "supplier_id",
        "order_date",
        "quantity",
        "order_status"
    ]

    return spark.createDataFrame(daily_orders_data, daily_orders_columns)

#89 — Silver Cleaned Table
@dlt.table(
    name="silver_orders",
    comment="Cleaned orders data"
)
def silver_orders():

    df = dlt.read("bronze_orders")

    return (
        df.withColumn("order_date", to_date("order_date"))
          .withColumn("quantity", col("quantity").cast("int"))
    )

# 90 — Add Total Revenue
@dlt.table(
    name="silver_orders_revenue"
)
def silver_orders_revenue():

    return (
        dlt.read("silver_orders")
        .withColumn("total_revenue", col("quantity") * lit(100))
    )
# 91 — Remove Invalid Records
@dlt.table(
    name="silver_orders_clean"
)
def silver_orders_clean():

    return (
        dlt.read("silver_orders_revenue")
        .filter("quantity > 0")
        .filter("order_status != 'Cancelled'")
    )

#92 — Gold Revenue by City
@dlt.table(
    name="gold_cities_revenue"
)
def gold_city_revenue():

    df = dlt.read("silver_orders_clean")

    city_df = df.withColumn(
        "city",
        when(col("supplier_id")==1001,"Chennai")
        .when(col("supplier_id")==1002,"Bangalore")
        .otherwise("Hyderabad")
    )

    return city_df.groupBy("city") \
        .agg(sum("total_revenue").alias("city_revenue"))

#93 — Gold Revenue by Category
@dlt.table(
    name="gold_category_revenue"
)
def gold_category_revenue():

    df = dlt.read("silver_orders_clean")

    category_df = df.withColumn(
        "category",
        when(col("product_id")==101,"Electronics")
        .when(col("product_id")==102,"Furniture")
        .otherwise("Accessories")
    )

    return category_df.groupBy("category") \
        .agg(sum("total_revenue").alias("category_revenue"))