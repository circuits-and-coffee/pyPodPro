from dataclasses import dataclass
from typing import Optional, Tuple, Dict, Any

@dataclass
class JellyfinServer:
    base_url: str
    verified: bool = False
    from_addr: Optional[Tuple[str, int]] = None
    location_url: Optional[str] = None
    info: Optional[Dict[str, Any]] = None
