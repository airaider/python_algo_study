from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
n	times	return
6	[7, 10]	28
"""

test_cases = convert_table_to_test_cases(table_text)