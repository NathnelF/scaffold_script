
import os
import sys
from pathlib import Path

def create_cpp_project(project_name):
    project_path = Path(project_name)
    project_path.mkdir(exist_ok=True)

    (project_path / "src").mkdir(exist_ok=True)
    (project_path / "build").mkdir(exist_ok=True)
    (project_path / "include").mkdir(exist_ok=True)
    (project_path / "lib").mkdir(exist_ok=True)

    cmake_content = """cmake_minimum_required(VERSION 3.15...4.0)

project({project_name})
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable(main src/main.cpp)
""".format(project_name=project_name)

    (project_path / "CMakeLists.txt").write_text(cmake_content)

    main_file = """#include <stdio.h>

int main(void)
{
    printf("Hello, World!\\n");
    return 0;
}
"""
    (project_path / "src" / "main.cpp").write_text(main_file)

    gitignore = """build/
*.o
*.exe
"""

    (project_path / ".gitignore").write_text(gitignore)

    just_content = """cmake:
    cmake -G "Ninja" -B build

build:
     cmake --build build

run: build
     ./build/main
     """

    (project_path / "Justfile").write_text(just_content)
    
    print(f"{project_name} create successfully");


def create_c_project(project_name):
    project_path = Path(project_name)
    project_path.mkdir(exist_ok=True)

    (project_path / "src").mkdir(exist_ok=True)
    (project_path / "build").mkdir(exist_ok=True)
    (project_path / "include").mkdir(exist_ok=True)
    (project_path / "lib").mkdir(exist_ok=True)

    cmake_content = """cmake_minimum_required(VERSION 3.15...4.0)

project({project_name})
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable(main src/main.c)
""".format(project_name=project_name)

    (project_path / "CMakeLists.txt").write_text(cmake_content)

    main_file = """#include <stdio.h>

int main(void)
{
    printf("Hello, World!\\n");
    return 0;
}
"""
    (project_path / "src" / "main.c").write_text(main_file)

    gitignore = """build/
*.o
*.exe
"""

    (project_path / ".gitignore").write_text(gitignore)

    just_content = """cmake:
    cmake -G "Ninja" -B build

build:
     cmake --build build

run: build
     ./build/main
     """

    (project_path / "Justfile").write_text(just_content)
    
    print(f"{project_name} created successfully!");
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        if (sys.argv[1] == "c"):
            create_c_project(sys.argv[2])
        elif (sys.argv[1] == "cpp"):
            create_cpp_project(sys.argv[2])
        else:
            print("please provide a valid language: (c or cpp)")
        
    else:
        print("Usage: scaffold.py <language> (c or cpp) <project name> (one word max)")
            

