def to_wrong(answer):
    """
    Customize your wrong answer according to the right answer.
    Only trigger in fill-the-blank questions.
    """
    if isinstance(answer, str):
        return '.'
    else:
        wrong_answer = []
        for item in answer:
            wrong_answer.append(to_wrong(item))
        return wrong_answer