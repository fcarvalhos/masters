import os
import re
import sys

import re
import sys

def comment_remover(text):
    """ remove c-style comments.
        text: blob of text with comments (can include newlines)
        returns: text with comments removed
    """
    pattern = r"""
                            ##  --------- COMMENT ---------
           /\*              ##  Start of /* ... */ comment
           [^*]*\*+         ##  Non-* followed by 1-or-more *'s
           (                ##
             [^/*][^*]*\*+  ##
           )*               ##  0-or-more things which don't start with /
                            ##    but do end with '*'
           /                ##  End of /* ... */ comment
         |                  ##  -OR-  various things which aren't comments:
           (                ## 
                            ##  ------ " ... " STRING ------
             "              ##  Start of " ... " string
             (              ##
               \\.          ##  Escaped char
             |              ##  -OR-
               [^"\\]       ##  Non "\ characters
             )*             ##
             "              ##  End of " ... " string
           |                ##  -OR-
                            ##
                            ##  ------ ' ... ' STRING ------
             '              ##  Start of ' ... ' string
             (              ##
               \\.          ##  Escaped char
             |              ##  -OR-
               [^'\\]       ##  Non '\ characters
             )*             ##
             '              ##  End of ' ... ' string
           |                ##  -OR-
                            ##
                            ##  ------ ANYTHING ELSE -------
             .              ##  Anything other char
             [^/"'\\]*      ##  Chars which doesn't start a comment, string
           )                ##    or escape
    """
    regex = re.compile(pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
    noncomments = [m.group(2) for m in regex.finditer(text) if m.group(2)]

    return "".join(noncomments)


COMMENTS = re.compile(r'''
    (//[^\n]*(?:\n|$))    # Everything between // and the end of the line/file
    |                     # or
    (/\*.*?\*/)           # Everything between /* and */
''', re.VERBOSE)


def remove_commentsSimple(content):
    return COMMENTS.sub('\n', content)

'''
#linhas de teste das funcoes
filename = "C:\\Users\\Fernando\\Desktop\\10172_9871.c"
code_w_comments = open(filename).read()
code_wo_comments = remove_commentsSimple(code_w_comments)
code_wo_comments = comment_remover(code_wo_comments)
print(code_wo_comments)


filename = "C:\\Users\\Fernando\\Desktop\\10172_9871.c"
code_w_comments = open(filename).read()
code_wo_comments = comment_remover(code_w_comments)
print(code_wo_comments)
fh = open(filename+".nocomments", "w")
fh.write(code_wo_comments)
fh.close()

'''

'''
#versao do github, nao parece funcionar
def remove_comments(text):
    """Remove C-style /*comments*/ from a string."""

    p = r'/\*[^*]*\*+([^/*][^*]*\*+)*/|("(\\.|[^"\\])*"|\'(\\.|[^\'\\])*\'|.[^/"\'\\]*)'
    return ''.join(m.group(2) for m in re.finditer(p, text, re.M|re.S) if m.group(2))
'''



path = "mypath\\"

for root, dirs, files in os.walk(path):
    for name in files:
        fileOld = open(os.path.join(root, name), "r", encoding="utf-8", errors="ignore")
        filename = fileOld.read()
        fileOld.close()

        with open(os.path.join(root, name), "w", encoding="utf-8", errors="ignore") as f:
            code = comment_remover(filename)
            code = remove_commentsSimple(code)

            f.write(code)


#remove includes dos arquivos


path = "mypath\\"

for root, dirs, files in os.walk(path):
    for name in files:
        fileOld = open(os.path.join(root, name), "r", encoding="utf-8", errors="ignore")
        filename = fileOld.readlines()

        fileOld.close()
        with open(os.path.join(root, name), "w", encoding="utf-8", errors="ignore") as f:
            try:
                for lineR in filename:
                    if lineR.find("#include") == -1 and lineR.find("#define") == -1:
                        lineR = lineR.replace('bool ', 'int ')
                        #newLine = lineR.replace(lineR, "")
                        f.write(lineR)
            except:
                pass

