import streamlit as st
import re

# string_to_numlist = lambda x: [int(i) for i in re.split("[^0-9]", x) if i != ""]
#
#
# # Python3 program to solve fractional
# # Knapsack Problem
# class ItemValue:
#
#     # Item Value DataClass
#
#     def _init_(self, wt, val, ind):
#         self.wt = wt
#         self.val = val
#         self.ind = ind
#         self.cost = val // wt
#
#     def _lt_(self, other):
#         return self.cost < other.cost


# lcs() function to calculate length

def lcs_algo(S1, S2, m, n):
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Building the mtrix in bottom-up way
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index = L[m][n]

    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i - 1] == S2[j - 1]:
            lcs_algo[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Printing the sub sequences
    s = "".join(lcs_algo)
    st.success("LCS = " + s)
    st.success("LCS length = {}.".format(len(s)))


def LCS():
    st.title('Longest common subsequence')
    s1 = st.text_input("Please enter the first string")
    #   st.write(type(s1),s1)
    s2 = st.text_input("Please enter the second string")
    #   st.write(type(s2),s2)
    submit = st.button('Submit')
    if submit:
        m = len(s1)
        n = len(s2)
        lcs_algo(s1, s2, m, n)


# end of function LCS


# Driver Code
if __name__ == "__main__":
    st.header('Welcome in this program output calculator')
    st.write('Longest common subsequence')
    st.write('Here longest means that the subsequence should be the biggest one.'
            ' The common means that some of the characters are common between the two strings. '
            'The subsequence means that some of the characters are taken from the string that is '
            'written in increasing order to form a subsequence.'
            )
    LCS()

