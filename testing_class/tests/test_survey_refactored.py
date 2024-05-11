# test_survey_refactored.py
'''
Writing the test for the methods of the AnonymousSurvey class
using fixture to setup the creating a resource for each test.
'''
import pytest
from src.survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """
    Fixture to create an instance of AnonymousSurvey with a predefine
    question.
    """
    question = "What language did you first learn to speak."
    return AnonymousSurvey(question)


def test_initialize_attributes(language_survey):
    """
    Testing the initializing the attributes of AnonymousSurvey
    """
    # Given
    # Setup the an instance of the class with any input values or any
    # preconditions specific to this test
    # The fixture 'language_survey' is already providing us with an
    # initialized instance

    # When
    # Since this test is only concerned with verifing the initialization
    # of attributes, there's no specific action needed.

    # Then
    assert language_survey.question == "What language did you first learn to speak."
    assert language_survey.responses == []


def test_store_single_response(language_survey):
    """
    Test that a single response is stored properly.
    """
    # Given
    # Setup the an instance of the class with any input values or any
    # preconditions specific to this test
    # fixture

    # When
    language_survey.store_response('English')

    # Then
    assert "English" in language_survey.responses
