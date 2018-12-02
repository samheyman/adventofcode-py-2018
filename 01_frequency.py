frequency_shift = 0
list_of_frequencies = []
i=0

for loop in range (200):
    with open('data_01.txt', 'r') as data:
        for shift in data:
            frequency_shift+=int(shift)
            if (frequency_shift in list_of_frequencies) and (frequency_shift > 587):
                print("Frequency {} already detected!".format(frequency_shift))
                break
            else:
                list_of_frequencies.append(frequency_shift)
            #print("Adding {}. Total is now {}".format(shift, frequency_shift))
    print("Loop #{}".format(loop+2))
