from clickpy.strategy import ClickStrategy, NaturalClickStrategy
from pytest import CaptureFixture
from pytest_mock import MockerFixture

_SLEEP_PATH = "clickpy.strategy.strategy.sleep"
_PYAUTOGUI_CLICK_PATH = "clickpy.strategy.strategy.pyautogui.click"
_RANDINT_PATH = "clickpy.strategy.strategy.randint"


def test_NaturalClickStrategy_is_ClickProtocol():
    assert isinstance(NaturalClickStrategy(), ClickStrategy)


def test_NaturalClickStrategy_works(mocker: MockerFixture):
    num = 1.5
    mock_sleep = mocker.patch(_SLEEP_PATH)
    mock_randit = mocker.patch(_RANDINT_PATH, return_values=num)
    mock_clicker = mocker.patch(_PYAUTOGUI_CLICK_PATH)

    natural = NaturalClickStrategy()
    natural.timers = [num]

    natural.click()

    assert natural.debug is False
    mock_randit.assert_called_with(NaturalClickStrategy.min_time, NaturalClickStrategy.max_time)
    mock_sleep.assert_called
    mock_clicker.assert_called()


def test_click_method_with_debug_flag(mocker: MockerFixture, capsys: CaptureFixture):
    num = 1.0
    mock_sleep = mocker.patch(_SLEEP_PATH)
    mock_randit = mocker.patch(_RANDINT_PATH, return_values=num)
    mock_clicker = mocker.patch(_PYAUTOGUI_CLICK_PATH)

    natural = NaturalClickStrategy(debug=True)
    natural.timers = []

    natural.click()

    out, err = capsys.readouterr()

    assert (
        out
        == f"Natural click timers: [{num}].\n\nThread sleeping for {num} seconds.\n! Clicked !\n"
    )
    assert err == ""
    assert natural.debug is True
    mock_randit.assert_called_once()
    mock_sleep.assert_called_once_with(num)
    mock_clicker.assert_called_once()
