import json
import csv


def get_keys(d, key_list=[]):
    all_keys = []
    for key, value in d.items():
        if isinstance(value, dict):
            all_keys.extend(get_keys(value, key_list + [key]))
        else:
            all_keys.append('.'.join(key_list + [key]))
    return all_keys


def get_as_string(l):
    result = ""
    if isinstance(l, list):
        for element in l:
            result += get_as_string(element)
        result = result[:-1]
    elif isinstance(l, dict):
        result += "("
        for key, value in l.items():
            result += f"{key}:{get_as_string(value)}"
        result = result[:-1] + "),"
    else:
        if l is not None:
            result += str(l) + ","
    return result


def get_values(d):
    all_values = []
    for key, value in d.items():
        if isinstance(value, dict):
            all_values.extend(get_values(value))
        elif isinstance(value, list):
            all_values.append(get_as_string(value))
        else:
            all_values.append(value)
    return all_values


def main():
    for dataset in ["countries", "currencies", "uk"]:
        with open(f"../datasets/{dataset}/{dataset}.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        with open(f"../datasets/{dataset}/{dataset}.csv", "w+", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            first_value = next(iter(data.values()))
            writer.writerow(get_keys(first_value))
            for value in data.values():
                writer.writerow(get_values(value))


if __name__ == "__main__":
    main()