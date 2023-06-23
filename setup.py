from cx_Freeze import setup, Executable
excludes = ["asyncio", "concurrent", "ctypes", "distutils", "email", "html", "http", "bz2", "decimal"
            "logging", "pydoc_data", "test", "tkinter", "unittest", "urllib", "xml", "xmlrpc", "hashlib", "lzma",
            "_socket"]
options = {
    "build_exe": {
        "include_msvcr": True,
        "excludes": excludes
    }
}
setup(
    name="Scrambler",
    version="1.0",
    author="X1Z53",
    description="Program for project activities, working with ciphers",
    executables=[Executable("main.py", icon="shield.ico")],
    options=options
)