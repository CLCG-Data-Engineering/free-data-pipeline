from mage_ai.orchestration.run_status_checker import check_status

if "sensor" not in globals():
    from mage_ai.data_preparation.decorators import sensor


@sensor
def check_condition(*args, **kwargs) -> bool:
    """
    Template code for checking if block or pipeline run completed.
    """
    return check_status(
        "example_pipeline",
        kwargs["execution_date"],
        block_uuid="sleep_20_seconds",
    )
