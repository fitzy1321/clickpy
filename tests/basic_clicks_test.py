# noqa

import typer
from clickpy import BasicClickStrategy
from clickpy.strategy import ClickStrategy
from pytest import CaptureFixture
from pytest_mock import MockerFixture

_SLEEP_PATH = "clickpy.strategy.strategy.sleep"
_PYAUTOGUI_CLICK_PATH = "clickpy.strategy.strategy.pyautogui.click"
_RANDINT_PATH = "clickpy.strategy.strategy.randint"


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
    assert basic_click._stdout == typer.echo
    assert basic_click._timer == 0.5
    assert basic_click.fast is True
    mock_sleep.assert_called_once_with(0.5)
    mock_gui_click.assert_called_once()


def test_BasicClickStrategy_uses_randint_when_sleep_time_is_none(mocker: MockerFixture):  # noqa
    # Arrange
    sleep_time = 5
    mock_randint = mocker.patch(_RANDINT_PATH, return_value=sleep_time)
    mock_sleep = mocker.patch(_SLEEP_PATH)
    mock_gui_click = mocker.patch(_PYAUTOGUI_CLICK_PATH)

    # Act
    basic_click = BasicClickStrategy()
    basic_click.click()

    # Assert
    assert basic_click.fast is False
    assert basic_click._timer == 5
    mock_randint.assert_called_once_with(BasicClickStrategy.min_time, BasicClickStrategy.max_time)
    mock_sleep.assert_called_once_with(sleep_time)
    mock_gui_click.assert_called_once()


def test_BasicClickStrategy_prints_stdout_when_print_debug_is_True(
    mocker: MockerFixture, capsys: CaptureFixture
):  # noqa
    # Arrange
    mock_sleep = mocker.patch(_SLEEP_PATH)
    mock_gui_click = mocker.patch(_PYAUTOGUI_CLICK_PATH)

    # Act
    basic_click = BasicClickStrategy(fast=True, debug=True)
    basic_click.click()

    out, err = capsys.readouterr()

    # Assert
    assert basic_click.fast is True
    assert basic_click._timer == 0.5
    assert basic_click.debug is True
    assert out == "Thread sleeping for 0.5 seconds.\n! Clicked !\n"
    assert err == ""
    mock_sleep.assert_called_once_with(0.5)
    mock_gui_click.assert_called_once()


def test_BasicClickStrategy_prints_random_time_when_debug_true(
    mocker: MockerFixture, capsys: CaptureFixture
):  # noqa
    # Arrange
    sleep_time = 1.0
    mock_randint = mocker.patch(_RANDINT_PATH, return_value=sleep_time)
    mock_sleep = mocker.patch(_SLEEP_PATH)
    mock_gui_click = mocker.patch(_PYAUTOGUI_CLICK_PATH)

    # Act
    basic_click = BasicClickStrategy(debug=True)
    basic_click.click()

    out, err = capsys.readouterr()

    # Assert
    assert out == f"Thread sleeping for {sleep_time} seconds.\n! Clicked !\n"
    assert err == ""
    assert basic_click.debug is True
    assert basic_click._timer == 1
    assert basic_click.fast is False
    mock_randint.assert_called_once_with(basic_click.min_time, basic_click.max_time)
    mock_sleep.assert_called_once_with(sleep_time)
    mock_gui_click.assert_called_once()
