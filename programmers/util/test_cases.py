from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]
"""

test_cases = convert_table_to_test_cases(table_text)
