from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from .config import KAFKA_BROKER, SCHEMA_REGISTRY_URL, AVRO_SCHEMA

def create_avro_producer():
    """
    Create and return an AvroProducer instance.
    """
    # Convert the AVRO_SCHEMA dictionary to a schema string
    value_schema = avro.loads(str(AVRO_SCHEMA))
    
    # Create and return an AvroProducer with the specified configuration
    return AvroProducer({
        'bootstrap.servers': KAFKA_BROKER,
        'schema.registry.url': SCHEMA_REGISTRY_URL
    }, default_value_schema=value_schema)