import pymongo

client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_tab = walden['sheet_tab']

path = '/home/lau/PycharmProjects/python-web-crawlers/mongodb/walden.txt'
with open(path,'r') as f:
    linse = f.readlines()
    for index,line in enumerate(linse):
        data = {
            'index':index,
            'line' :line,
            'words':len(line.split())
        }
        sheet_tab.insert_one(data)
for item in sheet_tab.find({'words':{'$lt':5}}):
    print(item)




