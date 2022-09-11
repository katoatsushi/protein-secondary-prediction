import csv
# csvの読み込み
path = { 'source': '../../DATA/one_str_input.csv', 'target': '../../DATA/one_str_output.csv'}
f = open(path['source'], 'r',encoding="utf-8")
source_rows = csv.reader(f)
SOURCE_DATA = [ row[:-1] for row in  list(source_rows)] # encorderに入力するもの

f = open(path['target'], 'r',encoding="utf-8")
target_rows = csv.reader(f)
TARGET_DATA = [ row[:-1] for row in  list(target_rows)] # decorderに入力するもの

source_datas = SOURCE_DATA
target_datas = TARGET_DATA

result = []
for source, target in zip(SOURCE_DATA, TARGET_DATA):
    source = "".join(source)
    target = " ".join(target)
    result.append([source, target])

with open('../../DATA/main.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(result)
