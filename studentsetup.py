from cx_Freeze import *
includefiles=["icon.ico"]
excludes=[]
packages=[]
base=None
if sys.platform=="win32":
    base="Win32GUI"


shortcut_table=[
    ("DesktopShortcut",#shortcut
     "DesktopFolder",# directory_
     "StudentDatasheet",# name
     "TARGETDIR",# component
     "[TARGETDIR]\studenct.exe",#target
     None, # Argument
     None, # Description
     None,# Hotkey
     None,#Icon
     None,#Iconindex
     None,#showcmd
     "TARGETDIR",#Wkdir
     )
]

msi_data={"Shortcut":shortcut_table}
bdist_msi_options={"data":msi_data}
setup(
    version="0.1",
    description="Student Management System Developed by Mahendra paudel",
    author="Mahendra",
    name="Student Management System",
    options={'build_exe': {'include_files': includefiles},"bdist_msi":bdist_msi_options,},
    executables=[
        Executable(
            script="studenct.py",
            base=base,
            icon="icon.ico",
        )
    ]
)