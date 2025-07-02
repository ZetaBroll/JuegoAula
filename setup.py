from importlib.resources import path
from cx_Freeze import Executable
from setuptools import setup


executables = [Executable("main.py")]

setup(
    name="Montanhas Atiradeiras",
    version="1.0",
    description= "Monatanha atireadei app",
    options= {"build_exe": {"packages": ["pygame"]}},
    executables=executables
)