import json
from services.subscription_service import SubscriptionService

class AuthService:
    def __init__(self) -> None:
        with open("/tmp/data.json", "r") as file:
            self.users = json.load(file)

    def is_user_authenticated(self, email: str) -> bool:
        return email in self.users

    def is_user_authorized(self, email: str) -> bool:
        return SubscriptionService().is_user_subscribed(email)
    
    def verify_user(self, email: str) -> bool:
        return self.is_user_authenticated(email) and self.is_user_authorized(email)
