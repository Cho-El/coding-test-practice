import heapq

# def solution(book_time):
#     answer = 1
    
#     # "HH:MM" → HH * 60 + MM
#     book_time_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
#     book_time_ref.sort()
    
#     heap = []
#     for s, e in book_time_ref:
#         if not heap:
#             heappush(heap,e)
#             continue
#         if heap[0] <= s:
#             heappop(heap)
#         else:
#             answer += 1
#         heappush(heap,e+10)
    
#     return answer

def solution(book_time):
    bookTimeMinute = []
    answer = 1
    for start, end in book_time:
        temp = []
        hour, minute = map(int,start.split(":"))
        temp.append(hour * 60 + minute)
        hour, minute = map(int,end.split(":"))
        temp.append(hour * 60 + minute)
        bookTimeMinute.append(temp)
    
    bookTimeMinute.sort()
    q = []
    for start, end in bookTimeMinute:
        if not q:
            heapq.heappush(q,end + 10)
            continue
        elif q[0] <= start:
            heapq.heappop(q)
        else:
            answer += 1
        heapq.heappush(q, end + 10)
    return answer
        
print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))