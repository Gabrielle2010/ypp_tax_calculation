#!/usr/bin/env python
# @Time    : 7/28/2017 10:06 AM
# @Author  : Wu Guo


# from Tkinter import *
# import rootMessageBox as message_box
from tkinter import *
import tkinter.messagebox as message_box
from lib.lib import *
from lib.base_class import *


def submit_button():
    salary_str = salary_entry.get('0.0', END)
    if len(salary_str) == 1:
        message_box.showinfo("Error", "Please input Salary")
        return
    month_salary = float(salary_str.replace(',', '').replace(' ', ''))

    insurance_base_str = insurance_base_entry.get('0.0', END)
    if len(insurance_base_str) == 1:
        message_box.showinfo("Error", "Please input Insurance Base")
        return
    insurance_base = float(insurance_base_str.replace(',', '').replace(' ', ''))

    house_fund_base_str = house_fund_base_entry.get('0.0', END)
    if len(house_fund_base_str) == 1:
        message_box.showinfo("Error", "Please input House Fund Base")
        return
    house_fund_base = float(house_fund_base_str.replace(',', '').replace(' ', ''))

    stock_str = stock_entry.get('0.0', END)
    if len(stock_str) == 1:
        message_box.showinfo("Error", "Please input House Fund Base")
        return
    stock = float(stock_str.replace(',', '').replace(' ', ''))

    employ_costs = 0
    for i in house_obs:
        employ_costs += i.get_employ(house_fund_base)
        i.fill_entry(house_fund_base)

    for i in insurance_obs:
        employ_costs += i.get_employ(insurance_base)
        i.fill_entry(insurance_base)

    salary_tax_ob = SalaryTax(tax_standard, tax_free)
    employ_tax = salary_tax_ob.get_tax(month_salary - employ_costs)

    stock_tax_ob = StockTax(stock_tax_employ_ratio)
    replace_text(salary_tax_entry, employ_tax)
    replace_text(stock_tax_entry, stock_tax_ob.get_tax(stock))
    replace_text(net_salary_entry, round(month_salary + stock - employ_tax - employ_costs, 2))


if __name__ == "__main__":
    endowment_name = 'Endowment Insurance'
    medical_name = 'Medical Insurance'
    unemployment_name = 'Unemployment Insurance'
    injure_name = 'Work-related Injury Insurance'
    childbirth_name = 'Childbirth Insurance'
    house_name = 'Housing Funds'

    root = Tk()
    root.wm_title('Normal Calculator')

    salary_entry = create_item(root, 'Salary', bg='yellow')
    insurance_base_entry = create_item(root, 'Insurance Base', bg='yellow')
    house_fund_base_entry = create_item(root, 'House Fund Base', bg='yellow')
    stock_entry = create_item(root, 'Stock', bg='yellow')
    net_salary_entry = create_item(root, "Net Salary")
    salary_tax_entry = create_item(root, 'Salary Tax')
    stock_tax_entry = create_item(root, 'Stock Tax')

    house_obs = []
    house_fund = HouseFund(house_fund_employ_ratio, house_fund_company_ratio, house_fund_base_max,
                           house_fund_base_min, root, house_name)

    house_obs.append(house_fund)

    # Insurance objects
    insurance_obs = []
    insurance = Insurance(endowment_insurance_employ_ratio, endowment_insurance_company_ratio,
                          endowment_insurance_base_max, endowment_insurance_base_min, root,
                          endowment_name)

    insurance_obs.append(insurance)

    insurance = Insurance(medical_insurance_employ_ratio, medical_insurance_company_ratio,
                          medical_insurance_base_max, medical_insurance_base_min, root,
                          medical_name, medical_insurance_employ_addition)

    insurance_obs.append(insurance)

    insurance = Insurance(unemployment_insurance_employ_ratio, unemployment_insurance_company_ratio,
                          unemployment_insurance_base_max, unemployment_insurance_base_min, root,
                          unemployment_name)

    insurance_obs.append(insurance)

    insurance = Insurance(injure_insurance_employ_ratio, injure_insurance_company_ratio,
                          injure_insurance_base_max, injure_insurance_base_min, root,
                          injure_name, hide=True)

    insurance_obs.append(insurance)

    insurance = Insurance(childbirth_insurance_employ_ratio, childbirth_insurance_company_ratio,
                          childbirth_insurance_base_max, childbirth_insurance_base_min, root,
                          childbirth_name, hide=True)

    insurance_obs.append(insurance)

    submit = Button(root, text='Submit', command=lambda: submit_button())
    submit.pack()

    # for text
    replace_text(salary_entry, '29,858.00')
    replace_text(stock_entry, '0')
    # replace_text(insurance_base_entry, '7706')
    # replace_text(house_fund_base_entry, '4000')
    replace_text(insurance_base_entry, '29,858.00')
    replace_text(house_fund_base_entry, '29,858.00')
    root.mainloop()
