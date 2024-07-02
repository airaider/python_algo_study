from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
citations	return
[10,11,12,13]   4
"""

test_cases = convert_table_to_test_cases(table_text)