# python3
#Jēkabs Kindzulis, 221RDC047, 18.gr

import heapq

def parallel_processing(n, m, data):

    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    free_threads = list(range(n))
    heapq.heapify(free_threads)

    #heap trackos kurs ir nakamais job
    next_job = [(0, i) for i in range(m)]
    heapq.heapify(next_job)

    while next_job:
        time, job_index = heapq.heappop(next_job)

        thread_index = heapq.heappop(free_threads)

        start_time = max(time, output[thread_index][1] if output else 0)

        output.append((thread_index, start_time))

        heapq.heappush(free_threads, thread_index)

        heapq.heappush(next_job, (time + data[job_index], job_index))

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

    for a, b in result:
        print(a, b)



if __name__ == "__main__":
    main()
