from httptest.test_requests.decrypt.requests_decrypt import ApiRequest

class TestApiRequest():
    req_data = {
        "method": "get",
        "url": "http://0.0.0.0:999/demo1.txt",
        "headers": None,
        "encoding": "base64"
    }
    def test_send(self):
        ar=ApiRequest()
        print(ar.send(self.req_data))
