import os,sys
import tkinter as tk

# from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk

import scraiping

import file_scr


# load_url = "https://news.goo.ne.jp/"

""" 
やることリスト
スクレイピング説明文（違法性、大分類と小分類の意味、検証の内容確認)

"""



def gui_crate():

    root = tk.Tk()
    root.title("WEBスクレイピングツール")
    root.geometry("768x1024")



    """ 
    --------------------
    ボタンイベント関数
    --------------------
    """

    # 「表示確認」ボタンクリックのイベント
    def btn_kakunin():




        Messagebox = tk.messagebox.askquestion('表示確認','スクレイピング内容を表示してもよろしいでしょうでしょうか？')
        if Messagebox == 'yes': #If関数
            # テキストウィジェット表示
            root_text = tk.Tk()
            root_text.geometry("500x300")
            root_text.title('Webスクレイピングデータ内容')
            scr_text = tk.scrolledtext.ScrolledText(root_text)
            scr_text.pack()

            # スクレイピングする
            dp_dai = drop_list_dai.get()
            dp_sho = drop_list_sho.get()
            tb_dp_dai = textBox_drop_dai.get()
            tb_dp_sho = textBox_drop_sho.get()

            scr_dict = {"dai_list":dp_dai,"dai_text":tb_dp_dai,
                        "sho_list":dp_sho,"sho_text":tb_dp_sho}


            scr = scraiping.URL_SCR()
            scr.url_scraipe(textBox_url.get(),scr_dict)
            i = 0
            for element in scr.element_list:
                scr_text.insert(float(i),element + "\n")
                i+=1
            root_text.mainloop()
        else:
            tk.messagebox.showinfo('戻る','アプリケーション画面に戻ります')

    # ファイル参照画面
    def btn_dialog():
        iDir = os.path.abspath(os.path.dirname(__file__))
        iDirPath = filedialog.askdirectory(initialdir = iDir)
        textBox_path.delete(0, tk.END)
        textBox_path.insert(tk.END,iDirPath)

    # 「実行」ボタンクリックのイベント
    def btn_jikko():
        rb_kug = flg_kugiri.get()
        rb_fil = flg_file.get()
        rb_ty = flg_ty.get()
        enty_file = textBox_file.get()
        enty_path = textBox_path.get()

        Messagebox = tk.messagebox.askquestion('ファイルの書き込み実行確認','ファイルの書き込みを実行してもよろしいでしょうか？')
        if Messagebox == 'yes': #If関数
            # スクレイピング実行
            scr_jikko = scraiping.URL_SCR()
            scr_jikko.url_scraipe(textBox_url.get())
            lis_jikko = scr_jikko.element_list

            
            file_SCR = file_scr.file_scr(rb_kug, rb_fil, rb_ty, lis_jikko, enty_file, enty_path)
            print(file_SCR)
            if file_SCR == True:
                tk.messagebox.showinfo('ファイルの書き込み完了','ファイルの書き込みが完了しました')
            elif file_SCR == False:
                tk.messagebox.showerror('ファイル書き込みエラー','ファイルの書き込みエラーがでました\nもう一度入力内容を確認して実行して下さい')
        else:
            tk.messagebox.showinfo('戻る','アプリケーション画面に戻ります')

    # 「閉じる」ボタンのイベント
    def btn_exit():
        Messagebox = tk.messagebox.askyesno('終了確認','画面を閉じてもよろしいでしょうか？')
        if Messagebox:
            tk.messagebox.showinfo('終了画面','アプリケーションを終了します')
            root.destroy()
        else:
            tk.messagebox.showinfo('戻る','アプリケーション画面に戻ります')




    """ 
    ---------------------
    WEbサイト設定フレーム
    ---------------------
     """


    # タイトルラベル
    LabelTitle = tk.Label(text="WEBスクレイピングツール",font=("MSゴシック", "20", "bold"))
    LabelTitle.pack(anchor=tk.NW,padx=32,pady=30)

    # WEBサイトフレーム
    frame_site = tk.LabelFrame(
        root,
        borderwidth=1,
        relief="groove",
        text="WEBサイト設定",
        font=("MSゴシック", "12", "bold")
    )
    frame_site.pack(anchor=tk.W,padx=52, pady=(20,0))

    # サイトURL
    Label_url = tk.Label(frame_site,text="サイトURL:",font=("MSゴシック", "12", "bold"))
    textBox_url = tk.Entry(frame_site,width=80)
    textBox_url.insert(0,"https://news.goo.ne.jp/")

    Label_url.pack(anchor=tk.W,padx=25,pady=(15,0))
    textBox_url.pack(anchor=tk.W,padx=52)

    # 大分類フレーム
    frame_dai = tk.LabelFrame(
        frame_site,
        borderwidth=1,
        relief="groove",
        text="大分類",
        font=("MSゴシック", "12", "bold")
        )
    frame_dai.pack(anchor=tk.W,padx=25,pady=(10,0))
    # 小分類フレーム
    frame_sho = tk.LabelFrame(
        frame_site,
        borderwidth=1,
        relief="groove",
        text="小分類",
        font=("MSゴシック", "12", "bold")
        )
    frame_sho.pack(anchor=tk.W,padx=25,pady=10)
            
    # htmlリスト
    html_list = ["href","id","class_","a"]

    #グループA用変数
    flg_htmlA = tk.StringVar()
    
    #グループB用変数
    flg_htmlB = tk.StringVar()
    
    #グループB用変数
    flg_ty = tk.StringVar()
    flg_ty.set('0')

    # ドロップダウンリスト
    drop_list_dai = ttk.Combobox(frame_dai,textvariable=flg_htmlA,values=html_list)
    drop_list_dai.current(2)
    drop_list_sho = ttk.Combobox(frame_sho,textvariable=flg_htmlB,values=html_list)
    drop_list_sho.current(2)

    Label_drop_dai = tk.Label(frame_dai,text="タグ種類：",font=("MSゴシック", "12", "bold"))
    textBox_drop_dai = tk.Entry(frame_dai)
    textBox_drop_dai.insert(0,"gn-news-list")
    Label_tag_dai = tk.Label(frame_dai,text="タグ名：",font=("MSゴシック", "12", "bold"))

    Label_drop_sho = tk.Label(frame_sho,text="タグ種類：",font=("MSゴシック", "12", "bold"))
    textBox_drop_sho = tk.Entry(frame_sho)
    textBox_drop_sho.insert(0,"list-title-topics")
    Label_tag_sho = tk.Label(frame_sho,text="タグ名：",font=("MSゴシック", "12", "bold"))

    # サイトを配置
    Label_drop_dai.pack(side="left",pady=(15,0))
    drop_list_dai.pack(side="left")
    Label_tag_dai.pack(side="left",padx=(50,0))
    textBox_drop_dai.pack(side="left",padx=10)

    Label_drop_sho.pack(side="left",pady=(15,0))
    drop_list_sho.pack(side="left")
    Label_tag_sho.pack(side="left",padx=(50,0))
    textBox_drop_sho.pack(side="left",padx=10)


   # 実行ボタン
    Button_kakunin = tk.Button(text="表示確認",width=10,command=btn_kakunin)
    Button_kakunin.pack(pady=10)




    """ 
    ------------------------
    保存内容設定フレーム
    ------------------------
    """


    # ファイル読み込みフレーム
    frame1 = tk.LabelFrame(
        root,
        borderwidth=1,
        relief="groove",
        text="保存内容設定",
        font=("MSゴシック", "12", "bold")
    )
    frame1.pack(anchor=tk.W,padx=52, pady=(30,0))
    # ファイル名
    Label_file = tk.Label(frame1,text="ファイル名:",font=("MSゴシック", "12", "bold"))
    Label_file.pack(anchor=tk.W,pady=(15,0),padx=25)
    textBox_file = tk.Entry(frame1,width=80)
    textBox_file.pack()
    # 保存先
    Label_path = tk.Label(frame1,text="保存先:",font=("MSゴシック", "12", "bold"))
    Label_path.pack(anchor=tk.W,padx=25)
    textBox_path = tk.Entry(frame1,width=80)
    textBox_path.pack()
    Button_path = tk.Button(frame1,text="保存先参照",command=btn_dialog)
    Button_path.pack(anchor=tk.W,padx=52)
    # 保存形式
    """ Label2_3 = tk.Label(frame1,text="保存形式")
    Label2_3.pack(anchor=tk.W,pady=(15,0)) """



    #グループA用変数
    flg_kugiri = tk.StringVar()
    flg_kugiri.set('0')
    #グループB用変数
    flg_file = tk.StringVar()
    flg_file.set('0')
    #グループB用変数
    flg_ty = tk.StringVar()
    flg_ty.set('0')

    # 区切りラジオボタンフレーム
    frame_kugiri = tk.LabelFrame(
        frame1,
        borderwidth=1,
        relief="groove",
        text="区切り",
        font=("MSゴシック", "12", "bold")
    )
    frame_kugiri.pack(side="left",anchor=tk.W,pady=10,padx=60)
    Radio_kugiri1 = tk.Radiobutton(frame_kugiri,text="カンマ区切り", value=0, variable=flg_kugiri)
    Radio_kugiri2 = tk.Radiobutton(frame_kugiri,text="タブ区切り", value=1, variable=flg_kugiri)
    Radio_kugiri1.pack()
    Radio_kugiri2.pack()

    # file形式ラジオボタンフレーム
    frame_file = tk.LabelFrame(
        frame1,
        borderwidth=1,
        relief="groove",
        text="保存形式",
        font=("MSゴシック", "12", "bold")
    )
    frame_file.pack(side="left",anchor=tk.W,pady=10,padx=60)
    Radio_file1 = tk.Radiobutton(frame_file,text="csv", value=0, variable=flg_file)
    Radio_file2 = tk.Radiobutton(frame_file,text="text", value=1, variable=flg_file)
    Radio_file1.pack()
    Radio_file2.pack()

    # 縦横ボタンフレーム
    frame_ty = tk.LabelFrame(
        frame1,
        borderwidth=1,
        relief="groove",
        text="縦/横並び",  
        font=("MSゴシック", "12", "bold")
    )
    frame_ty.pack(side="left",anchor=tk.W,pady=10,padx=60)
    Radio_ty1 = tk.Radiobutton(frame_ty,text="縦並び", value=0, variable=flg_ty)
    Radio_ty2 = tk.Radiobutton(frame_ty,text="横並び", value=1, variable=flg_ty)
    Radio_ty1.pack()
    Radio_ty2.pack()



    """ 
    ---------------------
    実行ボタンフレーム
    ---------------------
    """


    # 実行ボタンフレーム
    frame_jikko = tk.Frame()
    frame_jikko.pack(pady=10)

    # 実行ボタン
    Button_jikko = tk.Button(frame_jikko,text="実　行",width=10,command=btn_jikko)
    Button_jikko.pack(side="left")

    # 閉じるボタン
    Button_exit = tk.Button(frame_jikko,text="閉じる",width=10,command=btn_exit)
    Button_exit.pack(side="left",padx=50)



    root.mainloop()


gui_crate()
