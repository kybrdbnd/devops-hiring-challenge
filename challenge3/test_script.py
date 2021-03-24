from .script import validate_input_json, validate_key_name, get_value


class TestJSON:
    def test_input_json(self):
        value = validate_input_json('{"a": {"b": "c"}}')
        assert value

    def test_input_json_1(self):
        value = validate_input_json('{"a": {"b"}}')
        assert value is not True

    def test_key_name(self):
        value = validate_key_name('a/b')
        assert value

    def test_key_name_1(self):
        value = validate_key_name('a/b/')
        assert value is not True

    def test_key_name_2(self):
        value = validate_key_name('/a/b')
        assert value is not True

    def test_key_name_3(self):
        value = validate_key_name('/a/b/')
        assert value is not True

    def test_get_value(self):
        value = get_value({"a": {"b": "c"}}, 'a')
        assert value is None

    def test_get_value_1(self):
        value = get_value({"a": {"b": "c"}}, 'a/b')
        assert value == 'c'

    def test_get_value_2(self):
        value = get_value({"a": {"b": "c"}}, 'a/b/c')
        assert value is None
