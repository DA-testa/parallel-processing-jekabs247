# python3
#Jēkabs Kindzulis, 221RDC047, 18.gr

def parallel_processing(n, m, data):

    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    free_threads = list(range(n))
    next_job = [(0, i) for i in range(m)]

    while next_job:

        time, job_index = next_job[0]

        thread_index = free_threads[0]

        start_time = 0
        if output and thread_index < len(output):
            start_time = max(time, output[thread_index][1])

        output.append((thread_index, start_time))

        free_threads = free_threads[1:]
        next_job = next_job[1:]

        if len(next_job) < n and next_job:
            next_job.sort()

        free_threads.append(thread_index)

        next_job.append((time + data[job_index], job_index))
        next_job.sort() 

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

    for thread_index, start_time in result:
        print(thread_index, start_time)



if __name__ == "__main__":
    main()
