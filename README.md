# pivot-json
*Emulates pivot tables by adding calculated fields in a JSON file*. This can be done in Excel by importing the JSON data and adding columns and expressions. However, this python script allows you to work just with the JSON file.

## Use case
Say you have a JSON file with data on companies' performance: num of employees, num of completed projects and annual turnover.

```json
{
    "data":[
        {
            "company": "Company 1", 
            "employees": 580, 
            "projects": 208, 
            "turnover": 897, 
        }, 
        {
            "company": "Company 2", 
            "employees": 691, 
            "projects": 107, 
            "turnover": 1159, 
        }, 
        {
            "company": "Company 3", 
            "employees": 448, 
            "projects": 40, 
            "turnover": 591, 
        }
    ]
}
```

We make use of a JSON visualizer ([JSON ninja](http://www.jsondata.ninja/ninja.html)) to give us a table.

[![image.png](https://s10.postimg.org/ai2n9x6vd/image.png)](https://postimg.org/image/9sjuxk6bp/)

The most exciting now is sorting by column name. But let's check how the companies perform on a per employee basis: we'll look at *turnover per employee* and *number of projects per employee*. This script lets us add what we want to be computed as expressions.

```json
{
    "expressions":[
        "turnover_per_employee = turnover / employees",
        "projects_per_employee = projects / employees"
    ],
    "data":[
        ...
    ]
}
```

Each expression results in a new column being added. Its value is the computed value stated in the expression.

```json
{
    "expressions": [
        "turnover_per_employee = turnover / employees", 
        "projects_per_employee = projects / employees"
    ], 
    "data": [
        {
            "turnover_per_employee": 1.547, 
            "company": "Company 1", 
            "projects_per_employee": 0.359, 
            "employees": 580, 
            "projects": 208, 
            "turnover": 897
        }, 
        {
            "turnover_per_employee": 1.677, 
            "company": "Company 2", 
            "projects_per_employee": 0.155, 
            "employees": 691, 
            "projects": 107, 
            "turnover": 1159
        }, 
        {
            "turnover_per_employee": 1.319, 
            "company": "Company 3", 
            "projects_per_employee": 0.089, 
            "employees": 448, 
            "projects": 40, 
            "turnover": 591
        }
    ]
}
```

Visualizing this in [JSON ninja](http://www.jsondata.ninja/ninja.html) gives a better pivot table to play around with.

[![image.png](https://s10.postimg.org/o1o2t0up5/image.png)](https://postimg.org/image/59c7pfyat/)

## Further development
- allow for more complex expressions. Now just 1 operation: either of + - / *
- add graphs
