def word_count(filename):
    open_file = open(filename)
    # for line in open_file:
    #     words = line.split()
    #     print words
    counted_words = {}
    for line in open_file:
        words = line.split()
        for word in words:
            counted_words[word] = counted_words.get(word, 0) + 1
    # print "%s: %d" % (word, counted_words)
    return counted_words


print word_count("test.txt")