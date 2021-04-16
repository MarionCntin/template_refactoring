from project.util.transformer import Transformer

class PartnerFeature(Transformer):

    def __init__(self, me_suffix='_me', partner_suffix='_partner'):
        Transformer.__init__(self)
        self.me_suffix = me_suffix
        self.partner_suffix = partner_suffix

    def transform(self, df):
        # CODE DU FEATURE ENGINEERING
        pass