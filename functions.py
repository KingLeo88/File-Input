def words_per_line(fileLoc):
        try:
            file=open(fileLoc,'r')
            wordCount=0
            totalCount=0


            for lines in file:
                totalCount =totalCount + len(lines.split())
                wordCount = wordCount +1

            avg=totalCount/wordCount
            return avg

        except FileNotFoundError:
            print("Invalid file\n")
            return None

def count_punctuation(fileLoc):
    punc='?.!,'
    try:
        file=open(fileLoc,'r')
        puncCount=0
        for line in file:
            for a in line.strip():
                if a in punc:
                    puncCount = puncCount+1

        return puncCount

    except FileNotFoundError:
        print("Invalid file\n")
        return None

def output_string(fileLoc,fileStr,fileInt):
    try:
        fileInt=int(fileInt)
        file=open(fileLoc,'w')
        file.write((fileStr+'\n')*fileInt)
        file.close()
        return True
    except ValueError:
        print('Invalid input\n')
        return False

