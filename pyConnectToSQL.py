# MSSQL to Python 

import pyodbc 


# server examples (connectiong stuff) 

#server = 'tcp:myserver.database.windows.net' # obviously, theses are BS values 



server ='WS3040532\WORBENCH' # for a named instance 
database = 'test' 
username = 'sa'
password = 'sa' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=+database+';UID='+username=+';PWD='"password') #this may not be correct... 
cursor = cnxn.cursor() 


# to execute a query 

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 

# loop through the rowset (basically) 
while row: 
    print(row[0]) 
    row = cursor.fetchone() # fetch another ... welll.... row... 

