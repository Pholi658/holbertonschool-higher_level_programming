#!/usr/bin/python3
import requests
import csv
import json


def fetch_and_print_posts():

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url) 
    print(f"Status code: {response.status_code}")

    json_data = response.json() 
    for value in json_data:
        print(value["title"])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
 
    dict_list = json.loads(response.text)
    filtered_dict =[]

    for dict in dict_list:
        filtered_dict.append({
            "id": dict["id"],
            "title": dict["title"],
            "body": dict["body"]
        })
    headers = ["id","title","body"]

    with open('posts.csv','w',newline="" ) as f:
        write_csv = csv.DictWriter(f,fieldnames=headers)
        write_csv.writeheader()
        write_csv.writerows(filtered_dict)
        
