
import poplib
import email
import time

class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop=poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)
            #количество писем
            num = pop.stat()[0]
            if num > 0:
                for n in range(num):
                    #возвращает кортеж, текст письма - во втором элементе
                    msglines = pop.retr(n+1)[1]
                    #склеиваем строки
                    msgtext = "\n".join(map(lambda x: x.decode('utf-8'), msglines))
                    #анализ текста
                    msg = email.message_from_string(msgtext)
                    if msg.get('Subject') == subject:
                        #помечаем письмо на удаление
                        pop.dele(n+1)
                        #закрыть соединение с сохранением
                        pop.quit()
                        return msg.get_payload()
                    pop.quit()
                    time.sleep(5)
                return None