from django.db import models
from datetime import date, timedelta


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    def get_age(self):
        if self.birth_date:
            age = date.today().year - self.birth_date.year
            return f'Вам {age} лет'


class Employee(AbstractPerson):
    position = models.CharField(max_length=40, verbose_name='Должность')
    salary = models.IntegerField(verbose_name='Зарплата')
    work_experience = models.DateField(verbose_name='Дата принятия')

    # def save(self, *args, **kwargs):
    #     if self.position and self.salary and self.work_experience:
    #         return f'{self.position} сохранено в поле "Должность"' \
    #                f' {self.salary} сохранено в поле "Зарплата"' \
    #                f'{self.work_experience} сохранено в поле "Дата принятия"'
    #     super().save(*args, **kwargs)


class Passport(models.Model):
    inn = models.CharField(max_length=14, verbose_name='ИНН паспорта')
    id_card = models.CharField(max_length=8, verbose_name='Номер ID паспорта')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='passports')

    def __str__(self):
        return self.inn

    def get_gender(self):
        if self.inn[:1] == '1':
            return 'Female'
        elif self.inn[:1] == '2':
            return 'Male'


class WorkProject(models.Model):
    project_name = models.CharField(max_length=50, verbose_name='Название проекта')
    employee = models.ManyToManyField(Employee, related_name='workprojects', through='Membership')

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        if self.project_name:
            return f'{self.project_name} сохранено в поле "Название проекта"'
        super().save(*args, **kwargs)


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now=True)


class Client(AbstractPerson):
    address = models.CharField(max_length=50, verbose_name='Адрес')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')

    def save(self, *args, **kwargs):
        if self.address and self.phone_number:
            return f'{self.address} сохранено в поле "Адрес"' \
                   f'{self.phone_number} сохранено в поле "Номер телефона"'
        super().save(*args, **kwargs)


class VIPClient(Client):
    vip_status_start = models.DateField(verbose_name='Дата начала вип-статуса')
    donation_amount = models.IntegerField(verbose_name='Сумма пожертвования')

    def save(self, *args, **kwargs):
        if self.vip_status_start and self.donation_amount:
            return f'{self.vip_status_start} сохранено в поле "Дата начала вип-статуса"' \
                   f'{self.donation_amount} сохранено в поле "Сумма пожертвования"'
        super().save(*args, **kwargs)
