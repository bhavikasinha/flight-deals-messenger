from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACC_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)

    def send_notif(self, city):
        txt_msg = f"-Low price alert! Only ₹{city.cheapest_price} from BLR to {city.iata_code} on 2026-08-01"
        message = self.client.messages.create(
            from_=f'whatsapp:+{os.getenv("TWILIO_FROM_WHATSAPP")}',
            body=txt_msg,
            to=f'whatsapp:+{os.getenv("TWILIO_TO_WHATSAPP")}'
        )

        print(message.status)