import pytest
from clickpy import ClickStrategy, generate_click_strategy
from clickpy.exception import ClickStrategyNotFound
from clickpy.strategy import DEFAULT_STRATEGY


def test_default_clicker_is_basic() -> None:
    from clickpy.strategy import DEFAULT_STRATEGY

    assert DEFAULT_STRATEGY == "basic"


def test_factory_func_raises_TypeError_when_arg_is_None() -> None:
    with pytest.raises(TypeError):
        generate_click_strategy(None)


def test_factory_func_raises_ClickStrategyNotFound_for_unknown_strat_string() -> None:
    with pytest.raises(ClickStrategyNotFound):
        generate_click_strategy("derp")


def test_factory_func_returns_ClickStrategy_subclass() -> None:
    basic: ClickStrategy = generate_click_strategy(DEFAULT_STRATEGY)
    assert isinstance(basic, ClickStrategy)


def test_factory_func_passes_kwargs_through_to_objects() -> None:
    result: ClickStrategy = generate_click_strategy(DEFAULT_STRATEGY, debug=True, fast=True)

    assert result.debug is True
    assert result.fast is True
