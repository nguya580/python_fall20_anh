# News Search Engine by Anh Nguyen

Disclaimer: due to the limitation of my free account on the [newsapi](https://newsapi.org/), users can only search for articles **100 times per day.**

Check the file "noFunction_version.ipynb" for part 3, which is plain code without functions,

Check the file "final_withFunction_version.ipynb" for part 4, which contains functions.

## References:
For this project, I have guidances from:

    - [Ajinkya Sonawane](https://medium.com/daily-python/python-script-to-search-for-news-based-on-keywords-daily-python-5-509348bd190e)

    - [Corey Schafer](https://www.youtube.com/watch?v=ng2o98k983k&list=PLVW1_dn6ebDzRE6e_ezvt9qnJ3uRJPNI9&index=5&ab_channel=CoreySchafer)

    - [The News API documentation](https://newsapi.org/docs/client-libraries/python)

Visit [link](https://www.notion.so/Python-Assignment-1-60745b9ea7744e8193b10b208411d76b) to read about the project description.

## Pseudocode:
1. Ask input for keywords the user wants to search.
2. From the input variable (string), use it to look for articles:
    - Headline
    - URL link
    - Published date
    - Article summary
3. Organize outputs into variables to arrange it into rows within a csv file.
4. Use csv library to save as a CSV file.
