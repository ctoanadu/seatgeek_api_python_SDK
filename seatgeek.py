import logging
import os

import dotenv
import requests

logger = logging.getLogger(__name__)


class SeatGeekResource:
    def __init__(self, base_url, client_id, client_secret):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.logger = logger

        logging.basicConfig(level=logging.INFO)

    def get_url(self, endpoint, id=None, city=None):
        if id:
            url = f"{self.base_url}{endpoint}/{id}?client_id={self.client_id}&client_secret={self.client_secret}"
            logging.info(url)
            return url
        elif city:
            url = f"{self.base_url}{endpoint}?city={city}?client_id={self.client_id}&client_secret={self.client_secret}"
            logging.info(url)
            return url
        else:
            url = f"{self.base_url}{endpoint}?client_id={self.client_id}&client_secret={self.client_secret}"
            logging.info(url)
            return url

    def get_response(self, get_url):
        response = requests.get(get_url)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code


class SeatGeekClient(SeatGeekResource):
    def get_all_events(self, endpoint):
        url = self.get_url(endpoint)
        return self.get_response(url)

    def get_event_by_id(self, endpoint, id):
        url = self.get_url(endpoint, id)
        return self.get_response(url)

    def get_events_by_location(self, endpoint, ip, range=None):
        if range:
            url = f"{self.get_url(endpoint)}?geoip={ip}&range={range}"
        else:
            url = f"{self.get_url(endpoint)}?geoip={ip}"
        return self.get_response(url)

    def get_all_perfromers(self, endpoint):
        url = self.get_url(endpoint)
        return self.get_response(url)

    def get_performer_by_id(self, endpoint, id):
        url = self.get_url(endpoint, id)
        return self.get_response(url)

    def get_all_venues(self, endpoint):
        url = self.get_url(endpoint)
        return self.get_response(url)

    def get_venues_by_id(self, endpoint, id):
        url = self.get_url(endpoint, id)
        return self.get_response(url)

    def get_venue_by_city(self, endpoint, city):
        url = f"{self.get_url(endpoint,city)}"
        return self.get_response(url)


if __name__ == "__main__":

    dotenv.load_dotenv()
    base_url = "https://api.seatgeek.com/2"
    client_id = os.environ["client_id"]
    client_secret = os.environ["client_secret"]

    seat_geek_client = SeatGeekClient(base_url, client_id, client_secret)
    print(seat_geek_client.get_event_by_id("/events", "6205386"))
