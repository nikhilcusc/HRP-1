## NOTES:
1. A pattern can have multiple starts and ends :
    >^A.*$|^.*B$

1. Any character followed by not a character. using negetive lookahead.
    > \w(?!\w)

1. Greedy (.*) vs non-greedy (.*?) matches. 
    > Greedy will match everything in between. <a><b>somthing</a></b>
    > Compared to non greedy match. <a>