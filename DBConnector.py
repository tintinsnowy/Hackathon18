from pymongo import MongoClient
import pickle

class DBConnector:
    _client = None
    _db = None
    _reader = None

    def __init__(self, host='localhost', port=27017):
        self._client = MongoClient(host, port)
        self._db = self._client['RFID']

    def __del__(self):
        self.close()

    def close(self):
        self._reader = None
        self._db = None
        self._client.close()
        self._client = None

    def selectReader(self, ip):
        if self._db == None:
            return

        self._reader = self._db['raw_data_' + ip]

    def getDistinctMeasurementIDs(self):
        return list(self._reader.distinct('measurement_uuid'))
        

    def getTagsGroupedByAnt(self, measurement_list):
        groups = [[],[],[],[]]
        for m in measurement_list:
            a = list(self._reader.find({"measurement_uuid":m},{"data.AntennaPort":1, "data.EPC":1}))
            groups[a[0]["data"]["AntennaPort"] & 0x3].append([d["data"]["EPC"] for d in a])

        return groups

db  = DBConnector()
db.selectReader("192.168.0.69")
measure = db.getDistinctMeasurementIDs()
g = db.getTagsGroupedByAnt(measure[:100])
with open("outfile", 'wb') as f:
    pickle.dump(g, f)
