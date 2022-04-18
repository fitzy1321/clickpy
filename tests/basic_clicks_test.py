# noqa

from clickpy import BasicClickStrategy
from clickpy.strategy import ClickStrategy
from pytest import CaptureFixture
from pytest_mock import MockerFixture

_SLEEP_PATH = "clickpy.strategy._strategy.sleep"
_PYAUTOGUI_CLICK_PATH = "clickpy.strategy._strategy.pyautogui.click"


def test_BasicClickStrategy_is_SupportsClick():  # noqa
    assert isinstance(BasicClickStrategy(), ClickStrategy)


def test_BasicClickStrategy_sets_fast_sleep_time(
    mocker: MockerFixture, capsys: CaptureFixture
):  # noqa
    # Arrange
    mock_sleep = mocker.patch(_SLEEP_PATH)
    mock_gui_click = mocker.patch(_PYAUTOGUI_CLICK_PATH)

    # Act
    basic_click = BasicClickStrategy(fast=True)
    basic_click.click()

    # Assert
    assert basic_click._timer == 0.5
    assert basic_click.fast is True
    mock_sleep.assert_called_once_with(0.5)
    mock_gui_click.assert_called_once()


# def test_BasicClickStrategy_uses_randint_when_sleep_time_is_none(mocker: MockerFixture):  # noqa
#     # Arrange
#     sleep_time = 5
#     mock_randint = mocker.patch(randint_patch_str, return_value=sleep_time)
#     mock_sleep = mocker.patch(sleep_patch_str)
#     mock_gui_click = mocker.patch(click_patch_str)

#     # Act
#     basic_click = BasicClickStrategy(name=name)
#     basic_click.click()

#     # Assert
#     assert basic_click.fast is None
#     mock_randint.assert_called_once_with(basic_click.min_bound, basic_click.max_bound)
#     mock_sleep.assert_called_once_with(sleep_time)
#     mock_gui_click.assert_called_once()


# def test_BasicClickStrategy_prints_stdout_when_print_debug_is_True(
#     mocker: MockerFixture, capsys: CaptureFixture
# ):  # noqa
#     # Arrange
#     mock_sleep = mocker.patch(sleep_patch_str)
#     mock_gui_click = mocker.patch(click_patch_str)

#     # Act
#     basic_click = BasicClickStrategy(fast=True, debug=True, name=name)
#     basic_click.click()

#     out, err = capsys.readouterr()

#     # Assert
#     assert basic_click.fast is True
#     assert basic_click.debug is True
#     assert out == f"Thread sleeping now...\n... Clicked\n"
#     assert err == ""
#     mock_sleep.assert_called_once_with(0.5)
#     mock_gui_click.assert_called_once()


# def test_BasicClickStrategy_prints_random_time_when_sleep_time_is_None(
#     mocker: MockerFixture, capsys: CaptureFixture
# ):  # noqa
#     # Arrange
#     sleep_time = 1.0
#     mock_randint = mocker.patch(randint_patch_str, return_value=sleep_time)
#     mock_sleep = mocker.patch(sleep_patch_str)
#     mock_gui_click = mocker.patch(click_patch_str)

#     # Act
#     basic_click = BasicClickStrategy(debug=True)
#     basic_click.click()

#     out, err = capsys.readouterr()

#     # Assert
#     assert basic_click.fast is None
#     assert (
#         out
#         == f"Random thread sleep for {sleep_time} seconds.\nThread sleeping now...\n... Clicked\n"
#     )
#     assert err == ""
#     assert basic_click.debug is True
#     mock_randint.assert_called_once_with(basic_click.min_bound, basic_click.max_bound)
#     mock_sleep.assert_called_once_with(sleep_time)
#     mock_gui_click.assert_called_once()
