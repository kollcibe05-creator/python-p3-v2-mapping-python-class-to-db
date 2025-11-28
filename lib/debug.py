#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)

# payroll.save()
# print(payroll)

hr = Department.create("Human Resources", "Building c, East Wing")
print(hr)


quality_assurance = Department.create("Quality Asurance", 'Gaza Plaza')   

quality_assurance.name = "Quality Assurance"
quality_assurance.update()
print(quality_assurance)



staff_recruiters = Department.create("Staff recruitment", "Paza Plaza, 2nd Floor")
print(staff_recruiters)

staff_recruiters.delete()
print(staff_recruiters)

# hr.save()
# print(hr)
ipdb.set_trace()
