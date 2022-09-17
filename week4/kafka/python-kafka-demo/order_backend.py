import json
import time

# !package --> kafka-python
from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 15 

producer = KafkaProducer(bootstrap_servers="localhost:29092")
# Producer는 Kafka에게 데이터를 보내는 녀석
# Consumer는 Kafka로부터 데이터를 받는 녀석
# docker file에 보면 kafk는 29092번 포트를 사용하고 있음

print("Going to be generating order after 10 seconds")
print("Will generate one unique order every 10 seconds")
time.sleep(10)

for i in range(1, ORDER_LIMIT):
    data = {
        "order_id": i, 
        "user_id": f"blue_berry_{i}", # 여기 부터는 원래 front에서 받음
        "total_cost": i * 5, 
        "items": "raspberrypi, jetson",
    }

    producer.send(ORDER_KAFKA_TOPIC,
             json.dumps(data).encode("utf-8"))
    print(f"Done Sending..{i}")
    time.sleep(10)
