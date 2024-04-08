from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign


class InfluencerManagerApp:
    VALID_I = {"StandardInfluencer": StandardInfluencer, "PremiumInfluencer": PremiumInfluencer}
    VALID_C = {"LowBudgetCampaign": LowBudgetCampaign, "HighBudgetCampaign": HighBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []
        self.approved = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_I:
            return f"{influencer_type} is not an allowed influencer type."
        i = self._find_influencer_by_username(username)
        if i is None:
            new_inf = self.VALID_I[influencer_type](username, followers, engagement_rate)
            self.influencers.append(new_inf)
            return f"{username} is successfully registered as a {influencer_type}."
        return f"{username} is already registered."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_C:
            return f"{campaign_type} is not a valid campaign type."
        c = self._find_campaign_by_id(campaign_id)
        if c is None:
            new_cam = self.VALID_C[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(new_cam)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."
        return f"Campaign ID {campaign_id} has already been created."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        inf = self._find_influencer_by_username(influencer_username)
        if inf is None:
            return f"Influencer '{influencer_username}' not found."
        cam = self._find_campaign_by_id(campaign_id)
        if cam is None:
            return f"Campaign with ID {campaign_id} not found."
        if not cam.check_eligibility(inf.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."
        result = inf.calculate_payment(cam)
        if result > 0:
            self.approved.append(inf)
            cam.approved_influencers.append(inf)
            cam.budget -= result
            inf.campaigns_participated.append(cam)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_reached_followers = {}
        for campaign in self.campaigns:
            reached_followers = sum(
                influencer.reached_followers(campaign.TYPE) for influencer in campaign.approved_influencers)
            if reached_followers > 0:
                total_reached_followers[campaign] = reached_followers
        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = next((influencer for influencer in self.approved if influencer.username == username), None)
        if not influencer:
            return f"{username} has not participated in any campaigns."
        else:
            return influencer.display_campaigns_participated()


    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))
        campaign_info = "\n".join([f"  * Brand: {campaign.brand}, Total influencers:"
                                   f" {len(campaign.approved_influencers)},"
                                   f" Total budget: ${campaign.budget:.2f},"
                                   f" Total reached followers:"
                                   f" {self.calculate_total_reached_followers()[campaign]}"for campaign in sorted_campaigns])
        return f"$$ Campaign Statistics $$\n{campaign_info}"

    def _find_influencer_by_username(self, username):
        collection = [i for i in self.influencers if i.username == username]
        return collection[0] if collection else None

    def _find_campaign_by_id(self, campaign_id):
        collection = [c for c in self.campaigns if c.campaign_id == campaign_id]
        return collection[0] if collection else None

