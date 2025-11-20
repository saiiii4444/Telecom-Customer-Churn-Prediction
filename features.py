"""Feature engineering for telecom churn."""

import argparse
from pathlib import Path

import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=Path, required=True)
    parser.add_argument("--output_path", type=Path, required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.input_path)
    df = pd.get_dummies(df, drop_first=True)
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output_path, index=False)
    print(f"Features saved to {args.output_path} (rows: {len(df)})")


if __name__ == "__main__":
    main()
