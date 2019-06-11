from conans import ConanFile, tools
import os
import shutil


class WAFInstallerConan(ConanFile):
    name = "waf_installer"
    version = "2.0.17"
    url = "https://github.com/czoido/conan-wasf-installer"
    description = "Waf is a Python-based framework for configuring, compiling and installing applications."
    homepage = "https://gitlab.com/ita1024/waf"
    license = "BSD"
    exports_sources = ["LICENSE"]
    
    def build(self):
        source_url = "https://waf.io/waf-%s" % (self.version)
        self.output.warn("Downloading Waf build system: %s" % (source_url))
        tools.download(source_url, "waf")

    def package(self):
        self.copy(pattern="LICENSE", src='.', dst="licenses")
        self.copy('waf', src='.', dst="bin", keep_path=False)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

    def package_id(self):
        del self.info.settings.compiler