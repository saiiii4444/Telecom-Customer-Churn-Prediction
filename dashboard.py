"""Dashboard for telecom churn distribution."""

import argparse
from pathlib import Path

import pandas as pd
import plotly.express as px


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=Path, required=True)
    parser.add_argument("--output_path", type=Path, required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.input_path)
    if "Churn_Yes" in df.columns:
        target_col = "Churn_Yes"
    elif "Churn" in df.columns:
        target_col = "Churn"
    else:
        raise ValueError("Expected 'Churn' or 'Churn_Yes' column.")

    fig = px.histogram(df, x=target_col, title="Telecom Churn Distribution")
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(args.output_path)
    print(f"Dashboard saved to {args.output_path}")


if __name__ == "__main__":
    main()
