# seatgeek_api_python_SDK
This package provides you with an easy way to interact with the SEATGEEK API in your Python applications.

# SeatGeek API Wrapper

This Python package serves as a wrapper for the SeatGeek API, providing convenient methods for accessing various resources such as events, performers, and venues.

## Installation

To install the SeatGeek API wrapper, you can use pip:

```bash
pip install seatgeek-wrapper
```

## Usage

```python
from seatgeek_wrapper import SeatGeekClient

# Initialize the SeatGeek client with your API credentials
client = SeatGeekClient(client_id='your_client_id', client_secret='your_client_secret')

# Example: Get all events
events = client.get_all_events()
print(events)

# Example: Get event by ID
event_details = client.get_event_by_id(id='event_id')
print(event_details)

# Example: Get events by location
events_by_location = client.get_events_by_location(ip='127.0.0.1', range='10mi')
print(events_by_location)

# Other methods follow a similar pattern
```

## Documentation

### SeatGeekResource Class

This class provides methods for constructing URLs and making API requests.

#### Initialization

```python
SeatGeekResource(client_id, client_secret, base_url="https://api.seatgeek.com/2")
```

- `client_id` (str): Your SeatGeek API client ID.
- `client_secret` (str): Your SeatGeek API client secret.
- `base_url` (str, optional): Base URL for the SeatGeek API.

#### Methods

- `get_url(endpoint, id=None, city=None, datetime_utc=None)`: Constructs the URL for the API endpoint.
- `get_response(url)`: Sends a GET request to the API endpoint and returns the response.

### SeatGeekClient Class

This class extends SeatGeekResource and provides additional methods for accessing specific resources like events, performers, and venues.

#### Methods

- `get_all_events()`: Retrieves all events.
- `get_event_by_id(id)`: Retrieves an event by its ID.
- `get_events_by_location(ip, range=None)`: Retrieves events based on location.
- `get_all_performers()`: Retrieves all performers.
- `get_performer_by_id(id)`: Retrieves a performer by its ID.
- `get_all_venues()`: Retrieves all venues.
- `get_venues_by_id(id)`: Retrieves a venue by its ID.
- `get_venue_by_city(city)`: Retrieves venues by city.
- `get_venue_by_date(datetime_utc)`: Retrieves venues by date.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
