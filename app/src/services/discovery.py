import socket, time, json, urllib.request, urllib.parse
from typing import List
from models.server import JellyfinServer

SSDP_ADDR = ("239.255.255.250", 1900)
MSEARCH = (
    "M-SEARCH * HTTP/1.1\r\n"
    "HOST: 239.255.255.250:1900\r\n"
    "MAN: \"ssdp:discover\"\r\n"
    "MX: 2\r\n"
    "ST: urn:schemas-upnp-org:device:MediaServer:1\r\n"
    "\r\n"
).encode("ascii")

def _parse_headers(raw_text: str):
    headers = {}
    for line in raw_text.split("\r\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            headers[k.strip().upper()] = v.strip()
    return headers

def _base_from_location(location: str) -> str:
    u = urllib.parse.urlparse(location)
    return f"{u.scheme}://{u.netloc}"

def discover_jellyfin_servers(timeout=3.0, retries=2, verify=True) -> List[JellyfinServer]:
    # Send SSDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try: sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    except OSError: pass
    sock.bind(("", 0))
    sock.settimeout(timeout)

    for _ in range(retries):
        sock.sendto(MSEARCH, SSDP_ADDR)
        time.sleep(0.2)

    hits = []
    deadline = time.time() + timeout
    while True:
        remaining = deadline - time.time()
        if remaining <= 0: break
        sock.settimeout(remaining)
        try:
            data, addr = sock.recvfrom(65535)
        except socket.timeout:
            break
        text = data.decode("latin-1", errors="replace")
        headers = _parse_headers(text)
        loc = headers.get("LOCATION")
        if not loc: 
            continue
        base = _base_from_location(loc)
        # print(f"any(hit.location_url == base for hit in hits) returns {any(hit.base_url == base for hit in hits)}")
        if not any(hit.base_url == base for hit in hits):
            # print(f"Couldn't find {base}, adding it!")
            hits.append(JellyfinServer(base_url=base, from_addr=addr, location_url=loc))
    sock.close()

    if verify:
        for s in hits:
            try:
                with urllib.request.urlopen(f"{s.base_url}/System/Info/Public", timeout=2) as r:
                    if r.status == 200:
                        data = json.loads(r.read().decode("utf-8", errors="replace"))
                        if str(data.get("ProductName", "")).lower().startswith("jellyfin"):
                            s.verified = True
                            s.info = data
            except Exception:
                pass
    return hits
