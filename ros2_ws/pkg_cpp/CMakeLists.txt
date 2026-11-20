cmake_minimum_required(VERSION 3.20)
project(pkg_cpp)

# 如果使用GCC和Clang则额外添加编译选项
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# 手动添加其它依赖项
# find_package(<dependency> REQUIRED)

# 基本不管这一段
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# 调用ament_package()宏，它设置了包安装的目标和ament相关的一些构建属性
ament_package()
