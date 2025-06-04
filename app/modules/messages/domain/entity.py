from dataclasses import dataclass, field
from typing import Literal, Optional, Dict
from datetime import datetime, timezone
import uuid

@dataclass
class Message:
    id: str
    device_id: str
    content: Optional[str]
    role: Literal["user", "assistant", "system"]
    audio_url: Optional[str]
    function_call: Optional[Dict] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @staticmethod
    def create(device_id: str, content: Optional[str], role: Literal["user", "assistant", "system"], audio_url: Optional[str], function_call: Optional[Dict] = None) -> "Message":
        return Message(
            id=str(uuid.uuid4()),
            device_id=device_id,
            content=content,
            role=role,
            audio_url=audio_url,
            function_call=function_call or {},
            timestamp=datetime.now(timezone.utc)
        )
    
    @staticmethod
    def rebuild(id:str, device_id: str, content: Optional[str], role: Literal["user", "assistant", "system"], audio_url: Optional[str], timestamp: datetime, function_call: Optional[Dict] = None) -> "Message":
        return Message(
            id=id,
            device_id=device_id,
            content=content,    
            role=role,
            audio_url=audio_url,
            function_call=function_call or {},
            timestamp=timestamp
        )
