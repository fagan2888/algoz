from algoz.welcome import welcome_message

def test_welcome():
    html = welcome_message(private_key="asgd",public_key='asdf',email_alias='7@3za.org')
    assert "<html>" in html
