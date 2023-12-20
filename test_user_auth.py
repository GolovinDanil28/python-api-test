import requests
class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        
        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response.headers, "There is no CSRF token header in the response"
        assert "user_id" in response.json(), "There is no user id in the response"
        
        auth_id = response.cookies.get("auth_sid")
        token = response.headers.get("x-csrf-token")
        user_id_from_method = response.json()["user_id"]

        responseGet = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid":auth_id}
        )

        assert "user_id" in responseGet.json(), "There is no user id in the second response"
        user_id_from_check_method= responseGet.json()["user_id"]
        assert user_id_from_method == user_id_from_check_method, "There user id is no eaqul user_id_from_check method"
