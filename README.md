<!-- ## Description -->

## Requirement
RaspberryPi3 ModelB  
[Raspberry Pi カメラモジュール V2](https://www.switch-science.com/catalog/2713/)  
[Unicorn HAT HD](https://www.switch-science.com/catalog/3336/)   

## Usage
インストール方法や使い方は[こちらの記事]()を参考にしてください。  

## Index
-emoji-unicornhathd.py  
写真を一回撮り、人の顔が写っていればWeb APIと通信、表情に合わせた絵文字を表示します。  
人の顔がない場合、虫眼鏡の絵文字が出ます。  

-emoji-unicornhathd-stream.py  
emoji-unicornhathd.pyの動作を繰り返します。  
終わりたいときは ctrl + c。  

-test_emoji.py  
色々な絵文字を表示します。  
emoji_256フォルダに入っている絵文字画像を全て表示できます。  
a で前の絵文字、 d で次の絵文字に変えます。  
終わりたいときは a,d 以外のキーを押します。    

-pixel_matrix.py  
新しい絵文字を増やしたいときに使います。  
emojiフォルダに増やしたい画像をいれ、拡張子なしのファイル名を引数にして実行してください。  
16 x 16にリサイズし、emoji_256フォルダに保存、各ピクセルのRGBデータを行列にして、rgbフォルダに保存します。  

## Author

[Kazme Egawa](http://kazme.info)
