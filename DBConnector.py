from pymongo import MongoClient
import pymongo
import pickle
import numpy as np

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

    def selectReader(self, collection):
        if self._db == None:
            return

        self._reader = self._db[collection]

    def find(self, condi, proj=None):
        if (proj == None):
            return self._reader.find(condi)

        return self._reader.find(condi, proj)

    def distinct(self, field):
        return self._read.distinct(field)

    # def getDistinctMeasurementIDs(self):
        # return list(self._reader.distinct('measurement_uuid'))
        

    # def getTagsGroupedByAnt(self, measurement_list):
        # groups = [[],[],[],[]]
        # for m in measurement_list:
            # a = list(self._reader.find({"measurement_uuid":m},{"data.AntennaPort":1, "data.EPC":1}))
            # groups[a[0]["data"]["AntennaPort"] & 0x3].append([d["data"]["EPC"] for d in a])

        # return groups

    # def test(self):
        # # pymongo.collection.Collection(self._db, "zeros", True)
        # # coll = self._db['zeros']
        # # coll.insert_many([{'measurement_uuid':m,  "value":0} for m in measurement_list])
        # a = list(self._reader.aggregate([{"$match":{"data.EPC" : "c53217e28759b31e5db427319e24ae38"}},{"$project":{"measurement_uuid":1, "RSSI":"$data.RSSI"}}]))



db = DBConnector()
# db.selectReader("192.168.0.69")
#measure = db.getDistinctMeasurementIDs()
# g = db.getTagsGroupedByAnt(measure)

# with open("outfile", 'wb') as f:
    # pickle.dump(g, f)

# db.test()
# db.selectReader("temp_1_1_0")
# a = list(db.find({}))
# feature_matrix = []
# for tag in a:
    # feature = {}
    # for measure in tag["obs_by"][:1000]:
        # #feature.update({measure["measurement_uuid"]:measure["RSSI"]})
        # feature.update({measure["measurement_uuid"]:1})
    # feature_matrix.append(feature)

# from sklearn.feature_extraction import DictVectorizer
# v = DictVectorizer(sparse=True)
# x = v.fit_transform(feature_matrix)
# #x = x.transpose()
# # import sklearn
# # from sklearn.metrics.pairwise import pairwise_distances
# # dist_matrix = sklearn.metrics.pairwise.pairwise_distances(x)
# # dist_matrix = pairwise_distances(x, metric='manhattan')
# # print(dist_matrix)
# from sklearn.cluster import DBSCAN
# dbscan = DBSCAN(eps=30, min_samples=2, metric='manhattan').fit(x)
# # core_samples_mask = np.zeros_like(dbscan.labels_, dtype=bool)
# # core_samples_mask[dbscan.core_sample_indices_] = True

# labels = dbscan.labels_

# result = []
# print(len(labels))
# for i in range(len(labels)):
    # result.append([a[i]["_id"], labels[i]])

# print(result)
