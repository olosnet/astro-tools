# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x01\x73\
\x3c\
\x73\x76\x67\x20\x78\x6d\x6c\x6e\x73\x3d\x22\x68\x74\x74\x70\x3a\
\x2f\x2f\x77\x77\x77\x2e\x77\x33\x2e\x6f\x72\x67\x2f\x32\x30\x30\
\x30\x2f\x73\x76\x67\x22\x20\x77\x69\x64\x74\x68\x3d\x22\x32\x34\
\x22\x20\x68\x65\x69\x67\x68\x74\x3d\x22\x32\x34\x22\x20\x76\x69\
\x65\x77\x42\x6f\x78\x3d\x22\x30\x20\x30\x20\x32\x34\x20\x32\x34\
\x22\x20\x66\x69\x6c\x6c\x3d\x22\x6e\x6f\x6e\x65\x22\x20\x73\x74\
\x72\x6f\x6b\x65\x3d\x22\x63\x75\x72\x72\x65\x6e\x74\x43\x6f\x6c\
\x6f\x72\x22\x20\x73\x74\x72\x6f\x6b\x65\x2d\x77\x69\x64\x74\x68\
\x3d\x22\x32\x22\x20\x73\x74\x72\x6f\x6b\x65\x2d\x6c\x69\x6e\x65\
\x63\x61\x70\x3d\x22\x72\x6f\x75\x6e\x64\x22\x20\x73\x74\x72\x6f\
\x6b\x65\x2d\x6c\x69\x6e\x65\x6a\x6f\x69\x6e\x3d\x22\x72\x6f\x75\
\x6e\x64\x22\x20\x63\x6c\x61\x73\x73\x3d\x22\x66\x65\x61\x74\x68\
\x65\x72\x20\x66\x65\x61\x74\x68\x65\x72\x2d\x63\x6c\x69\x70\x62\
\x6f\x61\x72\x64\x22\x3e\x3c\x70\x61\x74\x68\x20\x64\x3d\x22\x4d\
\x31\x36\x20\x34\x68\x32\x61\x32\x20\x32\x20\x30\x20\x30\x20\x31\
\x20\x32\x20\x32\x76\x31\x34\x61\x32\x20\x32\x20\x30\x20\x30\x20\
\x31\x2d\x32\x20\x32\x48\x36\x61\x32\x20\x32\x20\x30\x20\x30\x20\
\x31\x2d\x32\x2d\x32\x56\x36\x61\x32\x20\x32\x20\x30\x20\x30\x20\
\x31\x20\x32\x2d\x32\x68\x32\x22\x3e\x3c\x2f\x70\x61\x74\x68\x3e\
\x3c\x72\x65\x63\x74\x20\x78\x3d\x22\x38\x22\x20\x79\x3d\x22\x32\
\x22\x20\x77\x69\x64\x74\x68\x3d\x22\x38\x22\x20\x68\x65\x69\x67\
\x68\x74\x3d\x22\x34\x22\x20\x72\x78\x3d\x22\x31\x22\x20\x72\x79\
\x3d\x22\x31\x22\x3e\x3c\x2f\x72\x65\x63\x74\x3e\x3c\x2f\x73\x76\
\x67\x3e\
"

qt_resource_name = b"\
\x00\x05\
\x00\x6f\xa6\x53\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x73\
\x00\x09\
\x00\x69\x8c\xe4\
\x00\x63\
\x00\x6c\x00\x69\x00\x70\x00\x62\x00\x6f\x00\x61\x00\x72\x00\x64\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x10\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x10\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x7c\x6b\xdb\x92\x8d\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
