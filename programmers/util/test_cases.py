from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
"""

test_cases = convert_table_to_test_cases(table_text)