from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.anomaly import detect_anomalies
from pipeline.analyze import analyze_data
from pipeline.load import save_outputs

from reporting.insights import generate_insights
from reporting.excel_report import generate_excel_report


def run_pipeline():
    df = extract_data()
    df = transform_data(df)

    if df is None:
        print("[INFO] No new data. Pipeline stopped.")
        return

    anomalies = detect_anomalies(df)

    kpis, analysis = analyze_data(df, anomalies)

    # Save intermediate outputs
    save_outputs(df, analysis, anomalies)

    # Generate insights
    insights = generate_insights(kpis, analysis, anomalies)

    # Generate final report
    generate_excel_report(kpis, analysis, anomalies, insights)


if __name__ == "__main__":
    run_pipeline()
