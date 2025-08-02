def leftMostrepeat(str):
    visited={}
    for i,ch in enumerate(str):
        if ch in visited:
            return visited[ch]
        else:
            visited[ch]=i
    return -1


text="necessary"
print(leftMostrepeat(text))