"""Download script for a public telecom churn dataset."""

import pathlib
import urllib.request


DATA_URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"


def main() -> None:
    root = pathlib.Path(__file__).resolve().parent
    raw_dir = root / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    target = raw_dir / "telco_churn.csv"

    if target.exists():
        print(f"File already exists at {target} (size={target.stat().st_size} bytes).")
        return

    print("Downloading telecom churn dataset...")
    print(f"URL: {DATA_URL}")
    print(f"Destination: {target}")
    urllib.request.urlretrieve(DATA_URL, target)
    print("Download finished.")
    print(f"Final size: {target.stat().st_size} bytes")


if __name__ == "__main__":
    main()
