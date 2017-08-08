
import csv
counter = 28600
with  open("Mike's SQL export.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in enumerate(reader):
        #print(row['DATE_ID'], row['CALENDAR_DATE'],row['BI_RPT_REGION_CODE'],row['LOCATION_NUMBER'],row['DEPARTMENT_NUM'],row['DEPARTMENT_SHORT_DESC'],row['AMOUNT'],row['MEASURE_QTY'])
        #print(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7])
        print(row[:5])
        counter += 1
        if counter > 28605:
            break