from soap_api import check_text


def test_step1(correct_word, incorrect_word):
    assert correct_word in check_text(incorrect_word), 'Test 1 FAILED'
