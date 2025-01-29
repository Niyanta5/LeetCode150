import json


def add_employees_to_dashboard(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)


salaries = '{"Nina": 300, "Niyanta": 300}'
new_salaries = add_employees_to_dashboard(salaries, "Robus", 399)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Nina"])
print(decoded_salaries["Niyanta"])
print(decoded_salaries["Robus"])
