'''
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
If you want to know more http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
More similar exercise are found here http://rosalind.info/problems/list-view/ (source)
DNA_strand ("ATTGC") # return "TAACG"
DNA_strand ("GTAT") # return "CATA"
脱氧核糖核酸（DNA）是一种在细胞核中发现的化学物质，带有生物体发育和功能的“指令”。
在DNA字符串中，符号“ A”和“ T”相互补充，如“ C”和“ G”。 您可以对DNA的一侧（字符串，Haskell除外）起作用。 您需要获得另一互补的一面.
 DNA链永远不会为空或根本没有DNA（同样，Haskell除外）。
DNA_strand（“ ATTGC”）＃返回“ TAACG”
DNA_strand（“ GTAT”）＃返回“ CATA”
'''
#自己写的
def DNA_strand(dna):
    alist = list(dna)
    blist = []
    # print(alist)
    for i in alist:
        if i == 'A':
            blist.append('T')
        elif i == 'T':
            blist.append('A')
        elif i == 'G':
            blist.append('C')
        elif i == 'C':
            blist.append('G')
    print(''.join(blist))
DNA_strand('CATA')

#高赞答案
# def DNA_strand(dna):
#     return dna.translate(string.maketrans('ATGC','TACG'))
# print(DNA_strand('CATA'))

# def DNA_strand(dna):
#     # code here
#     my = {
#             "A" : "T",
#             "T" : "A",
#             "C" : "G",
#             "G" : "C",
#             }
#     print("".join(my[i] for i in dna)) 
# DNA_strand('GTAT')
