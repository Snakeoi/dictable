from src.dictable.dictable import Dictable, csv_to_list_of_dicts, dictable_to_csv


def test_dictable_save_and_load_csv():
    data = [
                {
                    "name": "John",
                    "age": 22,
                    "money": 0.1,
                    "like dogs": True,
                    "like bugs": False,
                    "bills to pay": None,
                }
            ]
    created_dt = Dictable(data)
    dictable_to_csv(created_dt, 'working_files/test_dictable_save_and_load.csv')
    loaded_dt = Dictable(csv_to_list_of_dicts('working_files/test_dictable_save_and_load.csv'))

    assert created_dt.dictable == loaded_dt.dictable
    assert created_dt.table[0][0] == loaded_dt.table[0][0]
    assert created_dt.table[0][1] == loaded_dt.table[0][1]
    assert created_dt.table[0][2] == loaded_dt.table[0][2]
    assert created_dt.table[0][3] == loaded_dt.table[0][3]
    assert created_dt.table[0][4] == loaded_dt.table[0][4]
    assert created_dt.table[0][5] == loaded_dt.table[0][5]

    assert created_dt.table[1][0] == loaded_dt.table[1][0]
    assert created_dt.table[1][1] == loaded_dt.table[1][1]
    assert created_dt.table[1][2] == loaded_dt.table[1][2]
    assert created_dt.table[1][3] == loaded_dt.table[1][3]
    assert created_dt.table[1][4] == loaded_dt.table[1][4]
    assert created_dt.table[1][5] == loaded_dt.table[1][5]


def test_dictable_save_and_load_csv_with_no_auto_type():
    data = [
                {
                    "name": "John",
                    "age": "22",
                    "money": "0.1",
                    "like dogs": "True",
                    "like bugs": "False",
                    "bills to pay": "None",
                }
            ]
    created_dt = Dictable(data)
    dictable_to_csv(created_dt, 'working_files/test_dictable_save_and_load.csv')
    loaded_dt = Dictable(csv_to_list_of_dicts('working_files/test_dictable_save_and_load.csv', exclude_auto_typing='all'))

    assert created_dt.dictable == loaded_dt.dictable
    assert created_dt.table[0][0] == loaded_dt.table[0][0]
    assert created_dt.table[0][1] == loaded_dt.table[0][1]
    assert created_dt.table[0][2] == loaded_dt.table[0][2]
    assert created_dt.table[0][3] == loaded_dt.table[0][3]
    assert created_dt.table[0][4] == loaded_dt.table[0][4]
    assert created_dt.table[0][5] == loaded_dt.table[0][5]

    assert created_dt.table[1][0] == loaded_dt.table[1][0]
    assert created_dt.table[1][1] == loaded_dt.table[1][1]
    assert created_dt.table[1][2] == loaded_dt.table[1][2]
    assert created_dt.table[1][3] == loaded_dt.table[1][3]
    assert created_dt.table[1][4] == loaded_dt.table[1][4]
    assert created_dt.table[1][5] == loaded_dt.table[1][5]


def test_dictable_save_and_load_csv_with_auto_type_exclude():
    data = [
                {
                    "name": "John",
                    "age": "22",
                    "money": "0.1",
                    "like dogs": True,
                    "like bugs": "False",
                    "bills to pay": None,
                }
            ]
    created_dt = Dictable(data)
    dictable_to_csv(created_dt, 'working_files/test_dictable_save_and_load.csv')
    loaded_dt = Dictable(csv_to_list_of_dicts('working_files/test_dictable_save_and_load.csv',
                                     exclude_auto_typing='age, money, like bugs'))

    assert created_dt.dictable == loaded_dt.dictable
    assert created_dt.table[0][0] == loaded_dt.table[0][0]
    assert created_dt.table[0][1] == loaded_dt.table[0][1]
    assert created_dt.table[0][2] == loaded_dt.table[0][2]
    assert created_dt.table[0][3] == loaded_dt.table[0][3]
    assert created_dt.table[0][4] == loaded_dt.table[0][4]
    assert created_dt.table[0][5] == loaded_dt.table[0][5]

    assert created_dt.table[1][0] == loaded_dt.table[1][0]
    assert created_dt.table[1][1] == loaded_dt.table[1][1]
    assert created_dt.table[1][2] == loaded_dt.table[1][2]
    assert created_dt.table[1][3] == loaded_dt.table[1][3]
    assert created_dt.table[1][4] == loaded_dt.table[1][4]
    assert created_dt.table[1][5] == loaded_dt.table[1][5]

