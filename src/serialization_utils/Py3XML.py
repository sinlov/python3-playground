import codecs
import os
import re
from xml.dom import minidom
from xml.etree import ElementTree

__author__ = "sinlov"


class Py3MiniDom:
    """
    use as python2 minidom

    from tools.py2_xml import Py2MiniDom

    dom = minidom.parse('test.xml')

    Py2MiniDom.beauty_write(dom, 'test_test.xml')
    """

    def __init__(self):
        pass

    @staticmethod
    def read_xml_file(xml_path=str):
        # type: (str) -> minidom.Document
        """
        read xml file as minidom.Document

        :param xml_path: xml path
        :return: minidom.Document or Exception
        """
        try:
            if os.path.exists(xml_path):
                with open(xml_path, "r", encoding="UTF-8") as fh:
                    parse = minidom.parse(fh)
                    if parse:
                        return parse
                    else:
                        print("Error read_xml_file {0}".format("dom is None"))
            else:
                raise Exception("path not found {0}".format(xml_path))
        except Exception as ex:
            print("Error read_xml_file {0}".format(ex))
            pass

    @staticmethod
    def beauty_write(
        document, target_file_path=str, add_indent="\t", indent="", newline="", encode="utf-8"
    ):
        # type: (minidom.Document, str, str, str, str, str) -> None
        """
        beauty xml write

        :param document: for write document
        :param target_file_path: target xml path
        :param indent: sub element indent, default is ''
        :param add_indent: add sub element indent, default is \\\\t
        :param newline: sub element newline, default is ''
        :param encode: write encode, default is utf-8
        :return: None or print Exception
        """
        try:
            dom_copy = document.cloneNode(True)
            f = open(target_file_path, "wb")
            writer = codecs.lookup("utf-8")[3](f)
            dom_copy.writexml(
                writer, indent=indent, addindent=add_indent, newl=newline, encoding=encode
            )
            dom_copy.unlink()
            f.close()
        except Exception as ex:
            print("Error beauty_write -> {0}".format(ex))
            pass

    @staticmethod
    def Indent(dom, node, indent=0):
        # Copy child list because it will change soon
        children = node.childNodes[:]
        # Main node doesn't need to be indented
        if indent:
            text = dom.createTextNode("\n" + "\t" * indent)
            node.parentNode.insertBefore(text, node)
        if children:
            # Append newline after last child, except for text nodes
            if children[-1].nodeType == node.ELEMENT_NODE:
                text = dom.createTextNode("\n" + "\t" * indent)
                node.a(text)
                # Indent children which are elements
                for n in children:
                    if n.nodeType == node.ELEMENT_NODE:
                        Py3MiniDom.Indent(dom, n, indent + 1)
        pass

    @staticmethod
    def del_xml_empty_line(file_path):
        """Delete blanklines of infile"""
        try:
            if os.path.exists(file_path):
                result = list()
                in_fp = open(file_path, "r")
                for line in in_fp.readlines():
                    if not re.match(r"^\s*$", line):
                        result.append(line)
                in_fp.close()
                # print('start del_xml_empty_line count {0}'.format(len(result)))
                if len(result) > 0:
                    out_fp = open(file_path, "w")
                    out_fp.write("%s" % "".join(result))
                    out_fp.close()
        except Exception as ex:
            print("Error del_blank_line -> {0}".format(ex))
            pass


class Py3ElementTree:
    """
    for XML beauty

    use like

    tree = ElementTree.parse('test.xml')

    root = tree.getroot()

    Py3ElementTree.beauty_format(root)
    """

    def __init__(self):
        pass

    @staticmethod
    def beauty_format(element, indent="\t", newline="\n", level=0):
        # type: (ElementTree, str, str, int) -> None
        """
        beauty XML

        :param element: for beauty XML element
        :param indent: indent of XML,  default is \\\\t
        :param newline: newline of XML, default is \\\\n
        :param level: element level of XML, default is 0
        :return: None this method only do element beauty
        """
        if element is not None:  # 判断element是否有子元素
            if element.text is None or element.text.isspace():  # 如果element的text没有内容
                element.text = newline + indent * (level + 1)
            else:
                element.text = (
                    newline
                    + indent * (level + 1)
                    + element.text.strip()
                    + newline
                    + indent * (level + 1)
                )
                # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
                # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
        temp = list(element)  # 将 element 转成list
        for sub_element in temp:
            if temp.index(sub_element) < (
                len(temp) - 1
            ):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
                sub_element.tail = newline + indent * (level + 1)
            else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
                sub_element.tail = newline + indent * level
                # 对子元素进行递归操作
                Py3ElementTree.beauty_format(sub_element, indent, newline, level=level + 1)

    @staticmethod
    def beauty_format_print(element, indent="\t", newline="\n", level=0):
        # type: (ElementTree, str, str, int) -> None
        """
        print beauty XML

        :param element: for beauty XML element
        :param indent: indent of XML,  default is \\\\t
        :param newline: newline of XML, default is \\\\n
        :param level: element level of XML, default is 0
        :return: None this method only do element beauty
        """
        Py3ElementTree.beauty_format(element, indent, newline, level)
        ElementTree.dump(element)
