from django.core.mail import send_mail
from datetime import datetime, timezone
from config import settings
from main.models import Message, Mailing, Attempt
from crontab import CronTab
from datetime import datetime, timedelta


def send_order_email(obj: Mailing):
    try:

        send_mail(
            obj.message.theme,
            obj.message.content,
            settings.EMAIL_HOST_USER,
            [*obj.clients.all()],
            fail_silently=True)

        # запись в таблицу успешного выполнения
        mail_attempt = Attempt.objects.create(
            settings=obj,
            message=obj.message.letter_subject,
            date=datetime.now(),
            status=True,
            server_answer='delivered'

        )
    except Exception as e:

        # запись в таблицу ошибки
        mail_attempt = Attempt.objects.create(
            settings=obj,
            message=obj.message.theme,
            date=datetime.now(),
            status=False,
            server_answer=str(e)

        )


def send_manager():
    current_date = datetime.now().date()  # получение текущей даты

    mailings_created = Mailing.objects.filter(
        status='CREATED')  # выборка из базы данных всех рассылок со статусом создана

    if mailings_created.exists():  # проверка пустой ли список или нет

        for mailing in mailings_created:

            if mailing.start_date <= current_date <= mailing.end_date:  # проверка пришло ли время рассылки

                mailing.status = 'LAUNCHED'
                mailing.save()

    mailings_launched = Mailing.objects.filter(
        status='LAUNCHED')  # выборка из базы данных всех рассылок со статусом запущено

    if mailings_launched.exists():  # проверка пустой ли список или нет

        for mailing in mailings_launched:
            # проверка находится ли текущая дата внутри промежутка времени между началом и концом рассылки
            if mailing.start_date <= current_date <= mailing.end_date:
                if mailing.last_run:  # если до текущего момента уже был запуск рассылки

                    differance = current_date - mailing.last_run  # разница между текущей датой и последним запуском

                    if mailing.frequency == 'daily':
                        # если разница между текущей датой и последней датой запуска равна 1 дню
                        if differance.days == 1:
                            send_order_email(mailing)  # запуск рассылки
                            mailing.last_run = current_date  # установление новой даты последнего запуска

                            mailing.save()

                    elif mailing.frequency == 'weekly':
                        # если разница между текущей датой и последней датой запуска равна 7 дням
                        if differance.days == 7:
                            send_order_email(mailing)  # запуск рассылки
                            mailing.last_run = current_date  # установление новой даты последнего запуска

                            mailing.save()

                    elif mailing.frequency == 'monthly':
                        # если разница между текущей датой и последней датой запуска равна 30 дням
                        if differance.days == 30:
                            send_order_email(mailing)  # запуск рассылки
                            mailing.last_run = current_date  # установление новой даты последнего запуска

                            mailing.save()




                # если расслыка ещё не запускалась
                else:
                    send_order_email(mailing)  # запуск рассылки
                    mailing.last_run = current_date  # установление новой даты последнего запуска
                    mailing.save()

            # если текущая дата больше чем конец рассылки
            elif current_date >= mailing.end_date:

                mailing.status = 'COMPLETED'

                mailing.save()