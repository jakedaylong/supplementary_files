#!/usr/bin/env python

"""demo classes"""


class Employee:
    """ An employee is a person who works at EXPD """
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def change_salary(self, amt):
        """ change salary takes an increment (not a new salary)"""
        self.salary = self.salary + amt

    def describe(self):
        print(f"Employee {self.name} makes {self.salary}")

    def hire(self, job_title):
        employee_job = Job(job_title, self.name)
        employee_job.describe()


class Job:
    """ an employee has a job"""
    def __init__(self, job_title, name):
        self.job_title = job_title
        self.name = name

    def describe(self):
        print(f"Employee {self.name} has job {self.job}")


if __name__ == "__main__":

    employees = [
        ("andy", 34000),
        ("chris", 12000),
        ("fred", 75000),
        ("xxxx", 35000),
    ]

    for employee in employees:
        happier_employee = Employee(employee[0], employee[1])
        happier_employee.describe()
        happier_employee.change_salary(200)
        happier_employee.describe()
