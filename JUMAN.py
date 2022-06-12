from __future__ import unicode_literals # It is not necessary when you use python3.
from pyknp import Juman

import re

def juman_app(pptx_taple):
    extracted_pptx_texts = []
    extracted_pptx_pathes = []
    extracted_pptx_slide_num = []
    
    extracted_pptx_texts,extracted_pptx_pathes,extracted_pptx_slide_num = pptx_taple
    
    juman_Foward = juman_passive(extracted_pptx_texts)


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


def juman_passive(target_list):
    
    comment_target = []
    tmpp_target = ["ラプラスはかわいい","ラプラスはかっこいい"]

    print("target_list")
    print(tmpp_target)
    str1 = "ラプラスはかわいい"
    str2 = "ラプラスはかっこいい"
    juman_result = juman.analysis(str1)

    for mrph in juman_result.mrph_list(): # 各形態素にアクセス
        print("見出し:%s, 読み:%s, 原形:%s, 品詞:%s, 品詞細分類:%s, 活用型:%s, 活用形:%s, 意味情報:%s, 代表表記:%s" \
        % (mrph.midasi, mrph.yomi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))
        # 品詞細分類が動詞性接尾辞だったら
        if mrph.bunrui == "動詞性接尾辞":
            comment_target.append(juman_target)
            print("受け身かも！！")
        print()

    # for index, juman_target in enumerate(tmpp_target):

    #     print("juman_target")
    #     print(juman_target)
        
    #     juman_result = juman.analysis(str2)
    #     if not juman_result:
    #         print("ないよ！！　" + juman_target)

    #     for mrph in juman_result.mrph_list(): # 各形態素にアクセス
    #         print("見出し:%s, 読み:%s, 原形:%s, 品詞:%s, 品詞細分類:%s, 活用型:%s, 活用形:%s, 意味情報:%s, 代表表記:%s" \
    #         % (mrph.midasi, mrph.yomi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))
    #         # 品詞細分類が動詞性接尾辞だったら
    #         if mrph.bunrui == "動詞性接尾辞":
    #             comment_target.append(juman_target)
    #             print("受け身かも！！")
    #     print()

    print("comment_target")
    print(comment_target)

    return comment_target


def sort(extracted_pptx_texts):
    return_extracted_pptx_texts = []
    count = 0
    if len(extracted_pptx_texts) % 2 == 0:
        print(len(extracted_pptx_texts))
        
        while count < len(extracted_pptx_texts):
            return_extracted_pptx_texts.append(extracted_pptx_texts[count + 1])
            return_extracted_pptx_texts.append(extracted_pptx_texts[count])
            count += 2

        print(return_extracted_pptx_texts)
    else:
        print(len(extracted_pptx_texts))
        while count < len(extracted_pptx_texts) - 1:
            return_extracted_pptx_texts.append(extracted_pptx_texts[count + 1])
            return_extracted_pptx_texts.append(extracted_pptx_texts[count])
            count += 2
        return_extracted_pptx_texts.append(extracted_pptx_texts[count])
        print(return_extracted_pptx_texts)
    

    return return_extracted_pptx_texts
