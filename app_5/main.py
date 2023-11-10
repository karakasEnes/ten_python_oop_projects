from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               result=False,
                               billform=bill_form)

    def post(self):
        billform = BillForm(request.form)
        amount = float(billform.amount.data)
        period = billform.period.data

        name1 = billform.name1.data
        days_in_house_1 = float(billform.days_in_house1.data)

        name2 = billform.name2.data
        days_in_house_2 = float(billform.days_in_house2.data)

        the_bill = flat.Bill(amount=amount,
                             period=period)

        person1 = flat.Flatmate(name=name1, days_in_house=days_in_house_1)
        person2 = flat.Flatmate(name=name2, days_in_house=days_in_house_2)

        return render_template('bill_form_page.html',
                               result=True,
                               billform=billform,
                               name1=person1.name,
                               amount1=person1.pays(the_bill, person2),
                               name2=person2.name,
                               amount2=person2.pays(the_bill, person1))


class BillForm(Form):
    amount = StringField('Bill Amount: ', default='1000')
    period = StringField('Bill Period: ', default='December 2020')

    name1 = StringField('Flatmate1 Name: ', default='Jax')
    days_in_house1 = StringField(
        'Days in the house for Flatmate1: ', default=20)

    name2 = StringField('Flatmate2 Name: ', default='Marry')
    days_in_house2 = StringField(
        'Days in the house for Flatmate2: ', default='22')

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule(
    '/bill_form', view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)
