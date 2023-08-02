from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from os import path


@data_exporter
def export_data_to_big_query(data: list, *args, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    df, table_name = data
    print(table_name)
    
    table_id = f"clcg-dataengineering.emergencies.{table_name}"
    config_path = path.join(get_repo_path(), "io_config.yaml")
    
    config_profile = "default"
    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        table_id,
        if_exists="replace",  # Specify resolution policy if table name already exists
    )
