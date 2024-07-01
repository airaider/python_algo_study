from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
"""

test_cases = convert_table_to_test_cases(table_text)