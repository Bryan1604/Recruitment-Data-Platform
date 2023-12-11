from kafka import KafkaConsumer
import json
import sys

boostrap_server = ['127.0.0.1:9092']
topic_name = 'job_topic'

consumer = KafkaConsumer(
    group_id = 'group1',
    bootstrap_servers = ['127.0.0.1:9092'],
    auto_offset_reset = 'earliest'
)

consumer.subscribe(topic_name)

while 1==1:
    try:
        for message in consumer:
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
    except KeyboardInterrupt:
        sys.exit()
            
    