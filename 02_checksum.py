import collections


with open('data_02.txt', 'r') as data:
    twos=0
    threes=0
    checksum=0
    for box in data:
        has_two=False
        has_three=False
        print("Word: {}".format(box))
        d = collections.defaultdict(int)
        for c in box:
            d[c]+=1
        for c in sorted(d, key=d.get, reverse=True):
            if d[c] >= 2 and d[c]<=3:
                print("{} {}".format(c, d[c]))
            if d[c]==2:
                has_two=True
            if d[c]==3:
                has_three=True
        if has_two: twos+=1
        if has_three: threes+=1
    print("Twos: {}".format(twos))
    print("Threes: {}".format(threes))
    checksum = twos * threes
    print("Checksum: {}".format(checksum))

        