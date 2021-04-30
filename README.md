# タイルマップのxmlからjsonへのpython変換コード  
 
## 概要  
QGIS向けに作成したxmlタイルマップのxml表記からカシミール３D向けのjsonの記述への変換させるためのコードです．  

## 使い方

1. `code`で一式をダウンロード
　xmlファイルのオリジナルは下記のサイトとなります．．  
  https://github.com/japan-road-jp/KonjyakuMap_TileMap_for_QGIS

1. .pyをRunさせます．（Spyderなど）  

## 動作確認  
* Python 3.7.6  
* OS: Win 10

## 必要なライブラリー  
* glob
* xmltodict
* json  

ここではElementTreeなどのXMLパーサーを使わず，xmltodictというライブラリーを使い，xmlを辞書構造化させて必要なkey-valueを取得し，それをカシミール３Dの定形のjsonフォーマットへはめ込む方法をとっています．

## 使い方
詳細はこちらを御覧ください．  
https://note.com/notes/nd52eaf9214af/edit

## ライセンス
MITライセンスです．
