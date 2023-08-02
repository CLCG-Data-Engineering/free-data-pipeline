if "custom" not in globals():
    from mage_ai.data_preparation.decorators import custom
if "test" not in globals():
    pass


@custom
def transform_custom(*args, **kwargs):
    """Being used as a dynamic block to run the endpoints in parallel
    Returns:

    """
    endpoints = [
        {"name": "TableInfos", "table_name": "info"},
        {"name": "TypedDataSet", "table_name": "emergencies"},
        {"name": "DataProperties", "table_name": "properties"},
        {"name": "RegioS", "table_name": "regions"},
        {"name": "Perioden", "table_name": "periods"},
    ]
    return [endpoints]
