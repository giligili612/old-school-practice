cmake_minimum_required(VERSION 3.28)
project(c)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
include_directories(${PROJECT_SOURCE_DIR})

add_subdirectory(base)
add_subdirectory(linux)
add_subdirectory(perfbook)