import re

def fullJustify_2(str_arr, linelength):

    arr = str.split(str_arr)

        # helper function for filling in spaces
    def fill_in(s, linelength):
        diff = linelength - len(s)
        separater = ' '
        #  count how many parts/words are in the line
        parts = s.count(separater)
    
        if parts > 0:
            multiplier = diff #  parts + 1
            #  if the diff is too big, we need to evenly add the spaces, so replace each space with a multipler * space.
        if multiplier > 1:
            s = s.replace(separater, separater * multiplier)
            #  new separater is the group of spaces now.
        separater = separater * multiplier
        #  the remainder is now the mod
        diff = diff % parts

        while diff and " " in s:
            #  add each group of spaces with a space, for diff times.
            s = s.replace(separater, separater + ' ', diff)
            diff = linelength - len(s)


        if len(s) < linelength:
            s = s + diff * " "

        return s
    
    
    #  main function starts here
    ret = []
    #  sanity check
    if len(arr) == 0:
        return ret
    
    curr_length = 0
    #  out is the temp store to save the current line.
    out = ''
    
    
    #  go over each word
    for i in arr:
    
        # temp counter, if 0, means first word for that line.
        if curr_length == 0:
            if len(i) <= linelength:
                #  set the temp to current word, increment curr_length
                out = i
                curr_length = curr_length + len(i)
    else:
        #  calculate the new length by checking the length of the next word.
        new_len = curr_length + len(i) + 1
        if new_len <= linelength:
            curr_length = curr_length + len(i) + 1
            out = out + ' ' + i
        else:
            #  line reached max, now process the space filler and add to output.
            ret.append(fill_in(out, linelength))
        #  reset the temp variables for next line
            out = i
            curr_length = len(i)
    
    if out:
        #last line
        diff  = linelength - len(out)
        ret.append(out + " " * diff)
    
    return ret



def fullJustify(str_line, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    words = str.split(str_line)
    length=0
    line=[]
    ans=[]
    for word in words:
        wlen=len(word)
        if length and length+wlen+1>maxWidth: # to flush current line (single word  length<=maxWidth)
            # 1. flush this line
            nw=len(line) # number of words
            total=maxWidth-(length-(nw-1)) # total spaces
            if nw==1: # only one word
                ans.append(line[0]+(' '*total))
            else:
                base,res= divmod(total,nw-1) # base number of spaces, extra spaces
                for i in range(res):
                    line[i]+=' '
                ans.append((' '*base).join(line))
            # 2. reset & start next line
            length=wlen
            line=[word]
        else:
            if line:
                length+=1+wlen
            else:
                length+=wlen
            line.append(word)
    # 3. last line
    if line:
        ans.append(' '.join(line)+' '*(maxWidth-length))
    return ans






lead_re = re.compile(r'(^\s+)(.*)$')


def justify_str(line, length):
    words = str.split(line)

    current_length = 0
    current_line = []
    values = []

    for word in words:
        word_length = len(word)
        if current_length and current_length+word_length+1 > length:
            number_of_words = len(current_line)
            total = length - (current_length - (number_of_words - 1))
            if number_of_words == 1:
                values.append(line[0] + (' ' * total))
            else:
                base, res = divmod(total, number_of_words-1)
                for i in range(res):
                    current_line[i] += ' '
                values.append((' ' * base).join(current_line))

            current_length = word_length
            current_line = [word]
        else:
            if current_line:
                current_length += (1 + word_length)
            else:
                current_length += word_length
            current_line.append(word)
    if current_line:
        values.append(' '.join(current_line) + ' ' * (length - current_length))
    return values

def items_len(l):
    return sum([ len(x) for x in l] )


def align_string(s, width):
    '''
    align string to specified width
    '''
    # detect and save leading whitespace
    #m = re.compile(r'(^\s+)(.*)$').match(s)
    #if m is None:
    #    left, right, w = '', s, width
    #else:
    #    left, right, w = m.group(1), m.group(2), width - len(m.group(1))
    left, right, w = '', s, width
    items = right.split()

    # add required space to each words, exclude last item
    for i in range(len(items) - 1):
        items[i] += ' '


    # number of spaces to add
    left_count = w - sum([ len(x) for x in items] )
    while left_count > 0 and len(items) > 1:
        for i in range(len(items) - 1):
            items[i] += ' '
            left_count -= 1
            if left_count < 1:
                break

    res = left + ''.join(items)
    return res







if __name__ == '__main__':

    results = align_string("The quick brown fox jumps over the lazy dog.", 100)
    print(results)