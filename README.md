# AWS Glue Tutorial Files

## Code Snippets

### Read from S3 Bucket

```python
# Load the CSV file into a DynamicFrame
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [f"s3://transactions-cooperative/tranactions-2023.csv"]},
    format="csv",
    format_options={"withHeader": True}
)
```

### Upload to S3 Bucket

```python
# Define the S3 output path
s3_output_file = "s3://s3-workshop-miranda-b/result_chino.csv"

# Write the DataFrame to S3 in CSV format
df_result.coalesce(1).write.csv(s3_output_file, header=True, mode='overwrite')
```

## Exercises

Download the file in:

```
https://transactions-cooperative.s3.ap-southeast-1.amazonaws.com/transactions-2021.csv
```

1. Load the file as a Data Glue Catalog

2. analyze the produced columns

3. Create an ETL job that performs some aggregation and load it to another S3 bucket.
