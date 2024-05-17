import requests
import csv
import json

engin = ['data/engins.csv', '/engins/add']

base_url = 'http://127.0.0.1:8000'

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

def insert_data(entite):
    datas = extract_data_csv(entite[0])
    url = base_url+entite[1]
    print(f'URL = {url}')
    for data in datas:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            print(f'success: {response.text}')
        else:
            print(f'Error status: {response.status_code}, {response.text}')


def extract_data_csv(file):
    with open(file, newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        result = []
        for row in rows:
            for k, v in row.items():
                if v == '':
                    row[k] = None
            result.append(row)
    return result

print(insert_data(engin))
