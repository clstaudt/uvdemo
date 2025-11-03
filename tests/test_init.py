"""Tests for uvdemo module."""

from uvdemo import hello


def test_hello():
    """Test the hello function returns expected string."""
    result = hello()
    assert result == "Hello from uvdemo!"
    assert isinstance(result, str)

