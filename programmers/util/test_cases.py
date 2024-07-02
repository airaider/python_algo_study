from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
brown	yellow	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
"""

test_cases = convert_table_to_test_cases(table_text)