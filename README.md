# タイルマップのxmlからjsonへのpython変換コード  
 
## 概要  
QGIS向けに作成したxmlタイルマップのxml表記からカシミール３D向けのjsonの記述への変換させるためのコードです．  

## xmlファイル
xmlファイルはこちらの「今昔マップXYZ_tile全国版」にあるファイルが対象です．  
https://github.com/japan-road-jp/KonjyakuMap_TileMap_for_QGIS



## 動作確認  
* Python 3.7.6  
* OS: Win 10

## 必要なライブラリー  
glob
xmltodict
json  

ここではElementTreeなどのXMLパーサーを使わず，xmltodictというライブラリーを使い，xmlを辞書構造化させて必要なkey-valueを取得し，それをカシミール３Dの定形のjsonフォーマットへはめ込む方法をとっています．
