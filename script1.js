conn = new Mongo();
db = conn.getDB("RFID");

//for (i = 0; i < 4; i++){
	//db["raw_data_192.168.0.69"].aggregate([{$match:{"data.AntennaPort" : {$mod:[4, i]}}},{$project:{EPC:"$data.EPC", measurement_uuid:1}}, {$out:"temp" + i.toString()}]);
//}

//db["temp3"].mapReduce(function(){emit(this.measurement_uuid, this.EPC);}, function(key, value){return {"result":value};}, {out:"temp3_new"})
//db["temp3"].aggregate([{$group:{_id: "$EPC", obs_by:{$push:"$measurement_uuid"}}}, {$out:"temp31"}], {allowDiskUse:true})
for (i = 0; i < 4; i++){
	db["raw_data_192.168.0.69"].aggregate([
		{$sort:{measurement_uuid:1}},
		{$match:{"data.AntennaPort" : {$mod:[4, i]}}},
		{$project:{RSSI:"$data.RSSI",EPC:"$data.EPC", measurement_uuid:1}}, 
		{$group:{_id: "$EPC", obs_by:{$push:{measurement_uuid:"$measurement_uuid", RSSI:"$RSSI"}}}},
		{$out:"temp_1_1_" + i.toString()}], 
		{allowDiskUse:true});
	db["temp"+ i.toString()].createIndex({_id: 1},{unique:true})
}

//for (i = 0; i < 4; i++){
	//db["raw_data_192.168.0.69"].aggregate([
		//{$match:{"data.AntennaPort" : {$mod:[4, i]}}},
		//{$group:{_id: "$data.EPC", count:{$sum:1}}},
		//{$out:"temp_3_1_" + i.toString()}], 
		//{allowDiskUse:true});
	//db["temp"+ i.toString()].createIndex({_id: 1},{unique:true})
//}
