org_names=["Justin","Eminem","Charlie","Michael","Nathan"]
org_amounts=[88.5,63,78.56,451,69.3]

unfor_message="""Hi Thanks {name} For The Purchase Of {total} on {date}."""

def makemessages(names, amounts):
    message=[]
    if len(names) == len(amounts):
        i = 0
        for name in names:
            #i = i + 1
            new_msg = unfor_message.format(
                name=name,
                    date='some date',
                    total=amounts[i]
            )
            print(new_msg)
            i = i + 1

makemessages(org_names, org_amounts)

