import re


def email_parse(email):
    out_dict = {}
    email_patern = re.compile(r'\w*@\w*\.')
    if email_patern.match(email):
        out_dict['username'] = email.split('@')[0]
        out_dict['domain'] = email.split('@')[1]
    else:
        assert email_patern.match(email), f'ValueError({email})'
    return print(out_dict)


email_parse('daniilluytaev1@gmail.com')
