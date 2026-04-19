from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.anomaly import detect_anomalies
from pipeline.analyze import analyze_data
from pipeline.load import save_outputs

from reporting.insights import generate_insights
from reporting.excel_report import generate_excel_report

from utils.logger import setup_logger

logger = setup_logger()


def run_pipeline():
    try:
        logger.info("Pipeline started")

        df = extract_data()
        df = transform_data(df)

        if df is None:
            logger.warning("No new data. Pipeline stopped.")
            return

        anomalies = detect_anomalies(df)

        kpis, analysis = analyze_data(df, anomalies)

        save_outputs(df, analysis, anomalies)

        insights = generate_insights(kpis, analysis, anomalies)

        generate_excel_report(kpis, analysis, anomalies, insights)

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")


if __name__ == "__main__":
    run_pipeline()