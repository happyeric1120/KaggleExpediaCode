from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['DataAnalytics']
collection = db['train']

for trainRow in collection.find().batch_size(500000):  
    for key, val in trainRow.items():      
        if val == u'NULL': 
            trainRow[key] = None
            #print(key + ' has string "NULL"');

        collection.save(trainRow);