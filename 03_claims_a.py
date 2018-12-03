import collections

with open('data_03.txt', 'r') as data:
    width_max=0
    height_max=0
    canvas = [['..' for x in range(1000)] for row in range(1000)]
    shared_areas = 0

    for claim in data:
        claim = claim.split(' ')
        dimensions = claim[3].split('x')
        position = claim[2].split(',')
        width = int(dimensions[0])
        height = int(dimensions[1])
        pos_x = int(position[0])
        pos_y = int(position[1].split(':')[0])
        max_x = pos_x + width
        max_y = pos_y + height
        if max_x > width_max: width_max = max_x
        if max_y > height_max: height_max = max_y
        print("Claim {}".format(claim[0]))
        # print("Claim {}:\n---------\nPosition:{}x{}\nSize: {}x{}\nWidth max:{}\nHeight max:{}".format(
        #     claim[0],pos_x, pos_y, width, height, width_max, height_max))
        
        for x in range(1000):
            for y in range(1000):
                if (pos_x <= x < max_x) and (pos_y <= y < max_y): 
                    if canvas[y][x] == '..':
                        canvas[y][x] = claim[0]
                    else: 
                        canvas[y][x] = 'XX'
                        touched = True

    for row in canvas:
        print(row)

    print("Result: {}".format(sum(row.count('XX') for row in canvas)))
   
with open('data_03.txt', 'r') as data:
    for claim in data:
        claim = claim.split(' ')
        dimensions = claim[3].split('x')
        position = claim[2].split(',')
        width = int(dimensions[0])
        height = int(dimensions[1])
        area = sum(row.count(claim[0]) for row in canvas)
        if area == width * height:
            print("Claim {} untouched!".format(claim[0]))
            break