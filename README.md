# nosql4uspto
uspto patent data-pipeline for nosql system

### Environments
- OS: Ubuntu 16.04.4 LTS  
- Script language: Python 3.6.4 :: Anaconda custom (64-bit)  
- Database: MongoDB shell version v3.6.5

## 1. collect xml file from USPTO.
```$ python collect_weekly_xml.py {$YEAR}```

## 2. insert json file to MongoDB.
```$ python run_insert_mongo.py {$YEAR}```


 