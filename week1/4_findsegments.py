def find_segments(data):

    segments = []
    
    data_list = list(data)
    counter = 1

    # Create a for loop to iterate through "data_list", incrementing "counter" each time the
    # character is the same as the previous one (or None in case of the first character).
    # When the character is different, we'll append everything accumulated so far and reset
    # the count for the new character.

    for i in range(1, len(data_list)):
        # Initialize the list at the beginning of the for loop to be able to use ".append",
        # and then convert it into a tuple.
        segment_item = [] 

        if data_list[i] == data_list[i-1]:
            counter += 1
        else:
            segment_item.append(counter)
            segment_item.append(data_list[i-1])
            segment_item = tuple(segment_item)
            segments.append(segment_item)
            counter = 1 #Reset the counter at the end

    # For the last character in the list
    segment_item = [counter, data_list[-1]]  
    segment_item = tuple(segment_item)
    segments.append(segment_item)


    return segments





if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]