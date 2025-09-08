import json
import os
import urllib.request
import urllib.error

API_URL = "https://api.bolsadesantiago.com/v1/acciones"


def fetch_actions(token: str) -> str:
    """Fetches actions data from the Bolsa de Santiago API."""
    req = urllib.request.Request(API_URL)
    req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8")


def main() -> None:
    token = os.getenv("BOLSASANTIAGO_TOKEN")
    if not token:
        print("Set the BOLSASANTIAGO_TOKEN environment variable with your API token.")
        return
    try:
        data = fetch_actions(token)
        print(data)
    except urllib.error.HTTPError as err:
        print(f"HTTP error {err.code}: {err.reason}")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
