import win32con.client

wshShell = win32con.client.Dispatch("WScript.Shell")
wshShell.Run("notepad.exe")


target_path = "./pptx/sample.pptx"
ppt_app = win32com.client.GetObject(ppt_dir)

def addComment(comment_target):
    for index, ppt_slide in enumerate(ppt_app.Slides):
        if slide_num in comment_target:
            slide.addComment("受け身みっけ！！")