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
https://transactions-cooperative.s3.ap-southeast-1.amazonaws.com/transactions-2021.csv?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDmFwLXNvdXRoZWFzdC0xIkYwRAIgQXET2K9TymtMSxdw%2BvLSw%2BZQgOwZ1zDMdsEykdZqO94CICk%2BRLxKBFtfRKIQOTpdxVlqFSRoe0L5uPTyl%2Fe1H21DKuQCCEAQABoMNDI4ODQ2ODA4MDk3IgwdrkRPjjzse6BwJAAqwQKKEvgduLONbFCquOnUbNo4aFIgIaSRJUKQGE7hfadt37eP87LQjABvTgS3JPrfeEY6bjidQxH5TVx%2Fm06oQU2m8refCACYUCZufkqcid9cwMNka7OJCAjunLq%2F3XCvzTaYB5rPfhrxxfThJ5LocU%2Bt%2FOLv90NFs33IqigTHsU8ngRW2cd3AC%2FZXbGNUyWa%2B7a9RVejOU2HTC4vCY9zXajLCzBVBiU3MZkn%2BoV7GmpRLqYAUA5iyjehCArVdPilCReUbLzO%2FX4rDmxnOZ%2Bl9CEQLZ%2BoEZsuhEVLV8RmmLd%2BMGA08x5o0HBbCC6DIOSz16yOvP%2FnVLz1G9l7iT1iJIc8z4MYHl6ew3NSG3QeaQKh2oYcjw0iLxGy%2FWHLpXjydc%2BbT72H4Gmf5CDX4LcDyxpPN2h%2FcEV6NSZxwi1B%2F2utluMwhraTuAY6tAKmYMME%2BCHruIUfmMtFjoF2WaZ9N6BrT7%2FPDrLkQylI43GTw%2FEpOeRIsrOOi6sABAJxgFEiQGnAnaat7cf9Zh7Jp9onm4i4VTB5iuoFWH8VSQRPfPhqpp7Lh6R2MOA7%2FD8FDHHTn7x8p3SqyxwELLRiQSvWqjf66phV%2FSCMUnypG%2FMCBm4HOyFaeAha3CrYhmPVmMbbQFXoZ5IvMBsqoZl67rCrXLkk1KU8MQ%2F0WDPDeaJLN7b7YIb9wODSlkvilwO3oH0BEXWP3LOaI8aD%2Fqv9rBxJTp3e2jhYfwUmW0E4HyxPd5Sl2VGM4961pFyoriTs5cFmfqf1jxNjLjKaP36ezTqsGU0oOO%2BKeyvqqSkuQyN%2BcSdJgKEEQtOeOOLIAkNbKmauj6ciK3VjjfEtelnZH%2BTz9Q%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241008T072256Z&X-Amz-SignedHeaders=host&X-Amz-Expires=14400&X-Amz-Credential=ASIAWHWKC7QQT443E4V6%2F20241008%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Signature=b156bfcd22428c0dad9015d864ce5b3bb75a0316593d546f48e1f674b6982a4c
```

1. Load the file as a Data Glue Catalog

2. analyze the produced columns

3. Create an ETL job that performs some aggregation and load it to another S3 bucket.
