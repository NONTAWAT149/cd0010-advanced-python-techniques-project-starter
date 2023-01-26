"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.

    # Load data from csv file
    with open(neo_csv_path, 'r') as file:
        reader = csv.reader(file)
        raw_data = []
        for row in reader:
            raw_data.append(row)

        # Collect header and data
        header = raw_data[0]
        raw_data = raw_data[1:]

        # Process data in clean format - list with dictionary
        data_list = []
        for data in raw_data:
            data_list.append({header[i]: data[i] for i in range(len(data))})

        # Select data
        neo_list = []
        for row in data_list:
            neo_list.append(NearEarthObject(pdes = row['pdes'],
                                            name = row['name'],
                                            diameter = row['diameter'],
                                            pha = row['pha']
                                            )
                            )

    return neo_list



def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.

    # Load data
    with open(cad_json_path, 'r') as file:
        contents = json.load(file)

        # Process data to list with dictionary data
        raw_data = contents['data']
        ca_list = []
        for data in raw_data:
            ca_list.append(CloseApproach(des = data[0],
                                         cd = data[3],
                                         dist = data[4],
                                         v_rel = data[7]
                                         )
                           )

    return ca_list
