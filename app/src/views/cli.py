import argparse, json
from app.src.services.discovery import discover_jellyfin_servers

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=float, default=4)
    ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--no-verify", action="store_true")
    args = ap.parse_args()

    servers = discover_jellyfin_servers(
        timeout=args.timeout, retries=args.retries, verify=not args.no_verify
    )
    print(json.dumps([s.__dict__ for s in servers], indent=2, default=str))

if __name__ == "__main__":
    main()
