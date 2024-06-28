import re


def convert_table_to_test_cases(table_text):
    lines = table_text.strip().split('\n')
    columns = re.findall(r'\w+', lines[0])

    test_cases = []
    for line in lines[1:]:
        values = re.findall(r'\[.*?\]|"[^"]*"|\w+', line)
        values = [eval(val) if val.startswith('[') else val.strip('"') for val in values]

        input_dict = {columns[i]: values[i] for i in range(len(columns) - 1)}
        test_case = {
            "input": input_dict,
            "expected": values[-1]
        }
        test_cases.append(test_case)

    return test_cases