"""
Working with tables as dictionary lists.

The Dictable class object allows you to work with a table as a list of dictionaries. In any coin,
you can get from it a table with headings or the rows themselves as lists of lists.
You can also get the headers themselves as a list of strings.

Auxiliary methods allow you to write and read object to a CSV file.
"""

from typing import List, Union
import csv


class DictableError(Exception):
    """
    The Exception class reserved for the Dictable object.
    """
    def __init__(self, message):
        """
        :param message: message to be displayed when error is raised
        """
        super().__init__(message)


class Dictable:
    """
    The class allows you to create a table object, which is edited as a list of dictionaries. On creation,
    it takes an parameter (list_of_dicts) of a list of dictionaries, or an empty list. This one becomes
    the parameter self.dictable. It can be changed at will.

    Entering a parameter other than a dictionary list for list_of_dicts will raise a DictableError.

    The created object will also have read-only properties:
    - headers - a list of strings that are table headers.
    - rows - rows of the table as a list of lists.
    - table - a list of lists consisting of header and rows properties.
    """

    def __init__(self, list_of_dicts: List[dict]):
        """
        :param list_of_dicts: List of dictionaries.
        """
        self.dictable = self.implement(list_of_dicts)

    @property
    def headers(self) -> List[str]:
        """
        :return: list of strings that are table headers - These headers are generated based
        on the dictionary keys contained in self.dictable.
        """
        self.validate(self.dictable)
        headers: list[str] = []
        for i in self.dictable:
            for key in i.keys():
                if key not in headers:
                    headers.append(key)

        return headers

    @property
    def rows(self) -> List[list]:
        """
        :return: rows of the table as a list of lists.
        """
        rows: List[list] = []
        for i in self.dictable:
            row: list = []
            for header in self.headers:
                try:
                    row.append(i[header])
                except KeyError:
                    row.append(None)
            rows.append(row)
        return rows

    @property
    def table(self) -> List[list]:
        """
        :return: a list of lists consisting of header and rows properties
        """
        table: List[list] = self.rows
        if self.headers:
            table.insert(0, self.headers)
        return table

    def validate(self, list_of_dicts: List[dict]) -> None:
        """
        Checks if the parameter is a list of dictionaries. If it is not it raises a DictableError.
        It returns no value.

        :param list_of_dicts: list of dictionaries for validation
        :raise: DictableError if list_of_dicts is not a list of dictionaries.
        :return: nothing
        """
        """
        """
        if type(list_of_dicts) != list:
            raise DictableError('wrong structure: object is not list')
        for row in list_of_dicts:
            if type(row) != dict:
                raise DictableError('wrong structure: row is not dict')

    def implement(self, list_of_dicts: List[dict]) -> List[dict]:
        """
        Triggers the self.validate method and returns the accepted parameter.

        :param list_of_dicts: A list of dictionaries to be taken as self.dictable.
        :return: unchanged list_of_dicts
        """
        self.validate(list_of_dicts)
        return list_of_dicts


def auto_type(string: str) -> Union[str, int, float, bool, None]:
    """
    Automatically changes the data type from string to int, float, bool, or None if possible.
    Otherwise, it returns the accepted, unchanged parameter.

    :param string: string for typing
    :return: typed data str, int, float, bool or None
    """
    if string == '':
        return None
    else:
        try:
            if '.' in string:
                value = float(string)
            else:
                value = int(string)
            return value
        except ValueError:
            if string == 'True':
                return True
            elif string == 'False':
                return False
            else:
                return string


def get_headers_from_csv(path, delimiter: str = ",", quotechar: str = '"') -> List[str]:
    """
    I take as parameters the path to the CSV file and optionally delimiter and quote char.

    Extracts the first row from the CSV sheet. Returns it as a list of strings.
    For a CSV file to be interpretable as a Dictable, the first row must have table headers.

    This function comes in handy when you open an empty CSV file that only has headers.
    Because there will be no header information in the Dicktable object created from such a file.
    This is for the fact that they are generated from the dictionary keys stored in self.dictable.

    :param path: path with filename
    :param delimiter: a character that separates cells in a row of a CSV file
    :param quotechar: CSV file string delimiter
    :return: list of table headings
    """
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        table = []
        for row in reader:
            table.append(row)
            return row


def csv_to_list_of_dicts(path, delimiter: str = ",", quotechar: str = '"', encoding: str = "utf-8",
                         exclude_auto_typing: str = '') -> List[dict]:
    """
    I take as parameters the path to the CSV file and optionally delimiter, quote char, encoding for reading file.
    (encoding is set to utf-8 by default) and information about columns excluded from automatic typing.

    Returns a list of dictionaries.

    :param path: path with filename
    :param delimiter: character that separates cells in a row of a CSV file
    :param quotechar: CSV file string delimiter
    :param encoding: coding to read the CSV file - The default is set to "utf-8".
    :param exclude_auto_typing: An empty string means that all data is to be automatically typed.
    A value of "all" will mean that no columns will be typed. If you specify comma-separated header names
    (example: "Name, Age, Home address"), they will be excluded from typing.
    Note: The headers in the CSV file must not have spaces at the beginning and end.
    :return: CSV file table rows as a list of dictionaries
    """
    with open(path, "r", encoding=encoding) as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        table = []
        for row in reader:
            table.append(row)

    list_of_dicts: List[dict] = []
    if len(table) > 1:
        if exclude_auto_typing == '':
            row_dict: dict = {}
            for row in table[1:]:
                for index, value in enumerate(row):
                    row_dict[table[0][index]] = auto_type(value)
                list_of_dicts.append(row_dict)
        elif exclude_auto_typing == 'all':
            row_dict: dict = {}
            for row in table[1:]:
                for index, value in enumerate(row):
                    row_dict[table[0][index]] = value
                list_of_dicts.append(row_dict)
        else:
            excluded_headers = exclude_auto_typing.split(',')
            for idx, v in enumerate(excluded_headers):
                excluded_headers[idx] = v.strip()
            row_dict: dict = {}
            for row in table[1:]:
                for index, value in enumerate(row):
                    if table[0][index] in excluded_headers:
                        row_dict[table[0][index]] = value
                    else:
                        row_dict[table[0][index]] = auto_type(value)
                list_of_dicts.append(row_dict)
    return list_of_dicts


def dictable_to_csv(dictable: Dictable, path, delimiter: str = ",", quotechar: str = '"', encoding="utf-8") -> None:
    """
    Saves the data of the Dictable class object to a CSV file.

    :param dictable: object of the Dictable class
    :param path: path with filename
    :param delimiter: a character that separates cells in a row of a CSV file
    :param quotechar: CSV file string delimiter
    :param encoding: coding to read the CSV file - The default is set to "utf-8".
    :return: nothing
    """
    with open(path, 'w', encoding=encoding, newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in dictable.table:
            writer.writerow(row)
