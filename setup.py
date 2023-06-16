import sys
from cx_Freeze import setup, Executable

main_file = "main.py"

executables = [Executable(main_file, base=None)]

build_options = {
    "packages": ["pygame", "tkinter"],
    "excludes": [],
    "include_files": ["fundo.jpg", "nave.png", "SomNave.mp3"],  
    "build_exe": "build"  
}

setup(
    name="Nome do Projeto",
    version="1.0",
    description="Descrição do Projeto",
    options={"build_exe": build_options},
    executables=executables
)