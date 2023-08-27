from unittest import TestCase

from stellar_model import EffectsResponse
from stellar_model.model.horizon.effects import BaseEffect
from tests.response import load_response_file


class TestEffectsResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("effects_response.json")
        parsed_data = EffectsResponse.model_validate(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 200)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, BaseEffect))

        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/effects?cursor=&limit=200&order=desc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/effects?cursor=151484153660260353-1&limit=200&order=desc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon.stellar.org/effects?cursor=151484175135092737-1&limit=200&order=asc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
