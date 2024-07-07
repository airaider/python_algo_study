from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3
"""

test_cases = convert_table_to_test_cases(table_text)