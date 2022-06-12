from __future__ import unicode_literals # It is not necessary when you use python3.
from pyknp import Juman
import re


def juman_passive_single(juman_target):

    juman = Juman(jumanpp=False)   # default is JUMAN++: Juman(jumanpp=True). if you use JUMAN, use Juman(jumanpp=False)
    comment_target = []

    juman_target = re.sub(r"[\r\n]", "", juman_target)
    juman_target = re.sub(r"[\u3000 \t]", "", juman_target)
    juman_target = re.sub(r"\s", "", juman_target)
    
    juman_result = juman.analysis(target)

    for mrph in juman_result.mrph_list(): # 各形態素にアクセス
        # print("見出し:%s, 読み:%s, 原形:%s, 品詞:%s, 品詞細分類:%s, 活用型:%s, 活用形:%s, 意味情報:%s, 代表表記:%s" \
        # % (mrph.midasi, mrph.yomi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))
        # 品詞細分類が動詞性接尾辞だったら
        if mrph.bunrui == "動詞性接尾辞":
            return target
    
    return ""


