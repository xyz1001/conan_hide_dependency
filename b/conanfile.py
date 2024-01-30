from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout, CMakeToolchain, CMakeDeps
import os


class BConan(ConanFile):
    name = "library_b"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    exports_sources = "*"

    def requirements(self):
        self.requires("library_a/0.1")
        self.requires("fmt/8.1.1")

    def configure(self):
        self.options["fmt"].header_only = False
