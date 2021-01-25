# payment-rule-transformer

## requirement

- python 3.8

### Case 1
- `pip install --user -r requirements.txt`

### Case 2(推薦)
- 安裝虛擬環境 `pip install virtualenv`
- 建立虛擬環境 `virtualenv -p <python3_path> venv`
- 進入虛擬環境 `source venv/bin/activate`
- 安裝lib `pip install --user -r requirements.txt`


## local-run
```
python app.py
```

## local-test
```
python -m unittest discover -s ./test --pattern '*.py'
```

## 備註
- 上版前，請更新requirements.txt
`pip freeze > requirements.txt`
- build docker image 指令
```
docker build . -t google_pipline
docker run google_pipline python app.py conf/application.yml {version}
```