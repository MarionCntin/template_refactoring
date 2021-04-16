from project.util.transformer import Transformer

class Pipeline(Transformer):

    def __self__(self,transformers):
        Transformer.__init__(self)
        self.transformers = transformers

    def transform(self,df):
        for tr in self.transformers:
            df = tr.transform(df)
        return df