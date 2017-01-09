def word_count(filename):
    open_file = open(filename)
    counted_words = {}
    for line in open_file:
        words = line.split()
        for word in words:
            counted_words[word] = counted_words.get(word, 0) + 1
    for word, number in counted_words.iteritems():
        print "%s: %s" % (word, number)
    open_file.close()
    return counted_words

word_count("twain.txt")
