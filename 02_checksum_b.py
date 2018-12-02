import itertools

list_words = []

def compare(str1, str2):
    # print(str1 == str2)
    if str1 != str2:
        # print("{} and {}".format(str1, str2))
        zipped = zip(str1, str2)
        x = []
        for i,j in zipped:
            if i==j:
                x.append(j) 
        return x
    else:
        return [1]

if __name__ == "__main__":
    with open('data_02.txt', 'r') as file:
        data = file.read().splitlines()
        # for box in data:
        comparaison_number = 0
        print("Word length: {}".format(len(data[0])))
        for i in range(len(data)):
            for j in range(len(data)):
                comparaison_number+=1
                result = compare(data[i],data[j])
                if len(result) > 24:
                    print("\n*********\nComparaison #{}:".format(comparaison_number))
                    print("{} and {}".format(data[i], data[j]))
                    print("\n{}".format(result))
                    print("\nLength = {}".format(len(result)))
                    print("Result is: {}".format(''.join(result)))