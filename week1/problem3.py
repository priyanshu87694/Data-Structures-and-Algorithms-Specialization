
def get_input():
    S, n = map(int, input().split())
    requests = []
    for _ in range(n):
        a, p = map(int, input().split())
        requests.append((a, p))

    return S, requests

def main(S, requests):
    now = 0
    response = []
    last_a = requests[0][0]
    last_p = requests[0][1]

    for req in requests:
        a_time, p_time = req

        if a_time == last_a:
            if S >= (now+p_time):
                now += p_time
                response.append(a_time)
            else:
                response.append(-1)
            last_a = a_time
            last_p = p_time
        else:
            now -= last_p
            if S >= (now+p_time):
                now += p_time
                response.append(a_time)
            last_a = a_time
            last_p = p_time

    return response


if __name__ == "__main__":
    S, requests = get_input()
    response = main(S, requests)
    
    for res in response:
        print(res)
