%conn = mongo('localhost',27017,'RFID')
[data,str] = xlsread('.\EPC_Hashes.xlsx', 'A:E');
scatter3(data(:,2),data(:,3),data(:,4))
strJS = fileread('input.json');
jsonG = jsondecode(strJS);
