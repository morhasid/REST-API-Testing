import json
import requests
import responses
import random


class ClientGetRequest:
    NUMBERS_TO_GUESS = 6
    MIN_GUESS = 1
    MAX_GUESS = 37
    MIN_GUESS_STRONG = 1
    MAX_GUESS_STRONG = 7
    STATUS_OK = 200
    BASE_URL = 'https://loto.org'
    PATH = '/result'
    WINNING_NUMBERS = [5, 22, 1, 31, 9, 17]

    @staticmethod
    @responses.activate
    def get_response():
        def request_callback(request):
            numbers, strong = generate_response_from()
            resp_body = {"value": {'numbers': numbers, 'strong': [strong]}}
            return ClientGetRequest.STATUS_OK, {}, json.dumps(resp_body)

        responses.add_callback(
            responses.GET, ClientGetRequest.BASE_URL + ClientGetRequest.PATH,
            callback=request_callback,
            content_type="application/json",
        )

        def generate_response_from():
            numbers = ClientGetRequest.WINNING_NUMBERS
            while numbers == ClientGetRequest.WINNING_NUMBERS:
                # number != WINNING_NUMBERS, no future WIN
                numbers = random.sample(range(ClientGetRequest.MIN_GUESS, ClientGetRequest.MAX_GUESS)
                                        , ClientGetRequest.NUMBERS_TO_GUESS)
            strong = random.randint(ClientGetRequest.MIN_GUESS_STRONG, ClientGetRequest.MAX_GUESS_STRONG)
            return numbers, strong

        response = requests.get(ClientGetRequest.BASE_URL + ClientGetRequest.PATH)
        return response

