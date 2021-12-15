def sort_lists(lists):
    res_lists = []
    for i in lists:
        for j in i:
            res_lists.append(j)    
    print(sorted(res_lists))

def sort_lists2(lists):
    res_lists = [j for i in lists for j in i]
    print(sorted(res_lists))

if __name__ == "__main__":    
    sort_lists(([1,4,5],[1,3,4],[2,6]))
    sort_lists2(([1,4,5],[1,3,4],[2,6]))