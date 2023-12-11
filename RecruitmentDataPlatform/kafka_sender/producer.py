from kafka import KafkaProducer
from time import time
from faker import Faker
import json, time
import jsonlines

faker = Faker()

# def get_file() :
    # return {
    #     'name': faker.name(),
    #     'year' : faker.year()
    # }
    # filepath = "jobList.jsonl"
    # f = open(filepath) 
    # data = json.load(f)
    # return data
    
input_jsonl_file = 'companyList.jsonl'  
output_json_file = 'companyList.json'

#tranfer jsonl file to json file
with open(input_jsonl_file, 'r', encoding='utf-8') as jsonl_file, open(output_json_file, 'w', encoding='utf-8') as json_file:
    # Create a list to store the JSONL records
    json_data = []

    # Read each line in the JSONL file and append it to the list
    with jsonlines.Reader(jsonl_file) as reader:
        for record in reader:
            json_data.append(record)

    # Write the list as a JSON array to the output JSON file
    json.dump(json_data, json_file, indent=4)
    

def get_file() :
    filepath = "companyList.json"
    f = open(filepath) 
    data = json.load(f)
    return data

def get_partitioner(key_bytes, all_partitions, available_partitions):
    return 0

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers = ['127.0.0.1:9092'], # server name
    value_serializer = json_serializer # function callable
)

while 1==1:
    data = get_file()
    for element in data:
        print(element)
        producer.send(
            'job_topic',element
        )
        time.sleep(3)