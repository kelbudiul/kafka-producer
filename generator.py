from faker import Faker
from typing import List, Dict, Any
import random
import tomllib


class DataGenerator:
    """
    A class to generate synthetic data based on a dynamic schema defined in a configuration file.
    """

    def __init__(self, schema_path: str):
        """
        Initialize the DataGenerator with a path to the schema configuration file.

        Parameters:
            schema_path (str): The path to the schema configuration file.
        """
        self.fake = Faker()  # Initialize a Faker generator instance.
        # Load the schema from the specified TOML file.
        with open(schema_path, "rb") as schema_file:
            self.schema = tomllib.load(schema_file)

    def generate_data(self, num_records: int = 1) -> List[Dict[str, Any]]:
        """
        Generate synthetic data based on the loaded schema for a given number of records.

        Parameters:
            num_records (int): Number of records to generate.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, each representing a generated data record.
        """
        data = []
        for _ in range(num_records):
            record = {}
            for field in self.schema['fields']:
                # Generate data based on field type specified in schema.
                if field['type'] == 'name':
                    record[field['name']] = self.fake.first_name()
                elif field['type'] == 'surname':
                    record[field['name']] = self.fake.last_name()
                elif field['type'] == 'company':
                    record[field['name']] = self.fake.company()
                elif field['type'] == 'salary':
                    record[field['name']] = round(random.uniform(field['min'], field['max']), 2)
                elif field['type'] == 'integer':
                    record[field['name']] = random.randint(field['min'], field['max'])
                elif field['type'] == 'integer':
                    record[field['name']] = random.randint(field['min'], field['max'])
                elif field['type'] == 'url':
                    record[field['name']] = self.fake.url()
            data.append(record)
        return data
