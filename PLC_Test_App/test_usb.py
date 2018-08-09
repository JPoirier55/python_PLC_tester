import json

plc_outputs = [{"output_0": 0,
                "output_1": 0,
                "output_2": 0,
                "output_3": 0},
               {"output_0": 0,
                "output_1": 1,
                "output_2": 1,
                "output_3": 0},
               {"output_0": 0,
                "output_1": 0,
                "output_2": 1,
                "output_3": 1},
               {"output_0": 1,
                "output_1": 0,
                "output_2": 1,
                "output_3": 0},
               {"output_0": 1,
                "output_1": 1,
                "output_2": 1,
                "output_3": 0}]

plc_expected_outputs = [{"output_0": 0,
                         "output_1": 0,
                         "output_2": 0,
                         "output_3": 0},
                        {"output_0": 0,
                         "output_1": 0,
                         "output_2": 1,
                         "output_3": 0},
                        {"output_0": 0,
                         "output_1": 0,
                         "output_2": 1,
                         "output_3": 0},
                        {"output_0": 1,
                         "output_1": 0,
                         "output_2": 0,
                         "output_3": 0},
                        {"output_0": 1,
                         "output_1": 1,
                         "output_2": 1,
                         "output_3": 0}]


def run_test():
    with open('testdata_3.json') as f:
        data = json.load(f)
    for test_run in data:
        print(test_run)


if __name__ == "__main__":
    run_test()
