from setuptools import setup

# install requirements of the project
with open("requirements.txt") as req:
    install_requires = req.read()

setup(name='task-lectures',
      version="0.0.1",
      description="",
      url="",
      author="Yuri Mussi",
      author_email="ymussi@gmail.com",
      license="BSD",
      keywords="Yuri Mussi",
      packages=["task_lectures"],
      zip_safe=False
      ),