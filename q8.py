def sanitize_email(raw_input: str) -> str:
    s = raw_input.strip().lower()

    if s.count("@") == 1 and s.split("@")[0] and s.split("@")[1]:
        return s

    return "Invalid Email"

Teamname-{CodeTrio}
