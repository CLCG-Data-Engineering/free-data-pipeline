import re
import pandas as pd

def parse_columns(df: pd.DataFrame) -> pd.DataFrame:
    def convert(name: str) -> str:
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).replace('.', '_').lower()
    
    return df.rename(columns=convert)


@transformer
def transform(df: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
    """Retrieves the df and modifies the column names"""
    df = parse_columns(df)
    return df
