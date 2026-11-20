# 导入setuptools的find_package和setup函数
from setuptools import find_packages, setup

# 定义包名
package_name = 'pkt_py'

# 使用setup定义包的安装信息
setup(
    name=package_name,  # 包名
    version='0.0.0',    # 版本号
    packages=find_packages(exclude=['test']),   # 使用find_packages自动发现包，排除test目录
    # 定义需要安装的数据文件
    data_files=[
        # 数据文件需要安装到的目录，安装到该目录的文件列表
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']}, # 包内其他非py文件也一起打包安装，比如要一起打包json、xml等都在此处加上
    # 安装包所依赖的其他安装包
    install_requires=['setuptools'],
    # 指示该包是否可以被安全的作为zip文件安装
    zip_safe=True,
    maintainer='hzk',
    maintainer_email='hzk@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    # 声明可选依赖项
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # 如果有命令行工具，在此处添加条目
            # 比如： my_command = learning_pkg_py.my_module:main_func
        ],
    },
)
