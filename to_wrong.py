def to_wrong(answer):
    """
    Customize the wrong answer based on the correct one.
    This function is triggered for fill-in-the-blank questions.
    """
    if isinstance(answer, str):
        return '.'
    else:
        return [to_wrong(item) for item in answer]
