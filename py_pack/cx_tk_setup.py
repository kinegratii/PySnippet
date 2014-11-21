#coding=utf8
"""
cxFreeze的构建脚本
"""
import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
includeFiles = [
     ( r"D:\py\tcl\tcl8.5", "tcl"),  
     ( r"D:\py\tcl\tk8.5", "tk")  
    ]

setup(
        name = "tk_demo",
        version = "1.0",
        description = "A demo for tkinter",
        options = {"build_exe": {"include_files": includeFiles,}},
        executables = [Executable("tk_demo.py",base = base)])

