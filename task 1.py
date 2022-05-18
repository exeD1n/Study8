import re


def email_parse(email_address):
    parsed = re.findall(
        r'(^\w+)@((\w+).(\w{2,}))$', email_address)
    if not parsed:
        raise ValueError(f"Не соответствует почте: {email_address}")
    return dict(zip(["username", "domain"], parsed[0]))


if __name__ == "__main__":
    print(email_parse('daniillutaev1@gmail.com'))
