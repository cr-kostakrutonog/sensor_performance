import os
import time

from pywinauto import application


def createFileBySize(file_name="", file_size=0):
    try:
        with open(file_name, "w") as f:
            f.write('a' * file_size)
            f.close()
        return 1
    except Exception as e:
        print(e)
        return 0


def openNotepadFile(app, file_name=""):
    try:
        #print("Open notepad")
        # Open file
        app.Notepad.menu_select('File->Open')
        # app.[window title].[control name]...
        app.Open.Edit.set_edit_text(file_name)
        app.Open.Open.click()
        return 1
    except Exception as e:
        print(e)
        return 0


def closeNotepad(app):
    try:
        #print("Close notepad")
        # Close
        app.Notepad.type_keys("%FX")
        return 1
    except Exception as e:
        print(e)
        return 0


# home_dir = os.path.expanduser('~')
# file_path = home_dir + '\\Desktop'
# source_file_name = file_path + '\\ttt.txt'
# size = 1048576 #1MB
# size = 104857600  # 100MB
# size = 134217728 #128MB
# size = 536870912 #512MB
# size = 1073741824 # bytes in 1 GiB
# t0 = time.time()
# createFileBySize(file_name=source_file_name,file_size=size)
# d = time.time() - t0
# print("Creation duration: %.2f s." % d)

# app = application.Application().start('notepad.exe')
# openNotepadFile(app,source_file_name)
# closeNotepad(app)


# Show About
# app.Notepad.menu_select("Help->About Notepad")
# app.AboutNotepad.OK.click()


# Write
# app.wait_cpu_usage_lower(timeout=None)
# app.Notepad.Edit.type_keys ("pywinauto Works!", with_spaces = True)

# Print properties
# app.Notepad.Edit.Properties.print_control_identifiers()

# Save
# app.Notepad.menu_select("File->SaveAs")
# app.Notepad.SaveAs.ComboBox5.select("UTF-8")
# app.SaveAs.edit1.set_text("Example-utf8.txt")
# app.SaveAs.Save.click()
