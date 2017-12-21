#!/usr/bin/python
import json
import sys

def printUsage():
	print
	print '   Usage: ' +sys.argv[0]+ ' <filename>.json'
	print
	print 'JSON file must be in format'
	print
	print '   ['
	print '      {'
	print '         "expressions":['
	print '            "new_column_name     = key <operator> key",'
	print '            "another_column_name = key <operator> key",'
	print '            ...'
	print '         ],'
	print '      },{'
	print '         "data":['
	print '            "key": value,'
	print '            "key": value,'
	print '            ...'
	print '         ]'
	print '      }]'
	print '   ]'
	print
	print 'where <operator> is either of: + - / *'
	print
	print 'Example json file:'
	print
	print '   {'
	print '       "expressions": ['
	print '           "turnover_per_employee = turnover / employees", '
	print '           "projects_per_employee = projects / employees"'
	print '       ], '
	print '       "data": ['
	print '           {'
	print '               "company": "Company 1", '
	print '               "employees": 580, '
	print '               "projects": 208, '
	print '               "turnover": 897'
	print '           }, '
	print '           {'
	print '               "company": "Company 2", '
	print '               "employees": 448, '
	print '               "projects": 40, '
	print '               "turnover": 591'
	print '           }'
	print '       ]'
	print '   }'
def checkArgs():
	if len(sys.argv) == 1:
		printUsage()
		sys.exit(1)
def loadJson(filename):
	with open(filename, 'r') as f:
		data = json.load(f)
	return data
def validateExpressions(data):
	AllowedOperations = ['+', '-', '/', '*']
	valid_expressions = []
	for expr in data['expressions']:
		column_name, rhs = expr.split('=')
		for allowed_op in AllowedOperations:
			if allowed_op in rhs:
				a, b = rhs.split(allowed_op)
				valid_expressions.append({'column_name': column_name.strip(), \
										  'a':           a.strip(), \
										  'op':          allowed_op, \
										  'b':           b.strip()})
				break
	return valid_expressions
def applyExpressions(data, expressions):
	i = 0
	for json_obj in data['data']:
		for expr in expressions:
			json_obj[expr['column_name']] = round(eval('1.0 * ' + str(json_obj[expr['a']]) + expr['op'] + str(json_obj[expr['b']])), 3)
		data['data'][i] = json_obj
		i += 1
	return data
def saveJson(filename, data):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)
def main():
	filename          = sys.argv[1]
	json_data         = loadJson(filename)
	valid_expressions = validateExpressions(json_data)
	json_data         = applyExpressions(json_data, valid_expressions)
	saveJson(filename, json_data)

if __name__ == '__main__':
	checkArgs()
	main()
