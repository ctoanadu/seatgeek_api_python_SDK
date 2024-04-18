import logging
import requests


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



class SeatGeekResource:
    def __init__(self, client_id, client_secret, base_url="https://api.seatgeek.com/2"):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.logger = logger


    def get_url(self, endpoint, id=None, city=None ,datetime_utc=None):
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
        try:
            response = requests.get(get_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f'Request failed:{e}')
            return None 
        


class SeatGeekClient(SeatGeekResource):
    def get_all_events(self):
        endpoint='/events'
        url = self.get_url(endpoint)
        return self.get_response(url)

    def get_event_by_id(self, id):
        endpoint='/events'
        url = self.get_url(endpoint, id)
        return self.get_response(url)

    def get_events_by_location(self,ip, range=None):
        endpoint='/events'
        if range:
            url = f"{self.get_url(endpoint)}?geoip={ip}&range={range}"
        else:
            url = f"{self.get_url(endpoint)}?geoip={ip}"
        return self.get_response(url)

    def get_all_performers(self):
        endpoint='/performers'
        url = self.get_url(endpoint)
        return self.get_response(url)

    def get_performer_by_id(self,id):
        endpoint='/performers'
        url = self.get_url(endpoint, id)
        return self.get_response(url)

    def get_all_venues(self):
        endpoint='/venues'
        url = self.get_url(endpoint)
        return self.get_response(url)

    def get_venues_by_id(self, id):
        endpoint='/venues'
        url = self.get_url(endpoint, id)
        return self.get_response(url)

    def get_venue_by_city(self,city):
        endpoint='/venues'
        url = self.get_url(endpoint,city)
        return self.get_response(url)

    def get_venue_by_date(self,datetime_utc):
        endpoint='/venues'
        url = self.get_url(endpoint,datetime_utc)
        return self.get_response(url)





