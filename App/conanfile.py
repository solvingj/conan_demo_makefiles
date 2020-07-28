from conans import ConanFile, tools

class App(ConanFile):
    name = "App"
    version = "1.0"
    settings = "os", "arch", "compiler", "build_type"

    generators = "make"

    scm = {"type": "git",
           "url": "http://gitbucket/root/App.git",
           "revision": "auto"}

    def requirements(self):
        self.requires("libD/1.0@mycompany/demo")

    def build(self):
        print("|-----------------------------------------|")
        print("|-------------   BUILDING   --------------|")
        print("|---------------   App   ----------------|")
        print("|-----------------------------------------|")
        with tools.environment_append({"INCLUDE_MAKEFILE": "conanbuildinfo.mak"}):
            self.run("make exe")

    def package(self):
        self.copy("LICENSE", dst="licenses")
        self.copy("*.a", dst="lib", src="out")
        self.copy("*.so", dst="lib", src="out")
        self.copy("*.bin", dst="bin", src="out")
        self.copy("*.h", dst="include", src="include")
