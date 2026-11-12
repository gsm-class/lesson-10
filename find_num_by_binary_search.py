# [iteration]
def search_num(n_list, target_n):
    start_idx = 0
    end_idx = len(n_list)-1
    
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2

        if target_n < n_list[mid_idx]:
            end_idx = mid_idx-1
        elif target_n > n_list[mid_idx]:
            start_idx = mid_idx+1
        else:
            return mid_idx
    
    return -1

# [recursion]
def search_num_recursion(n_list, target_n, start_idx, end_idx):
    if start_idx > end_idx:
        return -1
    
    mid_idx = (start_idx + end_idx) // 2

    # TODO: 여기에 코드를 작성하세요.

    return mid_idx

if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()

    m = int(input())
    for target_num in map(int, input().split()):
        # if search_num(num_list, target_num) >= 0:
        if search_num_recursion(num_list, target_num, 0, n-1) >= 0:
            print("1")
        else:
            print("0")