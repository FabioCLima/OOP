# test_secretagent.py
import pytest
from src.secretagent import SecretAgent


@pytest.fixture
def capsys_fixture(capsys):
    return capsys


def test_initialize_attributes(capsys):
    # Given
    # Setup the input values or any preconditions specific to this test
    codename = "Bond"

    # When
    # Create a car instance
    doble_seven = SecretAgent("Bond")

    # Then
    # Access the attributes and verify their values
    result_codename = doble_seven.codename
    result_secrets = doble_seven._secrets

    # Assert the results against the expected values
    assert result_codename == codename, "Verify the codename attribute"
    assert result_secrets == [], "Verify the _secrets attribute"
