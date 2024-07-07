from time import sleep
from producer import Producer
from typing import Dict, Any
from utils import load_config
from generator import DataGenerator
import datetime


config: Dict[str, Any] = load_config()
kafka_config: Dict[str, Any] = config['kafka']
mode_config: Dict[str, Any] = config['mode']

producer: Producer = Producer(
    kafka_config['server'],
    kafka_config['topic_name']
)

# Load the schema path from configuration and initialize DataGenerator
schema_path = config['data_generator']['schema_path']
data_generator = DataGenerator(schema_path)

if __name__ == "__main__":
    while True:
        # Send messages based on the mode specified in configuration (single or batch)
        if mode_config['type'] == 'single':
            message = data_generator.generate_data(1)[0]  # Generate a single data record
            message['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            producer.send_message(message)
        elif mode_config['type'] == 'batch':
            messages = data_generator.generate_data(mode_config['batch_size'])  # Generate a batch of data records
            for msg in messages:
                msg['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            producer.send_messages_batch(messages)
        sleep(kafka_config['sleep_time'])  # Delay between message sends, configurable
