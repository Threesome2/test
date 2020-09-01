# given an integer list containing digits from [0,9], the task is to print all possible
# letter combinations that the numbers could represent. A mapping of digit to letters(just
# like on the telephone buttons) is being followed.Note that 0 and 1 do not map to any 
# letters.All the mapping are shown in the image below
try:
    import reduce
except:
    from functools import reduce

def get_mapper():
    '''
    Fixed mapping rules
    return a dict of map
    white list to avoid wrong input
    '''
    mapper = {
    '2':['A','B','C'],
    '3':['D','E','F'],
    '4':['G','H','I'],
    '5':['J','K','L'],
    '6':['M','N','O'],
    '7':['P','Q','R','S'],
    '8':['T','U','V'],
    '9':['W','X','Y','Z']
    }
    return mapper

def get_input():
    # test
    input_list = [1,2,3,4,5,6]
    # input_list = [] 
    # input_list = ['.','*',0,1,2]     
    return input_list

def lists_combination(lists,code=''):
    fn = lambda x, code=',': reduce(lambda x, y: [str(i)+code+str(j) for i in x for j in y], x)
    # fn(lists, code)
    return fn(lists, code)

def stage2():
    for i in range(0,100):
        main(i)

def main(i):
    mapper = get_mapper()
    if i == -1:
        input_list = get_input()
        print('Input:',input_list) 
    else:
        if len(str(i)) == 1:
            input_list = [i]
        else:
            input_list = []            
            print('Input:',i)
            for j in range(len(str(i))):
                num_part = str(i)
                input_list.append(num_part[j])
    input_list_clean = []
    for num in input_list:
        if str(num) in mapper:
            # print(num)
            input_list_clean.append(num)
    lists = []
    for num in input_list_clean:
        letters_list = mapper[str(num)]
        lists.append(letters_list)
    if len(lists) == 0:
        print('No output')
        return
    else:
        result = lists_combination(lists)
        str_result = ' '.join(result)
        print('Output:',str_result.lower())
        return

if __name__ == '__main__':
    main(-1)
    # if test stage2,just use stage2()
    # stage2()




