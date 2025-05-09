import json
from datetime import datetime, timedelta

class SubscriptionService:
    def __init__(self):
        with open("data.json", "r+") as file:
            self.subscriptions = json.load(file)

    def is_user_subscribed(self, email: str) -> bool:
        return self.subscriptions[email]["subscribed"] and not self.is_subscription_exhausted(
            email
        )
    
    def is_subscription_exhausted(self, email: str) -> bool:
        subscription_exhausted = False

        if datetime.now() - datetime.strptime(
            self.subscriptions[email]["subscription_updated"], "%d-%m-%Y %H:%M:%S"
        ) > timedelta(days=30):
            self.subscriptions[email]["subscribed"] = False
            subscription_exhausted = True

            with open("data.json", "w+") as file:
                json.dump(self.subscriptions, file)
        
        return subscription_exhausted
