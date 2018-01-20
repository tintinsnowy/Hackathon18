%conn = mongo('localhost',27017,'RFID')
[data,str] = xlsread('EPC_Hashes.xlsx', 'A:E');
