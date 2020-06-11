# Import Libraries
import pandas as pd 
import psycopg2 as psy


# Prompt User for information to connect with Database
#dbIPaddress = input(f'Please enter local IP address for Database: ')
#dbName = input(f'Please enter the Database Name: ')
#userID = input(f'Please enter your User Name for Postgres: ')
#pgPassword = input(f'Please enter your Postgres Password: ')
#portNumber = input(f'Please enter the Port Number your Database is on: ')

# Connect to the DB
#conn = psy.connect(
#       host = dbIPaddress,
#       database = dbName,
#       user = userID,
#       password = pgPassword,
#       port = int(portNumber)
#   )

# Connect to the DB (no User Data Query for debugging purpose)
# Input your Static fields below:
conn = psy.connect(
        host = '127.0.0.1',
        database = "testingPlayground",
        user = "postgres",
        password = "Abednigo#1",
        port = 5432
    )

# SQL to grab table
sql = "SELECT * FROM peter;"

# Store SQL Query into Pandas Dataframe
database = pd.read_sql_query(sql, conn)

# close DB Connection
conn.close()

def querysearch(startdate, enddate, dataframe = database):
   aquired_df = dataframe[dataframe['invoicedate'] >= startdate]
   aquired_df2 = aquired_df[aquired_df['invoicedate'] <= enddate]
   aquired_df3 = aquired_df2.groupby(['consignorid'], as_index=False)['itemcost'].sum()
    
    
    #aquired_df4 = aquired_df2.groupby('consignorid')['rent'].avg()
    #result = pd.concat([df1, df4], axis=1).reindex(df1.index)
    #return(print(aquired_df3))

querysearch("2019-08-10", "2019-08-31")

#startdate = input(f'Please input a Starting Date in YYYY-MM-DD format: ')
#enddate = input(f'Please input a Ending Date in YYYY-MM-DD format: ')

#querysearch(str(startdate), str(enddate))

#print(database)