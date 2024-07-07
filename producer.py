from typing import Dict, Any, List
from kafka import KafkaProducer
import json


def json_serializer(data: Dict[str, Any]) -> bytes:
    """
    Serialize the given dictionary into JSON formatted string and encode it to bytes.

    Parameters:
        data (Dict[str, Any]): Data to be serialized.

    Returns:
        bytes: The JSON string encoded in UTF-8 bytes format, suitable for sending over Kafka.
    """
    return json.dumps(data).encode("utf-8")


class Producer:
    """
    A Kafka producer class for sending messages to a Kafka topic.
    """
    
    def __init__(self, server: str, topic_name: str):
        """
        Initialize the Kafka producer with server configuration and topic.

        Parameters:
            server (str): The Kafka broker server URL.
            topic_name (str): The name of the Kafka topic to send messages to.
        """

        self.topic_name: str = topic_name
        self.producer: KafkaProducer = KafkaProducer(
            bootstrap_servers=[server],  # Kafka bootstrap server address
            value_serializer=json_serializer  # Serializer function for message data
        )

    def send_message(self, message: Dict[str, Any]) -> None:
        """
        Send a single message to the Kafka topic.

        Parameters:
            message (Dict[str, Any]): The message data to send.
        """

        self.producer.send(self.topic_name, value=message)
        self.producer.flush()# Ensure all messages are sent to the Kafka server
        print(f"Sent message: {message}")

    def send_messages_batch(self, messages: List[Dict[str, Any]]) -> None:
        """
        Send a batch of messages to the Kafka topic.

        Parameters:
            messages (List[Dict[str, Any]]): A list of message data to send.
        """
        for message in messages:
            self.producer.send(self.topic_name, value=message)
        self.producer.flush() # Ensure all messages are sent to the Kafka server
        print(f"Sent batch of messages: {len(messages)}")
