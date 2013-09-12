from pymongo import MongoClient
import csv
import random

def runRandomSort():

    client = MongoClient('localhost', 27017)
    db = client['DataAnalytics']
    collection = db['test']

    currentSearchId = None
    propertyIds = []

    with open('D:/Course Material(note in Google Drive)/IS2725/term_project/basicPythonBenchmark/randomBenchmark.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['SearchId', 'PropertyId'])
        
        for benchRow in collection.find():
  
            searchId = benchRow['srch_id']
            propertyId = benchRow['prop_id']

            if(searchId != currentSearchId):
                
                writeUserSort(currentSearchId, propertyIds, writer)
                
                currentSearchId = searchId
                propertyIds = [currentSearchId]
            else:
                propertyIds.append(propertyId)

        writeUserSort(currentSearchId, propertyIds, writer)


def writeUserSort(currentSearchId, propertyIds, csvwriter):

    if(currentSearchId == None): return

    #shuffle array and write to csv file
    random.shuffle(propertyIds)
    for r_pid in propertyIds:
        csvwriter.writerow([currentSearchId] + [r_pid])

runRandomSort()