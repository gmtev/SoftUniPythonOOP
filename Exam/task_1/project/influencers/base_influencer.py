from abc import ABC, abstractmethod
from project.campaigns.base_campaign import BaseCampaign


class BaseInfluencer(ABC):
    TYPE = ""

    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated = []
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if value.strip() == "":
            raise ValueError("Username cannot be empty or consist only of whitespace!")
        self.__username = value

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, value):
        if value < 0:
            raise ValueError("Followers must be a non-negative integer!")
        self.__followers = value

    @property
    def engagement_rate(self):
        return self.__engagement_rate

    @engagement_rate.setter
    def engagement_rate(self, value):
        if not 0 <= value <= 5:
            raise ValueError("Engagement rate should be between 0 and 5.")
        self.__engagement_rate = value

    @abstractmethod
    def calculate_payment(self, campaign: BaseCampaign):
        pass

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        pass

    def display_campaigns_participated(self) -> str:
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."

        campaigns_info = "\n".join([
                                       f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, Reached followers: {self.reached_followers(type(campaign).__name__)}"
                                       for campaign in self.campaigns_participated])
        return f"{type(self).__name__} :) {self.username} :) participated in the following campaigns:\n{campaigns_info}"