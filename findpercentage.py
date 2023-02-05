if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


d={}
for x in student_marks:
    n=0
    for i in student_marks[x]:
        n+=i
    n=format(n/(len(student_marks[x])),".2f")
    student_marks[x]=n
    
print(student_marks[query_name])
