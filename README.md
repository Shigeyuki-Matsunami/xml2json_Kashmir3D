# 今昔マップの旧版地形図タイルマップ：QGIS用のタイルマップのxmlフォーマットからカシミール3Dのjsonフォーマットへの変換コード  
 
## 概要  
今昔マップの旧版地形図タイルマップでQGIS向けに作成したxmlタイルマップのxml表記からカシミール３D向けのjsonの記述への変換させるためのコードです．  

xmlファイルのオリジナルは下記のサイトとなります.   
 https://github.com/japan-road-jp/KonjyakuMap_TileMap_for_QGIS

## 背景情報
【GIS】#14　カシミール３D向け　今昔マップの旧版地形図タイルマップjsonファイル一式の公開．  
https://note.com/smatsu/n/na30de88b8f27


## 使い方

【1】`code`ボタンから一式をダウンロード．  
【2】xml2json_converter.pyをRunさせます．そうすると，フォルダ内で.jsonファイルが生成されます．  

## 動作確認  
* Python 3.7.6  
* OS: Win 10

## 必要なライブラリー  
* glob
* xmltodict
* json  

ここではElementTreeなどのXMLパーサーを使わず，xmltodictというライブラリーを使い，xmlを辞書構造化させて必要なkey-valueを取得し，それをカシミール３Dの定形のjsonフォーマットへはめ込む方法をとっています．

## ライセンス
MITライセンスです．
