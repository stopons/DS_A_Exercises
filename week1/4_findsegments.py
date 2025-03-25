def find_segments(data):

    segments = []
    counter = 1

    # Create a for loop to iterate through "data" str, incrementing "counter" each time the
    # character is the same as the previous one (or None in case of the first character).
    # When the character is different, we'll append everything accumulated so far and reset
    # the count for the new character.

    for i in range(1, len(data)):
        # No need to initialise a list to convert then in tuple because i can append
        # the list directly with "segments.append((counter, data[-1]))" at the end

        if data[i] == data[i-1]:
            counter += 1
        else:
            segments.append((counter, data[i-1]))
            counter = 1 #Reset the counter for the upcoming "different" character

    # For the last character in the list
    segments.append((counter, data[-1]))

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