from projects.project_1.animal import make_message


def test_make_message():
    assert make_message("wolf") == "Your favorite animal is the wolf."

