from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

class AdventOfCodeUtils(ConanFile):
    name = "aoc_utils"
    version = "1.0.1"
    settings = "os", "compiler", "build_type", "arch"
    package_type = "static-library"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def requirements(self):
        self.requires("ctre/[*]")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        
    def package_info(self):
        self.cpp_info.components["Utils"].set_property("cmake_target_name", f"{self.name}::Utils")
        self.cpp_info.components["Utils"].libs = [ "Utils" ]
        self.cpp_info.components["Utils"].requires = [ "ctre::ctre" ]
    