from setuptools import setup

setup(
    name='networking_bot',
    version='1.0',
    description = "a bot that send linkedin connection request to your school alumnis",
    url = "https://github.com/leopoldavezac/NetworkingBot",
    author = "Leopold Davezac",
    author_email = "leopoldavezac@gmail.com",
    license = "MIT",
    keywords = "linkedin bot connections networking alumni",
    packages=["networking_bot"],
    install_requires = ["selenium", "pyyaml"],
    python_requires = ">=3",
    entry_points={
    'console_scripts': [
        'network=networking_bot.main:main',
        ]
    }
)