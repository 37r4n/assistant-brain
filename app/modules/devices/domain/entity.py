from dataclasses import dataclass
from typing import List
import uuid

@dataclass
class Device:
    id: str
    device_id: str
    name: str
    is_active: bool
    capabilities: List[str]

    @staticmethod
    def create(device_id: str, name: str, is_active: bool, capabilities: List[str]) -> "Device":
        return Device(
            id=str(uuid.uuid4()),
            device_id=device_id,
            name=name,
            is_active=is_active,
            capabilities=capabilities
        )
    
    @staticmethod
    def rebuild(id: str, device_id: str, name: str, is_active: bool, capabilities: List[str]) -> "Device":
        return Device(
            id=id,
            device_id=device_id,
            name=name,
            is_active=is_active,
            capabilities=capabilities
        )
