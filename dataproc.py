1. Data Processing (ETL / Analytics)

Use case: Clean and transform raw data

data = ["10", "20", "30", "invalid", "40"]

cleaned = [int(x) for x in data if x.isdigit()]
print(sum(cleaned))

✅ Output

100
