def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

thea = replace_domain("tdcforonda@mymail.mapua.edu.ph", "mymail.mapua.edu.ph", "mapua.edu.ph")
print(thea)
