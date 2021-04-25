from unittest import TestCase

from stellar_model import PathsResponse
from stellar_model.model.horizon.path import Path
from tests.response import load_response_file


class TestPathsResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("paths_response.json")
        parsed_data = PathsResponse.parse_obj(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 5)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, Path))
