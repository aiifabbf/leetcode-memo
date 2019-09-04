/* 
筛选出每个部门工资最高的人。

首先要获得每个部门最高的工资

.. code:: sql

    select Employee.DepartmentId, max(Employee.Salary) as maxSalary
    from Employee
    group by Employee.DepartmentId

这样得到一张表

::

    DepartmentId, maxSalary

第一列是部门的Id，第二列是这个部门里最高的工资。

然后再从 ``Employee`` 表里筛选出工资数等于这个最高工资的人，因为可能有多个人工资并列部门第一。
*/ 

select Department.Name as Department, Employee.Name as Employee, Employee.Salary as Salary
from Department, Employee, ( -- 获得每个部门内最高的工资
    select Employee.DepartmentId as DepartmentId, max(Employee.Salary) as maxSalary
    from Employee
    group by Employee.DepartmentId
) as maxSalaries
where Employee.Salary = maxSalaries.maxSalary and Employee.DepartmentId = maxSalaries.DepartmentId and Department.Id = Employee.DepartmentId -- 筛选出每个部门里，工资是最高工资的人