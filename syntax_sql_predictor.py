from overrides import overrides

from allennlp.common.util import JsonDict
from allennlp.data import Instance
from allennlp.predictors.predictor import Predictor


@Predictor.register('syntax_sql_predictor')
class SyntaxSqlPredictor(Predictor):

    def predict(self, item) -> JsonDict:
        return self.predict_json(item)

    @overrides
    def _json_to_instance(self, json_dict: JsonDict) -> Instance:
        return self._dataset_reader.text_to_instance(item)