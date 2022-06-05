import pptx
from pptx.exc import PackageNotFoundError

import glob

pptx_files = []
target_path = "./pptx/**"

files = glob.glob(target_path,recursive=True)

for ispptx in files:
    if ".pptx" in ispptx:
        pptx_files.append(ispptx)

for pptx_file in pptx_files:
    print(pptx_file)

len(pptx_files)