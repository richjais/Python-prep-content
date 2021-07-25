def balanceLoad(A):
    N = len(A)
    if N < 5 or N > 10 ** 5:  # check length, boundary check
        return False  # return false length of array not in range

    # check elements are in range, boundary check
    for x in A:
        if x < 1 or x > 10 ** 3:
            return False

    s = set(A)  # to check if all elements are same
    if len(s) == 1:
        return False

    start = 1  # drop element index from begin
    end = N - 2  # drop element index from end

    # if start equals end then balancing not possible
    while start < end:  # loop till "start not equals end" to check load balancing

        # load of 3 workers is equal load balancing possible
        if sum(A[:start]) == sum(A[start + 1:end - 1]) == sum(A[end:]):
            return True

        # all workers load not same:
        # 1st worker load less or equal than 3rd worker increase load
        if sum(A[:start]) <= sum(A[end + 1:]):
            start += 1
        else:  # 3rd worker load is less increase load for last worker
            end -= 1
    return False  # load balancing not possible