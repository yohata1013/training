import copy
name_list = ['A','B','C']

def combi(index,working_list):
    #終了条件(1番最後まで要素を見たとき)
    if index == len(name_list):
        print(working_list)
        return

    # その値を入れた場合と入れなかった場合の分岐で再帰関数を呼び出す
    # 現時点でのindexにあたる要素を入れた場合
    # copyを取らないと、同じものを永遠にかけてしまうため、片方を動かすためにコピーする
    cp =copy.copy(working_list)
    cp.append(name_list[index])
    combi(index+1,cp)

    # 現時点でのindexにあたる要素を入れなかった場合
    combi(index+1,working_list)

combi(0,[])
