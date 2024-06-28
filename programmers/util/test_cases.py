from programmers.util.json_converter import convert_table_to_test_cases

table_text = """
participant completion return
["leo", "kiki", "eden"] ["eden", "kiki"]   "leo"
["marina", "josipa", "nikola", "vinko", "filipa"]   ["josipa", "filipa", "marina", "nikola"]   "vinko"
["mislav", "stanko", "mislav", "ana"]   ["stanko", "ana", "mislav"]    "mislav"
"""

test_cases = convert_table_to_test_cases(table_text)
