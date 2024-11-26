def send_email(recipient, *, sender='university.help@gmail.com'):
    if ('@' not in recipient or '@' not in sender or not recipient.endswith((".com", ".ru", ".net"))
            or not sender.endswith((".com", ".ru", ".net"))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('vasyok1337@gmail.com')
send_email('vasyok1337@gmail.ua')
send_email('vasyok1337gmail.com')
send_email('urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


