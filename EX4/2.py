import pymongo 

myclient  = pymongo.MongoClient("mongodb://localhost:27017/")
mydb =  myclient["mydatabase"]

mycol = mydb["customers"]

# finding documnets where address only starts with letter s 

myquery = {"address":{"$regex":"^K"}}

mydoc = mycol.find(myquery)

for x in mydoc:

    print(x)