__author__ = 'sinlov'

import codecs
import json
import os


class Py3Json:
    """
    for python3 json utils

    use as

    from serialization_utils import Py3Json

    Py3Json.dict_json_beauty(dict)
    """

    def __init__(self):
        pass

    @staticmethod
    def dict_json_printer(json_dict=dict):
        # type: (dict)->None
        """
        print json with utf-8

        :param json_dict: for print dict`
        :return: None
        """
        print(json.dumps(json_dict, ensure_ascii=False))

    @staticmethod
    def dict_json_print_beauty(json_dict=dict):
        # type: (dict)->None
        """
        print json with utf-8 beauty

        :param json_dict: for print dict
        :return: None
        """
        print(json.dumps(json_dict, ensure_ascii=False, indent=4, sort_keys=True))

    @staticmethod
    def dict_json_encoding_utf_8(json_dict=dict):
        # type: (dict)->str
        """
        let python2 Json format utf-8

        :param json_dict: for format dict
        :return: json str
        """
        return json.dumps(json_dict, ensure_ascii=False)

    @staticmethod
    def dict_json_beauty(json_dict=dict):
        # type: (dict)->str
        """
        let python2 Json format more right

        :param json_dict: for format dict
        :return: json str
        """
        return json.dumps(
            json_dict,
            ensure_ascii=False,
            indent=4,
            sort_keys=True,
            separators=(',', ':'),
        )

    @staticmethod
    def json_beauty(obj_json):
        # type: (object)->str
        """
        let python2 Json format more right

        :param obj_json: for format obj
        :return: json str
        """
        return json.dumps(obj_json, ensure_ascii=False, indent=4, sort_keys=True)

    @staticmethod
    def write_json_utf_8_beauty(out_path, json_dict, encode='utf-8', sort_keys=True):
        # type: (str, dict, str, bool) -> None
        js = json.dumps(
            json_dict,
            ensure_ascii=False,
            indent=4,
            sort_keys=sort_keys,
            separators=(',', ':'),
        )
        with codecs.open(out_path, 'w+', encode) as dict_json:
            dict_json.write(js)

    @staticmethod
    def write_json_utf_8(out_path, json_dict):
        # type: (str, dict) -> None
        js = json.dumps(json_dict, ensure_ascii=False)
        with codecs.open(out_path, 'w+', 'utf-8') as dict_json:
            dict_json.write(js)

    @staticmethod
    def write_json(out_path, json_dict, encode='utf-8'):
        # type: (str, dict, str) -> None
        js = json.dumps(json_dict, ensure_ascii=False)
        with codecs.open(out_path, 'w+', encode) as dict_json:
            dict_json.write(js)

    @staticmethod
    def write_dict_to_file(path, json_dict, encode='utf-8'):
        # type: (str, dict, str) -> None
        json_string = json.dumps(json_dict, encoding=encode)
        with open(path, 'w', encoding=encode) as f:
            f.write(json_string)
            f.close()

    @staticmethod
    def read_json_file_to_dict(json_path=str, encode='utf-8'):
        # type: (str, str) -> dict
        if not os.path.exists:
            return {}
        with open(json_path, 'r', encoding=encode) as load_js:
            return json.load(load_js)
