from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout, CMakeToolchain, CMakeDeps
import os


class AConan(ConanFile):
    name = "library_a"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    exports_sources = "*"

    def requirements(self):
        self.requires("spdlog/1.13.0", visible=False)

    def configure(self):
        self.options["spdlog"].header_only = True
        self.options["fmt"].header_only = True
