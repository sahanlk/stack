from stack.core import deep_merge


def test_deep_merge_simple():
    """Test merging two flat dictionaries."""
    dict_a = {"key1": "value1"}
    dict_b = {"key2": "value2"}

    result = deep_merge(dict_a, dict_b)

    assert result == {"key1": "value1", "key2": "value2"}


def test_deep_merge_overwrite():
    """Test that dict_b overwrites dict_a for shared keys."""
    dict_a = {"key1": "old"}
    dict_b = {"key1": "new"}

    result = deep_merge(dict_a, dict_b)

    assert result == {"key1": "new"}


def test_deep_merge_nested():
    """Test merging dictionaries with nested structures."""
    dict_a = {"database": {"host": "localhost", "port": 5432}}
    dict_b = {"database": {"host": "production-db"}, "debug": True}

    result = deep_merge(dict_a, dict_b)

    # Nested value should be updated, but other nested keys should remain
    assert result["database"]["host"] == "production-db"
    assert result["database"]["port"] == 5432
    assert result["debug"] is True
