from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
nums    result
[3,1,2,3]   2
[3,3,3,2,2,4]   3
[3,3,3,2,2,2]   2
"""

test_cases = convert_table_to_test_cases(table_text)