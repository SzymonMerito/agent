def validate_email(email):
    return '@' in email

def test_mail():
    assert validate_email('test@wp.pl') == True
