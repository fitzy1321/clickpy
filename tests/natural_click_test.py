from clickpy.strategy import ClickStrategy, NaturalClickStrategy
from pytest import CaptureFixture
from pytest_mock import MockerFixture

from . import click_patch_str
from . import natural_name as name
from . import randint_patch_str, sleep_patch_str


def test_NaturalClickStrategy_is_ClickProtocol():
    """Make sure NaturalClickStrategy implements ClickProtocol."""
    assert isinstance(NaturalClickStrategy(), ClickStrategy)  # type: ignore


def test_NaturalClickStrategy_works(mocker: MockerFixture):
    """Make sure __click__() method is working as planned."""
    num = 1.0
    mock_sleep = mocker.patch(sleep_patch_str)
    mock_randit = mocker.patch(randint_patch_str, return_values=num)
    mock_clicker = mocker.patch(click_patch_str)

    natural = NaturalClickStrategy(name=name)
    natural.wait_times = [num]

    natural.click()

    mock_sleep.assert_called_once_with(num)
    mock_clicker.assert_called_once()


def test_click_method_with_debug_flag(mocker: MockerFixture, capsys: CaptureFixture):
    """Make sure debug statements are correct."""
    num = 1.0
    mock_sleep = mocker.patch(sleep_patch_str)
    mock_randit = mocker.patch(randint_patch_str, return_values=num)
    mock_clicker = mocker.patch(click_patch_str)

    natural = NaturalClickStrategy(name=name, debug=True)
    natural.wait_times = [num]

    natural.click()

    out, _ = capsys.readouterr()

    assert out == f"Waiting for {num} sec ...\n... Clicked\n"
    mock_sleep.assert_called_once_with(num)
    mock_clicker.assert_called_once()
