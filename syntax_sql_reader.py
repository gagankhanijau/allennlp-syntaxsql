import json
from typing import Iterator, List, Dict

from allennlp.data.dataset_readers import DatasetReader
from allennlp.data import Instance


@DatasetReader.register("syntax_sql_reader")
class SyntaxSqlDatasetReader(DatasetReader):

    def __init__(self) -> None:
        super().__init__(lazy=False)
        
    def text_to_instance(self, input_json) -> Instance:
        instance=Instance(input_json)
        instance.indexed=True
        return instance

    def _read(self, file_path: str) -> Iterator[Instance]:
        data = json.load(open(file_path))
        for item in data[:]:
            yield self.text_to_instance(item)