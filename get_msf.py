import pandas as pd
import numpy as np
import wrds

## Connect to WRDS:
conn=wrds.Connection()

## Set start and end date for query:
begdate = '01/01/2000'
enddate = '12/31/2010'

## Fetch select columns from CRSP.MSF:
results = conn.raw_sql(f"""
                        select permno, date, cfacpr, cfacshr, shrout, prc, ret
                        from crsp.msf 
                        where date between '{begdate}' and '{enddate}'
                        """, date_cols=['date']) 

## Print Pandas DF overview of results, just as example.
## In actual research, we would further iterate through
## this results object towards a posited research goal:
print(results)
