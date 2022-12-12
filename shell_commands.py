from worker.models import *

pasport1 = Passport(employee=Employee.objects.create(name='Myrza', birth_date='1997-03-15', position='Python BackEnd',
                    salary=1000, work_experience='2022-12-31'),
                    inn='22503199701012', id_card='AN123456')
pasport2 = Passport(employee=Employee.objects.create(name='Adil', birth_date='1997-05-29', position='C# BackEnd',
                    salary=1500, work_experience='2020-11-10'),
                    inn='15456765401012', id_card='AN345678')
pasport3 = Passport(employee=Employee.objects.create(name='Kurban', birth_date='1996-03-31', position='JS FrontEnd',
                    salary=2000, work_experience='2018-02-11'),
                    inn='22456455656012', id_card='AN765432')
pasport4 = Passport(employee=Employee.objects.create(name='Avtandil', birth_date='1995-12-31', position='UX/UI design',
                    salary=800, work_experience='2021-02-15'),
                    inn='12567655501012', id_card='AN754426')

pasport1.save()
pasport2.save()
pasport3.save()
pasport4.save()

Employee.objects.filter(id=4).delete()

wp1 = WorkProject.objects.create(project_name='Google')

e5 = Employee.objects.create()

exp_date = Employee.objects.create(work_experience='2022-10-10')
my_list = [exp_date]
wp1.employee.set(my_list)

pasport5 = Passport(employee=Employee.objects.create(name='Amantur', birth_date='1993-06-25', position='QA tester',
                    salary=900, work_experience='2021-02-15'),
                    inn='125676553442', id_card='AN757726')


c1 = Client.objects.create(name='Leo Messi', birth_date='1987-06-24', address='Paris',
                           phone_number='+433222010101')
c2 = Client.objects.create(name='Kilyan Mbappe', birth_date='1998-12-04', address='Lion',
                           phone_number='+433288899101')
c3 = Client.objects.create(name='Neymar', birth_date='1992-02-05', address='Brazil',
                           phone_number='+454563437108')

vip = VIPClient.objects.create(name='Jose Mourinho', birth_date='1967-01-15', address='Roma',
                               phone_number='+767687645608', vip_status_start='2004-01-30',
                               donation_amount=10000000)

Client.objects.filter(id=2).delete()

print(Employee.objects.all())
print(Employee.objects.only('passport'))

print(WorkProject.objects.all())
# print(WorkProject.objects.filter())

print(Client.objects.all())
print(VIPClient.objects.all())
