import sys
import os
import pandas as pd
import pymongo
import json
import pathlib

def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['sanofi']
    collection_name = 'sanofi'
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
  for file in os.listdir(str(pathlib.Path().absolute())+ "/Source/csv/"):
        if file.endswith(".csv"):
          filepath = str(pathlib.Path().absolute())+ "/Source/csv/" + file
          import_content(filepath)
          base = os.path.splitext(file)[0]
          os.rename(str(pathlib.Path().absolute())+ "/Source/csv/"+file, str(pathlib.Path().absolute())+ "/Source/csv/"+base + ".lido")
          os.rename(str(pathlib.Path().absolute())+ "/Source/"+base+".dbc", str(pathlib.Path().absolute())+ "/Source/"+base + ".dbc" + ".convertido")
          os.rename(str(pathlib.Path().absolute())+ "/Source/"+base+".dbf", str(pathlib.Path().absolute())+ "/Source/"+base + ".dbf" + ".convertido")


