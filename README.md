# NOSQL 4 USPTO
uspto patent data-pipeline for nosql system
--------------------------------------------
>
>
![image](https://www.commerce.gov/sites/commerce.gov/files/styles/scale_700w/public/media/images/branding/uspto_seal_full_color.jpg?itok=0CpME9vD)
>
>
## 프로젝트에서 중점사항
>
* 매년 150,000건 이상의 데이터를 issue하는 USPTO 빅데이터 활용
* 병렬구조로 수집하여 수집 속도를 향상시킴
* USPTO에서 자주 활용이되는 QUERY 위주의 test 및 비교
>
>
>
## 1. 데이터 소개 및 수집
>
### 1.1. 데이터 소개
>
- USPTO 데이터 2018년 1월 ~ 6월 18일까지의 데이터
- 총 162,238건의 데이터 (약 17GB)
>
>
### 1.2. 데이터 수집
>
1) 파일 수집 URL 생성
  * USPTO에 2002년 이후에 생성된 데이터들은 xml 파일형식으로 가져올 수 있음
  * 따라서, USPTO의 url에서 년도만(2002이후) 바꾸어 xml파일을 수집하는 형식으로 파이썬 문법 작성
  * 본 프로젝트에서는 실험적으로 2018년 1-6월까지의 약 6개월 데이터만 가져옴
>
>
2) zip을 풀어 xml 형태로 최종 수집
  * USPTO에 올려져 있는 파일들은 zip 형태로 되어 있음
  * 따라서, zip을 풀어서 xml 형태로 최종 수집
>
![image](https://user-images.githubusercontent.com/37169177/41616343-bcfe824e-7438-11e8-9a6a-ae6b8a9d5655.png)
>
>
## 2. 데이터 변환 및 결과
>
### 2.1. 데이터 변환 : XML -> JSON
>
* MongoDB에서 JSON과 같은 형식(BSON)이 사용 가능하기 때문에 XML을 JSON파일 형식으로 변환해야 함
>
>
### 2.2. 데이터 결과
>
> * a sample record () for each system (image)
>
>
### test query 
* title, assignee(=patent number), dates(priority, publication), legal status(patent application, granted patent), number of claims
> 
>



## Step Running.
### 0. Environments
- OS: Ubuntu 16.04.4 LTS  
- Script language: Python 3.6.4 :: Anaconda custom (64-bit)  
- Database: MongoDB shell version v3.6.5

### 1. collect xml file from USPTO.
```$ python collect_weekly_xml.py {$YEAR}```

### 2. insert json file to MongoDB.
```$ python run_insert_mongo.py {$YEAR}```


