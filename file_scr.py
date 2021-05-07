import csv


list_url = ["Top Gun","Risky Business","Minority Report"]

def file_scr(kug, fil, ty, list_url, ent_file, ent_path):
    path_file_txt = ent_path + "/" + ent_file + ".txt"
    path_file_csv = ent_path + "/" + ent_file + ".csv"

    # エラーも出る可能性あるのでトライエラー処理
    try:
        # ファイル形式「csv」選択時
        if fil == "0":
            with open(path_file_csv,"a",newline="") as csvfile:
                if ty == "1":
                    if kug == "0":
                        csvwrite = csv.writer(csvfile,delimiter=",")
                        csvwrite.writerow(list_url)
                    elif kug == "1":
                        csvwrite = csv.writer(csvfile,delimiter="\t")
                        csvwrite.writerow(list_url)
                elif ty == "0":
                    csvwrite.writerow(csvfile,delimiter="\n")



        # ファイル形式「txt」選択時
        elif fil == "1":
            with open(path_file_txt, "a",encoding="utf-8") as f:
    
                # スクレイピングデータ（list_url）をまわす
                for i,element in enumerate(list_url):

                    # 最後のリストでなければ区切りと縦横処理
                    if(i+1 < len(list_url)):

                        # カンマ区切り縦横
                        if fil == "0":
                            # 縦横判別
                            if ty == "0":
                                f.write(element + "," + "\n")
                            elif ty == "1":
                                f.write(element + ",")

                        # タブ区切り縦横
                        elif fil == "1":
                            # 縦横判別
                            if ty == "0":
                                f.write(element + "\t" + "\n")
                            elif ty == "1":
                                f.write(element + "\t")
                    else:
                        f.write(element)
        return True
    except:
        return False


            
