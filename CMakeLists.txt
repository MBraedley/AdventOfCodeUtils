# CMakeList.txt : Top-level CMake project file, do global configuration
# and include sub-projects here.
#
cmake_minimum_required (VERSION 3.26)

set(CMAKE_CXX_STANDARD 23)

if (MSVC)
  add_compile_definitions(NOMINMAX _CRT_SECURE_NO_WARNINGS)
endif()

project ("AdventOfCodeUtils")

find_package(ctre REQUIRED)

add_library(Utils STATIC "src/Utils/Utils.cpp" "src/Utils/Utils.h")
target_link_libraries(Utils PUBLIC ctre::ctre)

install( TARGETS Utils )
install( FILES "src/Utils/Utils.h" TYPE INCLUDE)
