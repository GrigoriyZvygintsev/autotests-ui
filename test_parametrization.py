import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (4, 5, 9)])
def test_numbers(a, b, expected):
    assert a + b != expected

@pytest.fixture(params=["chromium", "webkit", "firefox"])
# Фикстура будет возвращать три разных браузера
# Соотвественно все автотесты использующие данную фикстуру будут запускаться три раза
def browser(request: SubRequest) -> str:
    return request.param  # Внутри атрибута param находится одно из значений "chromium", "webkit", "firefox"


# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_open_browser(browser: str):
    # Используем фикстуру в автотесте, она вернет нам браузер в виде строки
    print(f"Running test on browser: {browser}")

@pytest.mark.parametrize("tel", ['88005553535', '3423455435', '434234324324'],
                         ids = ['opisanie 1', 'opisanie 2', 'opisanie 3'])
def test_tel(tel):
    assert type(tel) == str