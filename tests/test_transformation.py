import pandas as pd
from etl.transform import transform_data

def test_total_amount_calculation():
    df = pd.DataFrame({
        "quantity": [2, 3],
        "price": [10.0, 20.0]
    })

    result = transform_data(df)

    assert "total_amount" in result.columns
    assert result["total_amount"].iloc[0] == 20.0
    assert result["total_amount"].iloc[1] == 60.0
