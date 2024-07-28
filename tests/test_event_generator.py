import pytest
from src.generator import generate_event

def test_generate_event():
    event = generate_event()
    
    # Check if all expected keys are present
    expected_keys = ['user_id', 'timestamp', 'product_id', 'category', 'price', 'quantity', 'is_purchase']
    assert all(key in event for key in expected_keys)
    
    # Check data types
    assert isinstance(event['user_id'], str)
    assert isinstance(event['timestamp'], int)
    assert isinstance(event['product_id'], str)
    assert isinstance(event['category'], str)
    assert isinstance(event['price'], float)
    assert isinstance(event['quantity'], int)
    assert isinstance(event['is_purchase'], bool)
    
    # Check value ranges
    assert 10 <= event['price'] <= 1000
    assert 1 <= event['quantity'] <= 5
    
    # Check category is one of the expected values
    assert event['category'] in ['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Toys']

@pytest.mark.parametrize("num_events", [1, 10, 100])
def test_multiple_events(num_events):
    events = [generate_event() for _ in range(num_events)]
    assert len(events) == num_events
    assert len(set(e['user_id'] for e in events)) == num_events  # All user_ids should be unique