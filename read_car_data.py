from stats_can import StatsCan
from datetime import date
sc = StatsCan()
df = sc.table_to_df("23-10-0066-01")

start_date = date(2000, 1, 31)
end_date = date(2021, 1, 3)

bw_values = df.query('@start_date < REF_DATE < @end_date')
bw_values.to_csv("want.csv")



fruit_vegs_consumption = sc.table_to_df("13-10-0096-12")

start_date = date(2000, 1, 31)
end_date = date(2021, 1, 3)

bw_values = fruit_vegs_consumption.query('@start_date < REF_DATE < @end_date')
bw_values.to_csv("fruits_vegs.csv")