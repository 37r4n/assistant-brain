from dataclasses import dataclass
from typing import List
import uuid

@dataclass
class Software:
    id: str
    name: str
    version: str
    capabilities: List[str]

    @staticmethod
    def create(name: str, version: str, capabilities: List[str]) -> "Software":
        return Software(
            id=str(uuid.uuid4()),
            name=name,
            version=version,
            capabilities=capabilities
        )
    
    @staticmethod
    def rebuild(id: str, name: str, version: str, capabilities: List[str]) -> "Software":
        return Software(
            id=id,
            name=name,
            version=version,
            capabilities=capabilities
        )
