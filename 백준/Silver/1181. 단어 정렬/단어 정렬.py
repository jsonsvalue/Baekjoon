n = int(input())
words = []

for i in range(n):
    txt = input()
    words.append(txt)

words = set(words)
words = list(words)

#알파벳 순서대로 정렬
words.sort()

#알파벳 길이대로 정렬
words.sort(key = len)
print(*words, sep = "\n")


