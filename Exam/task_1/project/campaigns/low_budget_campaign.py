from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    TYPE = "LowBudgetCampaign"
    BUDGET = 2500.0

    def __init__(self, campaign_id, brand, required_engagement):
        super().__init__(campaign_id, brand, LowBudgetCampaign.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate):
        return engagement_rate >= 0.9 * self.required_engagement