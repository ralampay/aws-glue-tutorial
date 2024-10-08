import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext().getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Specify the Glue database and table name
glue_database = "tutorial_db"  # Replace with your Glue catalog database
glue_table = "customers"  # The Glue table where the customer data is cataloged

# Create a DynamicFrame from the Glue catalog
dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database=glue_database,
    table_name=glue_table
)

# Convert the DynamicFrame to a Spark DataFrame
df = dynamic_frame.toDF()

# Group by customer_id and sum the amounts
grouped_df = df.groupBy("customer_id").agg(F.sum("amount").alias("total_amount"))

# Show the result of the grouping and summing in the logs
grouped_df.show()  # Display all results

# Complete the job
job.commit()
