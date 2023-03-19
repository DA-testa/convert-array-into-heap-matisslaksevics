# Matiss Laksevics, IT, DITF, 4.grupa, 221RDB363

def sift_down(data, i, swaps):
    lc = 2 * i + 1
    if lc < len(data):
        rc = 2 * i + 2
        if rc < len(data) and data[rc] < data[lc]:
            lc = rc
        if data[lc] < data[i]:
            swaps.append((i, lc))
            data[i], data[lc] = data[lc], data[i]
            sift_down(data, lc, swaps)

def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def main():
    text = input()
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    if "F" in text:
        filename = input()
        filename = "tests/" + filename
        if 'a' not in filename:
            try:
                with open(filename, "r") as file:
                    n = int(input())
                    data = list(map(int, file.readline().split()))
                    assert len(data) == n
                    swaps = build_heap(data)
                    print(len(swaps))
                    for i, j in swaps:
                        print(i, j)
            except:
                return "File not found"

if __name__ == "__main__":
    main()