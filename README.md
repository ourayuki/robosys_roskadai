# ロボットシステム学 課題2

## 概要
rosを用いてランダムに文章が生成される動作を行いました。  
count.pyはyou get + robosys,all,unkのうちどれかが選ばれ出力されます。  
twice.pyはcount.pyの文章にcredit,garbageどちらかを選んで付け足し表示します。  
例　You get robosys credit  , You get unk garbage  
creditが出力される確率は低めです。

## 起動方法
    $ roscore  
    $ rosrun [pkg_name] count.py  
    $ rosrun [pkg_name] twice.py
      
## デモ動画URL
https://www.youtube.com/watch?v=HD_IXGFS5AY&feature=youtu.be

## 参考URL
こちらを参考に作成しました。
https://ryuichiueda.github.io/robosys2019/lesson13.html#/1
