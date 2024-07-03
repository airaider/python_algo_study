from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
numbers	target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2
"""

test_cases = convert_table_to_test_cases(table_text)