
fileName=str(input('File Name-> '))
#file1 = str(input('json File Name.json-> '))
#file2 = str(input('CSV File Name.csv-> '))

file1 = fileName+ ".json"
file2 = fileName+".csv"
topName = str(input('Array Name-> '))

import json
import csv
 

                   
with open(file1) as json_file: 
    data = json.load(json_file) 
  
order_data = data[topName] 
  

data_file = open(file2, 'w') 
   
csv_writer = csv.writer(data_file) 
  

count = 0
  
for orderId in order_data: 
    if count == 0: 
  
        
        header = orderId.keys() 
        csv_writer.writerow(header) 
        count += 1
  

    csv_writer.writerow(orderId.values()) 
  
data_file.close()
