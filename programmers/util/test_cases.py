from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5
"""

test_cases = convert_table_to_test_cases(table_text)