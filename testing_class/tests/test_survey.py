# test_survey.py
'''
Much of the work of testing classes involves testing the behavior of
the methods in the class.To test the behavior of a class, we need to
make an instance of the class.
'''
from src.survey import AnonymousSurvey


def test_store_single_response():
    """
    Test that a single response is stored properly.
    """
    # Given
    # Setup the an instance of the class with any input values or any
    # preconditions specific to this test
    question = "What language did you first learn to speak?"
    survey = AnonymousSurvey(question)  # an instance of the class

    # When
    survey.store_response('English')

    # Then
    assert "English" in survey.responses


def test_store_three_responses():
    """
    Test that three individual responses are stored properly.
    """
    # Given
    # Setup an instance of the class with any input values or any
    # preconditions specific to this test
    question = "What language did you first learn to speak?"
    survey = AnonymousSurvey(question)  # an instance of the class
    responses = ["English", "Spanish", "Mandarin"]

    # When
    for response in responses:
        survey.store_response(response)

    # Then
    for response in responses:
        assert response in survey.responses
