from flatmates_bill.flat import Bill, Flatmate
from flatmates_bill.reports import PdfReport, FileSharer

user_bill_amount = float(input('Hey User, Enter the Bill Amount: '))
user_period = input('What is the bill period? E.g: December 2020: ')
name1 = input('What is your name?: ')
days_in_house_1 = int(input(f"How many days did {name1} stay in the house during the bill period?: "))
name2 = input('What is your flatmate name?: ')
days_in_house_2 = int(input(f"How many days did {name2} stay in the house during the bill period?: "))

the_bill = Bill(amount=user_bill_amount, period=user_period)
person1 = Flatmate(name=name1, days_in_house=days_in_house_1)
person2 = Flatmate(name=name2, days_in_house=days_in_house_2)

print(f"{person1.name} pays: ", person1.pays(bill=the_bill, co_flatmate=person2))
print(f"{person2.name} pays: ", person2.pays(bill=the_bill, co_flatmate=person1))

pdf_report = PdfReport(f"{the_bill.period}.pdf")
filepath = pdf_report.generate(flatmate1=person1,
                               flatmate2=person2,
                               bill=the_bill)

file_sharer = FileSharer(filepath=filepath)
uploaded_link = file_sharer.share()
print(uploaded_link)
