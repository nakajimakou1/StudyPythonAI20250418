
def replace_spchar(search_filename_path) :

    # 特殊文字回避処理
    chk_file_search_path = search_filename_path.replace("〜","～")
    chk_file_search_path = chk_file_search_path.replace("～","?")
    chk_file_search_path = chk_file_search_path.replace("：","?")

    # https://note.nkmk.me/python-glob-usage/　  # 正規表現回避
    chk_file_search_path = chk_file_search_path.replace("[","?")  # 正規表現回避
    chk_file_search_path = chk_file_search_path.replace("]","?")  # 正規表現回避

    return chk_file_search_path
