import heapq


def solution(jobs):
    jobs.sort(key=lambda x: x[0])  # 요청 시간 기준으로 정렬
    n = len(jobs)
    current_time = 0
    total_waiting_time = 0
    heap = []
    job_index = 0
    completed_jobs = 0

    while completed_jobs < n:
        while job_index < n and jobs[job_index][0] <= current_time:
            duration, start = jobs[job_index]
            heapq.heappush(heap, (duration, start))
            job_index += 1
        if heap:
            duration, start = heapq.heappop(heap)
            current_time += duration


    return


if __name__ == "__main__":
    jobs =[[0, 3], [1, 9], [2, 6]]
    answer = 9
    solution(jobs)