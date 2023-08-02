from pandas import DataFrame
from datetime import datetime

if "data_exporter" not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to filesystem.

    Docs: https://docs.mage.ai/design/data-loading#example-loading-data-from-a-file
    """
    now = datetime.now().isoformat(timespec="seconds")
    filepath = f"{now}_titanic_clean.csv"
    df.to_csv(f"files/{filepath}")
