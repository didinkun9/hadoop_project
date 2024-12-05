import sys

current_word = None
current_count = 0

for line in sys.stdin:
    word, count = line.strip().split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# Print the last word
if current_word:
    print('%s\t%s' % (current_word, current_count))