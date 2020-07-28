from conans import ConanFile, tools

class App2(ConanFile):
    name = "App2"
    version = "1.0"
    settings = "os", "arch", "compiler", "build_type"

    generators = "make"

    scm = {"type": "git",
           "url": "http://gitbucket/root/App2.git",
           "revision": "auto"}

    def requirements(self):
        self.requires("libC/1.0@mycompany/demo")

    def build(self):
        print("|-----------------------------------------|")
        print("|-------------   BUILDING   --------------|")
        print("|---------------   App   ----------------|")
        print("|-----------------------------------------|")
        with tools.environment_append({"INCLUDE_MAKEFILE": "conanbuildinfo.mak"}):
            self.run("make exe")

    def package(self):
        self.copy("LICENSE", dst="licenses")
        self.copy("*.a", dst="lib")
        self.copy("*.so", dst="lib")
        self.copy("*.h", dst="include", src="include")

