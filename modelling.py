"""Churn prediction model."""

import argparse
from pathlib import Path

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=Path, required=True)
    parser.add_argument("--report_path", type=Path, required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.input_path)
    if "Churn_Yes" in df.columns:
        y = df["Churn_Yes"].astype(int)
        X = df.drop(columns=["Churn_Yes"], errors="ignore")
    elif "Churn" in df.columns:
        y = df["Churn"].astype(int)
        X = df.drop(columns=["Churn"], errors="ignore")
    else:
        raise ValueError("Expected 'Churn' or 'Churn_Yes' column.")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = GradientBoostingClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).T
    args.report_path.parent.mkdir(parents=True, exist_ok=True)
    report_df.to_csv(args.report_path)
    print(report_df)


if __name__ == "__main__":
    main()
