load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.2.0/rules_python-0.2.0.tar.gz",
    sha256 = "778197e26c5fbeb07ac2a2c5ae405b30f6cb7ad1f5510ea6fdac03bded96cc6f",
)

# load("@rules_python//python:pip.bzl", "pip_install")

# pip_install(
#     name = "my_python_deps",
#     requirements = "//third_party:requirements.txt",
# )

http_archive(
    name = "dpu_rules_pyenv",
    sha256 = "8ca32471f14f4a831f58333c54bb4b0f6cc8cc00e73a93d9a878f5f1fb5019c0",
    strip_prefix = "rules_pyenv-0.2.0",
    urls = ["https://github.com/digital-plumbers-union/rules_pyenv/archive/v0.2.0.tar.gz"],
)

load("@dpu_rules_pyenv//pyenv:defs.bzl", "pyenv_install")

pyenv_install(
    # hermetic = False,
    py2 = "2.7.18",
    py3 = "3.9.2",
)