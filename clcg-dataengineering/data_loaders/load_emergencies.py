import requests
import pandas as pd
import re


BASE_URL = "https://dataderden.cbs.nl/ODataApi/odata/47008NED"


@data_loader
def load_data(endpoint_info: dict, *args, **kwargs) -> pd.DataFrame:
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    url = f"{BASE_URL}/{endpoint_info['name']}"
    if endpoint_info["name"] == "TypedDataSet":
        url = f"{url}?$filter=Totaal_2 gt 0$&orderBy=Perioden desc&$top=9999"

    response = requests.get(url).json()
    df = pd.DataFrame(response.get("value"))

    return [df, endpoint_info["table_name"]]
