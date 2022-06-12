import pptx
from pptx.exc import PackageNotFoundError
from JUMAN import juman_passive_single
import glob

target_path = "./pptx/**"
pptx_files = []
files = glob.glob(target_path,recursive=True)

def pptx_start():

    for ispptx in files:
        if ".pptx" in ispptx:
            pptx_files.append(ispptx)

    for pptx_file in pptx_files:
        print(pptx_file)

    for pptx_file in pptx_files:
        # パスワードがかかっているかどうか
        try:
            # Presentation パワポの情報
            prs = pptx.Presentation(pptx_file)
        
        except PackageNotFoundError:
            print(pptx_file)
            print("パスワードがかかっているので開けません")
        
        for slide_num, slide in enumerate(prs.slides, start=0):
            for slide_shape in slide.shapes:
                if slide_shape.has_text_frame: # shapeに含まれるテキストデータ抽出
                    isPassive = juman_passive_single(slide_shape.text)
                    if isPassive == slide_shape.text:
                        addNote(slide)
                
                if slide_shape.has_table: #　テーブル
                    for cell in slide_shape.table.iter_cells():
                        isPassive = juman_passive_single(cell.text)
                        if isPassive == cell.text:
                            addNote(slide)
            
        prs.save(pptx_file)


# ノートの編集
def addNote(slide):
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = "受け身あるかも"


