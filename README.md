# twentyletters-solver
this isn't really fun anymore

## what

python script to solve the [twentyletters.com](https://twentyletters.com) puzzles. it's not optimized at all, but considering how fast it already is, there is no point to revise it too much. the performance increase would be so marginal.

## how use

1. download the repository.
2. run `main.py`.
3. the solution will be outputed, in addition to the run time and attempt count.

## how it work

1. get the scrabble dictionary the game is based on and the points for the individual letters.
2. get the letters and best possible score of the day from the website (using beautiful soup HTML parsing).
3. sort the words list from the longest to shortest words. the highest scores are the longest words, so it will be faster to start at the longer words.
4. iterate through the word list, choosing the first word that fits today's letters.
5. remove all the taken letters that this word uses so the next word(s) won't repeat letters.
6. continue through the word list and repeating the process of choosing words that fit the letters and removing those letters from our letter list.
7. calculate the score of the combination of words we chose. if the score doesn't match the highest possible score of the day, retry.
8. repeat until the combination is found.
