from pymongo import MongoClient


# connection
conn = MongoClient("mongodb://IP") 
db = conn["DataBase_Name"]
collection = db.Collection_Name
for doc in collection.find() as fetch:
    for row in fetch:
    # print(row)  # fetch出來的結果是NoneType
    row = dict(row)  # 先將依序取出的檔案指定成dict資料型態
    # print(row)
    with open('Collection.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(row.values())
    f_object.close()  # 將dict轉檔成csv檔並且儲存關閉檔案
    
