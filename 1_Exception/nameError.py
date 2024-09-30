def geek_message():
    try:
        geek = "Geeks For Geeks"
        return geek #change geek = geeks for nameError
    except NameError:
        return "NameError occurred same variable isn't defined"

print(geek_message())


# OUTPUT
# NameError occurred, variable isn't defined
