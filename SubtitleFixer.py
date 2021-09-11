import os


def fix_encode(file_path:str):
    """ This function gets the subtitle file path, check if the file format is supported,
    and then opens the file in windows-1256 encoding and then creates a new file with utf-8 format """

    name, ext = os.path.splitext(file_path)
    if ext != ".srt":
        raise TypeError(f"{ext} file type not supported")
    
    try:
        with open(file_path, "r") as file1:
            subtitle = file1.read()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="windows-1256") as file1:
            subtitle = file1.read()
    
    new_name = name + "_fixed" + ext

    with open(new_name, "x", encoding="utf-8") as file2:
        file2.write(subtitle)
