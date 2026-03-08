from extract import extract_data
from transform import transform_data
from load import load_data
from anomaly_detection import detect_anomalies
from visualization import plot_returns
def run_pipeline():

    print("Extracting data...")
    data = extract_data()

    print("Transforming data...")
    transformed_data = transform_data(data)

    print("Detecting anomalies...")
    detect_anomalies(transformed_data)

    print("Visualizing data...")
    plot_returns(transformed_data)

    print("Loading data...")
    load_data(transformed_data)
    print("ETL Pipeline Completed!")



if __name__ == "__main__":
    run_pipeline()


data = extract_data()

if data.empty:
    print("No data extracted. Pipeline stopped.")
