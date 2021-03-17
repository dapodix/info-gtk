import attr
import json5
from typing import List


@attr.dataclass
class TableData:
    no: str
    uraian: str
    data: str
    keterangan: str

    @classmethod
    def from_json5_list(cls, datas: str) -> List["TableData"]:
        results: List["TableData"] = list()
        for data in json5.loads(datas):
            results.append(cls(**data))
        return results
