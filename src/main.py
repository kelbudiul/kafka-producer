from .generator import generate_event
from .utils import create_avro_producer
from .config import KAFKA_TOPIC, MIN_SLEEP_TIME, MAX_SLEEP_TIME
import time
import random

def main():
    # Create an Avro producer
    avro_producer = create_avro_producer()

    while True:
        # Generate a random event
        event = generate_event()
        
        # Produce the event to Kafka
        avro_producer.produce(topic=KAFKA_TOPIC, value=event)
        
        # Ensure the event is sent
        avro_producer.flush()
        
        print(f"Sent event: {event}")
        
        # Sleep for a random time before generating the next event
        sleep_time = random.uniform(MIN_SLEEP_TIME, MAX_SLEEP_TIME)
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()