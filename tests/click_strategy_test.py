# """Unit tests for Click Strategy Module."""

# import inspect
# from typing import Protocol
# from unittest.mock import MagicMock

# import clickpy.click_strategy
# import pytest
# from clickpy.exception import ClickStrategyNotFound
# from clickpy.strategy import BasicClickStrategy, ClickStrategy
# from pytest import CaptureFixture


# class SomeObj:  # noqa
#     def __init__(self):  # noqa
#         self.x = 0


# def test_all_strats_in_STRATEGIES_dict():
#     """Make sure STRATEGIES dict is always up-to-date."""
#     members = inspect.getmembers(clickpy.click_strategy, inspect.isclass)
#     remove_types = [
#         (ClickProtocol.__name__, ClickProtocol),
#         (Protocol.__name__, Protocol),
#         (ClickStrategyNotFound.__name__, ClickStrategyNotFound),
#     ]

#     members = list(filter(lambda x: x not in remove_types, members))

#     # All classes (besides base protocol) should be in this dict
#     assert len(members) == len(STRATEGIES)

#     for member in members:
#         cli_name = member[1].cli_repr()
#         assert cli_name in STRATEGIES
#         assert STRATEGIES[cli_name] == member[1]


# def test_auto_click_works():  # noqa
#     # Arrange
#     basic = BasicClickStrategy()
#     basic.__click__ = MagicMock(return_value=None, name="__click__")

#     # Act
#     auto_click(basic)

#     # Assert
#     basic.__click__.assert_called_once()


# def test_auto_click_structural_subtyping_works() -> None:  # noqa
#     # Arrange
#     some_obj = SomeObj()
#     mock_click = MagicMock(return_value=None, name="__click__")
#     setattr(some_obj, "__click__", mock_click)
#     setattr(some_obj, "debug", False)
#     setattr(some_obj, "cli_repr", MagicMock(return_value="str", name="to_cli_string"))
#     # Act
#     auto_click(some_obj)  # type: ignore

#     # Assert
#     some_obj.__click__.assert_called_once()  # type: ignore
#     mock_click.assert_called_once()
#     some_obj.cli_repr.assert_not_called()  # type: ignore


# def test_auto_click_throws_type_error_if_arg_not_SupportsClick_subtype():  # noqa

#     with pytest.raises(TypeError) as excinfo:
#         auto_click(SomeObj())  # type: ignore

#     assert excinfo.type is TypeError
#     assert (
#         excinfo.value.args[0] == f"Argument passed in does not implement"
#         f" {ClickProtocol.__name__}"
#     )


# def test_click_strategy_factory_returns_BasicClickStrategy():
#     basic = click_strategy_factory()

#     assert isinstance(basic, BasicClickStrategy)
#     assert isinstance(basic, ClickProtocol)
#     assert basic.debug == False
#     assert basic.sleep_time is None


# def test_click_strategy_factory_with_debug_flag_and_defaults(capsys: CaptureFixture):
#     basic = click_strategy_factory(debug=True)
#     out, err = capsys.readouterr()

#     assert basic.debug
#     assert out == "click_type passed into factory func: None\n"


# funky_types = ["    basic", "BASIC", " Basic ", "  bAsIc     ", "Natural", "   natural   "]


# @pytest.mark.parametrize("types", funky_types)
# def test_click_strategy_factory_sanitizes_clik_type_param(types: str, capsys: CaptureFixture):
#     clicker = click_strategy_factory(types, debug=True)

#     out, _ = capsys.readouterr()

#     assert isinstance(clicker, ClickProtocol)
#     assert (
#         out
#         == f"""click_type passed into factory func: {types!r}
# sanitized click_type={types.strip().lower()!r}
# """
#     )


# bad_types = ["", "    ", "notatype", "SomThINGeLsE"]


# @pytest.mark.parametrize("types", bad_types)
# def test_empty_str_or_no_existing_type_string_throws_error(types: str):
#     with pytest.raises(ClickStrategyNotFound):
#         click_strategy_factory(click_type=types)
