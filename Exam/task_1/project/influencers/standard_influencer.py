from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    TYPE = "StandardInfluencer"
    INITIAL_PAYMENT = 0.45

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign):
        payment = campaign.budget * self.INITIAL_PAYMENT
        return payment

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            reached = (self.followers * self.engagement_rate) * 1.2
        elif campaign_type == "LowBudgetCampaign":
            reached = (self.followers * self.engagement_rate) * 0.9
        return round(reached)