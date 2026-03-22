import pytest
import faker


class TestLogin:

    def test_login(self, user):
        print(user.login, user.password)


class TestExample:

    @pytest.mark.usefixtures("user_data")
    def test_example(self):
        print(self.login, self.password)

class TestDriver:

    @pytest.mark.usefixtures("DR")
    def test_driver(self):
        self.driver.get("https://google.com")

    @pytest.mark.regress
    class TestAutoUse:
        def test_autouser(self):
            self.driver.get("https://google.com")