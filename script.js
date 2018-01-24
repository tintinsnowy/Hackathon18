conn = new Mongo();
db = conn.getDB("RFID");

var tags = ["c53217e28759b31e5db427319e24ae38","13e524cf416ebcea810f2d7ec305d4d7","d18f0b8dd7e32441ba30c2778578e9e2"]

for (i = 0; i < tags.length; i++){
	for (j = i + 1; j < tags.length; j++){
		db["raw_data_192.168.0.69"].aggregate([{$match:{"data.EPC" : tags[i]}},{$project:{measurement_uuid:1, RSSI:"$data.RSSI"}},{$out:"temp"}]);
		db["raw_data_192.168.0.69"].aggregate([{$match:{"data.EPC" : tags[j]}},{$project:{measurement_uuid:1, RSSI:"$data.RSSI"}},{$out:"temp"}]);
		db["temp"].mapReduce(function(){emit(this["measurement_uuid"], this["RSSI"]);}, function(key, values){if(values.length == 1) return values[0]; else return Math.abs(values[0] - values[1]);},{out:"result"});
		db["result"].aggregate([{$group:{_id:null, s:{$sum:"$value"}}},{$addFields:{left:tags[i], right:tags[j]}}, {$out:"final"}]);
		db.result.drop()
		db.temp.drop()
	}
}


