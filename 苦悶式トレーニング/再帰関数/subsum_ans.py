import copy
int_list = [1,2,4,9]
k = 7

def subsum(index,now_sum):
    #終了
    if index == len(int_list):
        return now_sum==k

    #indexにx番目の要素を足した場合
    #index+1なのは、次は指定indexの隣を見るから
    if subsum(index+1,now_sum+int_list[index]):
        return True

    #足さない場合
    if subsum(index+1,now_sum):
        return True

    return False

if subsum(0,0):
    print("YES")
else:
    print("NO")
