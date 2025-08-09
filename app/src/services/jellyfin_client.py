import urllib.request, json
from typing import Optional, Dict, Any

class JellyfinClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def _req(self, path: str) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        req = urllib.request.Request(url)
        if self.api_key:
            req.add_header("X-Emby-Token", self.api_key)  # Jellyfin honors Emby-style token
        with urllib.request.urlopen(req, timeout=5) as r:
            return json.loads(r.read().decode("utf-8", errors="replace"))

    def get_public_info(self):
        return self._req("/System/Info/Public")

    # Add more endpoints as you need tests for them...
