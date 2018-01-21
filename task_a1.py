from DBConnector import DBConnector

db = DBConnector()
# db.selectReader("192.168.0.69")
#measure = db.getDistinctMeasurementIDs()
# g = db.getTagsGroupedByAnt(measure)

# with open("outfile", 'wb') as f:
    # pickle.dump(g, f)

# db.test()
db.selectReader("temp_1_1_0")
a = list(db.find({}))
feature_matrix = []
for tag in a:
    feature = {}
    for measure in tag["obs_by"][:1000]:
        #feature.update({measure["measurement_uuid"]:measure["RSSI"]})
        feature.update({measure["measurement_uuid"]:1})
    feature_matrix.append(feature)

from sklearn.feature_extraction import DictVectorizer
v = DictVectorizer(sparse=True)
x = v.fit_transform(feature_matrix)
#x = x.transpose()
# import sklearn
# from sklearn.metrics.pairwise import pairwise_distances
# dist_matrix = sklearn.metrics.pairwise.pairwise_distances(x)
# dist_matrix = pairwise_distances(x, metric='manhattan')
# print(dist_matrix)
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=30, min_samples=2, metric='manhattan').fit(x)
# core_samples_mask = np.zeros_like(dbscan.labels_, dtype=bool)
# core_samples_mask[dbscan.core_sample_indices_] = True

labels = dbscan.labels_

result = []
print(len(labels))
for i in range(len(labels)):
    result.append([a[i]["_id"], labels[i]])

print(result)

