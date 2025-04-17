"""Test Snap Package Template."""

import curso_fastapi


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(curso_fastapi.__name__, str)
