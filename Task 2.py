letters ="ЫбВЫуЯСдущДШНКАеЩЙФеРФО"
for i, item in enumerate(letters):
    if ord(item) in range(1040, 1072):
        letters =letters.replace(item, ' ')
print(letters)