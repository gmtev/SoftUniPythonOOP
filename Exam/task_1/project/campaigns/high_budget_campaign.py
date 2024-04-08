from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    TYPE = "HighBudgetCampaign"
    BUDGET = 5000.0

    def __init__(self, campaign_id, brand, required_engagement):
        super().__init__(campaign_id, brand, HighBudgetCampaign.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate):
        return engagement_rate >= 1.2 * self.required_engagement
