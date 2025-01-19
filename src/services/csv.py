import csv


def create_csv_from_dict(dictionary: dict, filename: str):
    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")

        writer.writerow(["Erfüllungsgrad", "Anzahl"])

        for key, value in dictionary.items():
            writer.writerow([str(key).replace('.', ','), value])
