import logging

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class SeatGeekResource:
    """
    A class to interact with the SeatGeek API.

    Attributes:
        client_id (str): The client ID for accessing the API.
        client_secret (str): The client secret for accessing the API.
        base_url (str): The base URL for the SeatGeek API.
    """

    def __init__(self, client_id, client_secret, base_url="https://api.seatgeek.com/2"):
        """
        Initializes the SeatGeekResource with client ID, client secret, and base URL.

        Args:
            client_id (str): The client ID for accessing the API.
            client_secret (str): The client secret for accessing the API.
            base_url (str, optional): The base URL for the SeatGeek API. Defaults to "https://api.seatgeek.com/2".
        """
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.logger = logger

    def get_url(self, endpoint, id=None, city=None, datetime_utc=None):
        """
        Constructs the URL for the API endpoint.

        Args:
            endpoint (str): The endpoint of the API.
            id (str, optional): The ID of the resource. Defaults to None.
            city (str, optional): The city for filtering. Defaults to None.
            datetime_utc (str, optional): The UTC datetime for filtering. Defaults to None.

        Returns:
            str: The constructed URL.
        """

        if id:
            url = f"{self.base_url}{endpoint}/{id}?client_id={self.client_id}&client_secret={self.client_secret}"
            logging.info(url)
            return url
        elif city:
            url = f"{self.base_url}{endpoint}?city={city}?client_id={self.client_id}&client_secret={self.client_secret}"
            logging.info(url)
            return url
        elif datetime_utc:
            url = f"{self.base_url}{endpoint}?datetime_utc={datetime_utc}?client_id={self.client_id}&client_secret={self.client_secret}"
            logging.info(url)
            return url
        else:
            url = f"{self.base_url}{endpoint}?client_id={self.client_id}&client_secret={self.client_secret}"
            logging.info(url)
            return url

    def get_response(self, get_url):
        """
        Sends a GET request to the API endpoint and returns the response.

        Args:
            url (str): The URL of the API endpoint.

        Returns:
            dict: The JSON response from the API.
        """
        try:
            response = requests.get(get_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Request failed:{e}")
            return None


class SeatGeekClient(SeatGeekResource):
    """
    A client class for interacting with the SeatGeek API.
    Inherits from SeatGeekResource.

    Attributes:
        Inherits attributes from SeatGeekResource.
    """

    def get_all_events(self):
        """
        Retrieves all events from the SeatGeek API.

        Returns:
            dict: The JSON response containing all events.
        """
        endpoint = "/events"
        url = self.get_url(endpoint)
        return self.get_response(url)

    def get_event_by_id(self, id):
        """
        Retrieves an event by its ID from the SeatGeek API.

        Args:
            id (str): The ID of the event.

        Returns:
            dict: The JSON response containing the event details.
        """
        endpoint = "/events"
        url = self.get_url(endpoint, id)
        return self.get_response(url)

    def get_events_by_location(self, ip, range=None):
        """
        Retrieves events based on location from the SeatGeek API.

        Args:
            ip (str): The IP address for location detection.
            range (str, optional): The range for location filtering. Defaults to None.

        Returns:
            dict: The JSON response containing events based on location.
        """
        endpoint = "/events"
        if range:
            url = f"{self.get_url(endpoint)}?geoip={ip}&range={range}"
        else:
            url = f"{self.get_url(endpoint)}?geoip={ip}"
        return self.get_response(url)

    def get_all_performers(self):
        """
        Retrieves all performers from the SeatGeek API.

        Returns:
            dict: The JSON response containing all performers.
        """
        endpoint = "/performers"
        url = self.get_url(endpoint)
        return self.get_response(url)

    def get_performer_by_id(self, id):
        """
        Retrieves a performer by its ID from the SeatGeek API.

        Args:
            id (str): The ID of the performer.

        Returns:
            dict: The JSON response containing the performer details.
        """
        endpoint = "/performers"
        url = self.get_url(endpoint, id)
        return self.get_response(url)

    def get_all_venues(self):
        """
        Retrieves all venues from the SeatGeek API.

        Returns:
            dict: The JSON response containing all venues.
        """
        endpoint = "/venues"
        url = self.get_url(endpoint)
        return self.get_response(url)

    def get_venues_by_id(self, id):
        """
        Retrieves a venue by its ID from the SeatGeek API.

        Args:
            id (str): The ID of the venue.

        Returns:
            dict: The JSON response containing the venue details.
        """
        endpoint = "/venues"
        url = self.get_url(endpoint, id)
        return self.get_response(url)

    def get_venue_by_city(self, city):
        """
        Retrieves venues by city from the SeatGeek API.

        Args:
            city (str): The city for filtering venues.

        Returns:
            dict: The JSON response containing venues in the specified city.
        """
        endpoint = "/venues"
        url = self.get_url(endpoint, city)
        return self.get_response(url)

    def get_venue_by_date(self, datetime_utc):
        """
        Retrieves venues by date from the SeatGeek API.

        Args:
            datetime_utc (str): The UTC datetime for filtering venues.

        Returns:
            dict: The JSON response containing venues for the specified date.
        """
        endpoint = "/venues"
        url = self.get_url(endpoint, datetime_utc)
        return self.get_response(url)
