from dataclasses import dataclass
from typing import List, Optional
import uuid

@dataclass
class Skill:
    id: str
    name: str
    description: str
    version: str
    file_url: Optional[str]
    is_enabled: bool
    required_capabilities: List[str]
    tags: List[str]

    @staticmethod
    def create(name: str, description: str, version: str, file_url: Optional[str], is_enabled: bool,
               required_capabilities: List[str], tags: List[str]) -> "Skill":
        return Skill(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            version=version,
            file_url=file_url,
            is_enabled=is_enabled,
            required_capabilities=required_capabilities,
            tags=tags
        )
    
    @staticmethod
    def rebuild(id: str, name: str, description: str, version: str, file_url: Optional[str], is_enabled: bool,
                required_capabilities: List[str], tags: List[str]) -> "Skill":
        return Skill(
            id=id,
            name=name,
            description=description,
            version=version,
            file_url=file_url,
            is_enabled=is_enabled,
            required_capabilities=required_capabilities,
            tags=tags
        )
