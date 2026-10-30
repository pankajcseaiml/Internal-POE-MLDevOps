# evidently_monitor.py
"""
Evidently AI Monitoring Tool Configuration
Step 12: Evaluates data drift and data quality between reference and current datasets,
generates an interactive HTML dashboard, and logs drift metrics.
"""
import os
import sys
import numpy as np
import pandas as pd


def generate_sample_data(n_samples: int = 150):
    """
    Generate baseline (reference) and production (current) datasets.
    Simulates production data drift on feature_1 to demonstrate monitoring capabilities.
    """
    np.random.seed(42)

    # Reference dataset (training / baseline distribution)
    reference_df = pd.DataFrame({
        "feature_1": np.random.normal(loc=10.0, scale=2.0, size=n_samples),
        "feature_2": np.random.normal(loc=50.0, scale=5.0, size=n_samples),
        "category": np.random.choice(["A", "B", "C"], size=n_samples, p=[0.5, 0.3, 0.2]),
        "prediction": np.random.choice([0, 1], size=n_samples)
    })

    # Current dataset (production distribution with simulated drift in feature_1)
    current_df = pd.DataFrame({
        "feature_1": np.random.normal(loc=14.5, scale=3.0, size=n_samples),  # Drifted mean
        "feature_2": np.random.normal(loc=50.2, scale=5.1, size=n_samples),  # Stable
        "category": np.random.choice(["A", "B", "C"], size=n_samples, p=[0.2, 0.4, 0.4]),  # Shifted categories
        "prediction": np.random.choice([0, 1], size=n_samples)
    })

    return reference_df, current_df


def run_evidently_monitoring(output_html: str = "evidently_report.html"):
    """
    Run Evidently drift and summary metrics report and save interactive HTML report.
    """
    print("==================================================")
    print("  Evidently AI Tool - Data & Model Monitoring     ")
    print("==================================================")

    ref_data, curr_data = generate_sample_data()
    print(f"[INFO] Reference dataset shape: {ref_data.shape}")
    print(f"[INFO] Current (production) dataset shape: {curr_data.shape}")

    # Import Report and Presets with compatibility fallback
    try:
        from evidently import Report
        from evidently.presets import DataDriftPreset, DataSummaryPreset
        presets = [DataDriftPreset(), DataSummaryPreset()]
    except (ImportError, AttributeError):
        try:
            from evidently.report import Report
            from evidently.metric_preset import DataDriftPreset, DataQualityPreset
            presets = [DataDriftPreset(), DataQualityPreset()]
        except ImportError:
            from evidently.legacy.report import Report
            from evidently.legacy.metric_preset import DataDriftPreset, DataQualityPreset
            presets = [DataDriftPreset(), DataQualityPreset()]

    print("[INFO] Computing Data Drift and Summary metrics...")
    report = Report(metrics=presets)

    report_result = report.run(reference_data=ref_data, current_data=curr_data)

    # Save to interactive HTML
    if hasattr(report_result, "save_html"):
        report_result.save_html(output_html)
    elif hasattr(report, "save_html"):
        report.save_html(output_html)

    print(f"[SUCCESS] Evidently report generated successfully: {output_html}")
    full_path = os.path.abspath(output_html)
    print(f"[REPORT LOCATION] {full_path}")
    print("==================================================")
    return full_path


if __name__ == "__main__":
    report_file = "evidently_report.html"
    if len(sys.argv) > 1:
        report_file = sys.argv[1]
    run_evidently_monitoring(report_file)
