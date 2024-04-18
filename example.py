import os 
import dotenv
from seatgeek import SeatGeekClient

dotenv.load_dotenv()
client_id = os.environ["client_id"]
client_secret = os.environ["client_secret"]

seat_geek_client = SeatGeekClient(client_id, client_secret)
#print(seat_geek_client.get_event_by_id("6205386"))
print(seat_geek_client.get_all_events())
