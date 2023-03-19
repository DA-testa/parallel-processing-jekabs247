# python3
#Jēkabs Kindzulis, 221RDC047, 18.gr

def parallel_processing(n, m, data):

    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    free_threads = list(range(n))
    rep = list(0 for i in range(n))
    timeCount = 0
    temp = 0

    for a in range (m):

        output.append(rep[temp])
        output.append(free_threads[temp])

        while any(data):
            data[a] = data[a] - 1
            rep[temp] = rep[temp] + 1

            if not data[a]:
                break
        
        calcul = (temp + 1) % n
        temp = calcul

        if not temp:
            timeCount = timeCount + 1

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count

    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    rez_l = len(result)

    for a in range(0, rez_l, 2):
        print(result[a+1], result[a])



if __name__ == "__main__":
    main()
