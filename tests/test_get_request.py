import unittest
from src.client_get_request import ClientGetRequest


class ClientGetRequestTest(unittest.TestCase):
    # action
    response = ClientGetRequest.get_response()

    def test_get_request_api_aspects(self):
        # assume
        status_expected = ClientGetRequest.STATUS_OK
        header_content_type_expected = "application/json"

        # expect/assert
        self.assertEqual(self.response.status_code, status_expected)
        self.assertEqual(self.response.headers["Content-Type"], header_content_type_expected)

    def test_get_request_existing_fields(self):
        # action
        value = self.response.json()

        # expect/assert
        self.assertIn('value', value)
        self.assertIn('numbers', value['value'])
        self.assertIn('strong', value['value'])

    def test_get_request_fields_length(self):
        # action
        value = self.response.json()
        numbers, strong = value['value']['numbers'], value['value']['strong']

        # assume
        elements_in_value = 2
        elements_in_strong = 1
        elements_in_numbers = ClientGetRequest.NUMBERS_TO_GUESS

        # expect/assert
        self.assertEqual(len(value['value']), elements_in_value)
        self.assertEqual(len(strong), elements_in_strong)
        self.assertEqual(len(numbers), elements_in_numbers)

    def test_get_request_functionality(self):
        # action
        value = self.response.json()
        numbers, strong = value['value']['numbers'], value['value']['strong']

        # expect/assert
        self.assertTrue(ClientGetRequest.MIN_GUESS_STRONG <= strong[0] <= ClientGetRequest.MAX_GUESS_STRONG)
        self.assertTrue(len(numbers) == len(set(numbers)))  # no duplications
        self.assertTrue(all(ClientGetRequest.MIN_GUESS <= num <= ClientGetRequest.MAX_GUESS for num in numbers))
        self.assertTrue(numbers != ClientGetRequest.WINNING_NUMBERS)


if __name__ == '__main__':
    unittest.main()
