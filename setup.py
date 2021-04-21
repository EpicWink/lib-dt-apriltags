from xml.dom import minidom

from setuptools import setup

POSTFIX = ''

version = minidom.parse('apriltags/package.xml').getElementsByTagName("version")[0].childNodes[0].data

setup(version=version + POSTFIX)
