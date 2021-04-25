from unittest import TestCase

from stellar_model.model.horizon.root import Root
from stellar_model.response.root_response import RootResponse
from tests.response import load_horizon_file


class TestRootResponse(TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("root.json")
        parsed_data = RootResponse.parse_obj(raw_data)
        self.assertTrue(isinstance(parsed_data, RootResponse))
        self.assertTrue(isinstance(parsed_data, Root))
