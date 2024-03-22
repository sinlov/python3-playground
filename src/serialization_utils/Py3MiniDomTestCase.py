import unittest
from xml.dom import minidom
from xml.etree import ElementTree

from serialization_utils.Py3XML import Py3ElementTree, Py3MiniDom


class Py3MiniDomTestCase(unittest.TestCase):
    def test_reade_xml(self):
        print("test read_xml_file")
        document = Py3MiniDom.read_xml_file("test.xml")
        print(document.toxml("utf-8"))
        string_list = document.documentElement.getElementsByTagName("string")
        for string in string_list:
            key = string.getAttribute("name")
            value = string.childNodes[0].data
            print("string key -> {0}, text -> {1}".format(key, value))
        self.assertNotEqual(document, None)

    def test_beauty_write(self):
        print("test beauty_write")
        dom = minidom.Document()
        root_node = dom.createElement("resources")
        root_node.setAttribute("xmlns:ns1", "http://schemas.android.com/tools")
        dom.appendChild(root_node)
        string_dom = dom.createElement("string")
        root_node.appendChild(string_dom)
        string_dom.setAttribute("name", "test_key")
        value_text = dom.createTextNode("test_name")
        string_dom.appendChild(value_text)
        Py3MiniDom.beauty_write(dom, "test_test.xml", newline="\n")
        dom_new = Py3MiniDom.read_xml_file("test_test.xml")
        print(dom_new.toxml("utf-8"))
        root = dom_new.documentElement
        if root.hasAttribute("xmlns:ns1"):
            print("hasAttr xmlns:ns1")
            string_list = root.getElementsByTagName("string")
            for string in string_list:
                key = string.getAttribute("name")
                value = string.childNodes[0].data
                print("string key -> {0}, text -> {1}".format(key, value))
        self.assertNotEqual(dom_new, None)

    def test_fixed_writexml(self):
        print("test fixed_writexml")
        document = Py3MiniDom.read_xml_file("test_fix.xml")
        self.assertNotEqual(document, None)
        print(document.toxml("utf-8"))
        # Py3MiniDom.fixed_writexml(document, 'test_fix_test.xml')
        # Py3MiniDom.del_xml_empty_line('test_fix_test.xml')


class Py2ElementTreeTestCase(unittest.TestCase):
    def test_xml_print(self):
        print("test test_xml_print")
        tree = ElementTree.parse("test.xml")
        root = tree.getroot()
        ElementTree.dump(root)
        self.assertNotEqual(root, None)

    def test_beauty_xml_print(self):
        print("test beauty_format_print")
        tree = ElementTree.parse("test.xml")
        root = tree.getroot()
        Py3ElementTree.beauty_format_print(root)
        self.assertNotEqual(root, None)


if __name__ == "__main__":
    unittest.main()
