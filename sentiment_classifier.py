
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(sentence):
    for char in punctuation_chars:
        sentence = sentence.replace(char,"")
    return sentence

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(sentence):
    sentence = strip_punctuation(sentence)
    words = sentence.strip().split(' ')
    count = 0
    for word in words:
        if word in positive_words:
            count +=1
    return count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentence):
    sentence = strip_punctuation(sentence)
    words = sentence.strip().split(' ')
    count = 0
    for word in words:
        if word in negative_words:
            count +=1
    return count

read_file = open("project_twitter_data.csv", "r")
write_file = open("resulting_data.csv", "w")
write_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
for line in read_file.readlines()[1:]:
    fields = line.strip().split(',')
    (text,retweets,replies) = (fields[0],fields[1], fields[2])
    write_file.write("{},{},{},{},{}\n".format(retweets,replies,get_pos(text),get_neg(text),get_pos(text)-get_neg(text)))
read_file.close()
write_file.close()