from project.util.pipeline import Pipeline

class FeatureEngineeringPipeline(Pipeline):
    
    def __init__(self):
        Pipeline.__init(self, [
            PartnerFeature()
        ])