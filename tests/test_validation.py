from etl.validate import validate_schema


def test_validate_schema_success():
    record = {"order_id": 1, "quantity": 2, "unit_price": 50}
    assert validate_schema(record) is True


def test_validate_schema_failure():
    record = {"order_id": 1, "quantity": 2}
    assert validate_schema(record) is False
