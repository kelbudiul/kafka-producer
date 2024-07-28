import os

# Kafka connection details, with default values if environment variables are not set
KAFKA_BROKER = os.environ.get('KAFKA_BROKER', 'kafka:29092')
KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC', 'ecommerce_events')
SCHEMA_REGISTRY_URL = os.environ.get('SCHEMA_REGISTRY_URL', 'http://schema-registry:8081')

# Avro schema definition for e-commerce events
AVRO_SCHEMA = {
   "namespace": "com.example",
   "name": "EcommerceEvent",
   "type": "record",
   "fields" : [
     {"name" : "user_id", "type" : "string"},
     {"name" : "timestamp", "type" : "long"},
     {"name" : "product_id", "type" : "string"},
     {"name" : "category", "type" : "string"},
     {"name" : "price", "type" : "float"},
     {"name" : "quantity", "type" : "int"},
     {"name" : "is_purchase", "type" : "boolean"}
   ]
}

# Configuration for randomized sleep time between event generation
MIN_SLEEP_TIME = 0.1  # Minimum sleep time: 100 ms
MAX_SLEEP_TIME = 2.0  # Maximum sleep time: 2 seconds