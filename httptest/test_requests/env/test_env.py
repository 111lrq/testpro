from httptest.test_requests.env.env_demo import Api


class TestEnv:
    data = {
        "method":"get",
        "url": "http://testing-studio:999/demo1.txt",
        "headers": None,
    }
    def test_env(self):
        api=Api()
        api.send(self.data)

