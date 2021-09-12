#-------------------------------------------------
# xml2json_mapper.py
#
# This software is released under the MIT License.
#-------------------------------------------------
# -*- coding: utf-8 -*-


"""
QGIS向けのタイルマップXMLからカシミール3D向けのタイルマップjson形式へのマッピング変換
xmlは複数ファイルを一括で変換するケースに対応．

"""

__author__ = "くにみち"
__contact__ = "japan.road.jp@gmail.com"
__license__ = "MIT"
__copyright__ = "くにみち"
__version__ = "1.1.0"
__date__ = "2021/4/29"
__reversed__ = "2021/9/12"


# 必要とするライブラリ
import glob
import xmltodict
import json


# ファイル読み込み関数
def read_files(extension):

    # 読み込みファイルの取得
    path = 'xml_file/*.' + extension
    input_files = glob.glob(path)

    # ファイル数の取得
    number_of_files = len(input_files)

    return input_files, number_of_files

#ゲッター・セッター
def get_patameter(f,num):
    tile_name = f['qgsXYZTilesConnections']['xyztiles'][num]['@name']
    tile_url = f['qgsXYZTilesConnections']['xyztiles'][num]['@url']
    max_zoom = f['qgsXYZTilesConnections']['xyztiles'][num]['@zmax']
    
    return tile_name, tile_url, max_zoom

def set_patameter(tile_name, tile_url, max_zoom):
    kashmir[0]["name"]= tile_name
    kashmir[0]["url"]= tile_url.replace('http://', '').replace('{z}/{x}/{-y}.png', '$Z/$X/$Y')
    kashmir[0]["max_zoom"]= max_zoom
    
    return

# カシミール3Dのjsonスキーマ
kashmir = [{
    "name":"",
    "copyright":"今昔マップ on the web",
    "url":"",
    "ext":"png",
    "no_ext":"false",
    "port":"80",
    "url_type":"standard",
    "denshi-kokudo_type":"map",
    "origin":"bottom_left",
    "min_zoom":"8",
    "max_zoom":"",
    "dem":"false",
    "dem_type":"yamatabi",
    }]


# 実行処理
def main():
    #QGISのタイルレイヤの拡張子
    default_extension = 'xml'
    
    #ファイルの読み込み
    [flist, f_num] = read_files(default_extension)

    for i in range(f_num):
        
        with open (flist[i],'r' ,encoding='utf-8') as f:
            xml_text = f.read()
    
        # xmlを辞書構造に変換
        dict = xmltodict.parse(xml_text)

        #xmlにかかれているタイルマップの数を取得
        number_of_map = len(dict['qgsXYZTilesConnections']['xyztiles'])

        # ゲッターで必要なパラメータを読み出しとセッターで書き込み
        for j in range(number_of_map):
            tile_name, tile_url, max_zoom = get_patameter(dict,j)
            set_patameter(tile_name, tile_url, max_zoom)
  
            # jsonファイルとして出力
            with open(tile_name + '.json', 'w', encoding='utf-8') as f:
                json.dump(kashmir,f, indent = 0, ensure_ascii=False)
                print (kashmir) 
    

if __name__ == '__main__':
    main()


    
      