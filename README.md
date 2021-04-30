# xml2json_Kashmir3D
 
QGIS向けに作成したxmlタイルマップのxml表記からカシミール３D向けのjsonの記述への変換させるためのコードです．  

# 必要なライブラリー  
glob
xmltodict
json  

ここではElementTreeなどのXMLパーサーを使わず，xmltodictというライブラリーを使い，xmlを辞書構造化させて必要なkey-valueを取得し，それをカシミール３Dの定形のjsonフォーマットへはめ込む方法をとっています．
