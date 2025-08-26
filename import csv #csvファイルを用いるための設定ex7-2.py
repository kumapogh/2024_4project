import csv           #csvファイルを用いるための設定
looktime = 0         #looktime（比較回数）の初期値は0
swich = 0            #swich（入れ替え回数）の初期値は0

class Item:          #クラス、Itemの定義
  def __init__ (self, number:int, name:str, score:int):#クラスの設定
   self.number = number       #生徒番号の設定
   self.name = name           #名前の設定
   self.score = score         #成績の設定

def aditem(item_list,number:int,name:str,score:int):#クラスに要素を追加する関数
  item_list.append(Item(number,name,score))#リストに要素を追加

def csvreader(filename:str, item_list):  #CSVファイルを読み込む関数
  with open(filename,'r') as f:          #指定されたファイルを開く
    csvr = csv.reader(f)                 #CSVファイルの読み込み
    next(csvr)                           #読み込みをスキップ
    for row in csvr:                     #CSVファイルの1行ずつに対して
      number = int(row[0])               #学籍番号はint型
      name = str(row[1])                 #名前はstr型
      score = int(row[2])                #成績はint型
      aditem(item_list, number, name, score)   #これらをリストに追加

def outout(item_list,newfile):            #出力関数
  global looktime,swich                   #looktimeとswichをグローバル変数とする
  looktime = 0                            #looktimeの初期値は0
  swich = 0                               #swichの初期値は0
  alist = quicksort(item_list,0, len(item_list)-1)           #alistの値をクイックソートで並び替えた関数とする
  f = open(newfile,"w")                                      #newfileをfとして開く
  quicksort(item_list,0, len(item_list)-1)                   #クイックソート関数の呼び出し
  print("比較回数="+str(looktime),"入れ替え回数="+str(swich)) #比較回数と入れ替え回数の出力
  for item in alist:                                         #alistのそれぞれのitemに対して
    f.write(f"{item.number:4},{item.name:16},{item.score}\n")#ファイルに内容を書き込む
  print("出力ファイル名："+str(newfile))                      #出力ファイル名の出力

def quicksort(a:list, left:int,right:int):   #順序を入れ替えるクイックソート関数
    global looktime,swich                    #looktime（比較回数）,swich（入れ替え回数）をグローバル変数とする
    if left < right:                         #rightがleftより大きい時
        i, j = left, right                   #i=left,j=rightとする
        x = a[(left + right) // 2].score     #リストの中央にあるスコアの値をxに代入
        while True:                          #条件が正しい間
            while(a[i].score < x):           #i番目リストのスコアがリストの中央のスコアより小さい時（中央より左側について）
                looktime += 1                #比較回数を1回増やす
                i += 1                       #iをインクリメントすることで比較対象を次の値へとずらす（右にずらす）
            while(x < a[j].score):           #i番目リストのスコアがリストの中央のスコアより小さい時（中央より右側について）
                looktime += 1                #比較回数を1回増やす
                j -= 1                       #jを負にインクリメントすることで比較対象を次の値へとずらす（左にずらす）
            if (i <= j):                     #iの値がj以下になったら
                if i < j:                    #jの値がiの値よりも大きい時
                    swich += 1               #入れ替え回数の値を1回増やす
                    a[i], a[j] = a[j], a[i]  #リストのi番目のデータとj番目のデータを入れ替える
                i += 1                       #iの値を増やす
                j -= 1                       #jの値を減らす
            if i > j:                        #iの値がjの値よりも大きい時
                break                        # ループ終了
        if left < j:                         #最も左の値がjよりも小さい時
            quicksort(a, left, j)            #quicksort(a, left, j)関数の呼び出し
        if i < right:                        #最も左の値がiよりも大きい時
            quicksort(a , i, right)          #quicksort(a , i, right)関数の呼び出し
        return a                             # aに値を返す
item_list = []                               #item_listの初期値は空
csvreader('data_8.csv', item_list)           #入力ファイル
outout(item_list,"output_8.txt")             #出力ファイル
