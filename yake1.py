# # import yake
# # print("________________________________________")
# # text="""It is a lightweight, unsupervised automatic keyword extraction method that relies on statistical text features extracted 
# # from individual documents to identify the most relevant keywords in the text. This system does not need to be trained on a 
# # particular set of documents, nor does it depend on dictionaries, text size, domain, or language. Yake defines a set of five 
# # features capturing keyword characteristics which are heuristically combined to assign a single score to every keyword. The lower 
# # the score, the more significant the keyword will be. You can read more about it here. Python package for yake."""
# # kw_extractor = yake.KeywordExtractor(top=10, stopwords=None)
# # keywords = kw_extractor.extract_keywords(text)
# # for kw, v in keywords:
# #   print("Keyphrase: ",kw, ": score", v)

# # # from yake import KeywordExtractor



# import pke
# from nltk.corpus import stopwords

# # taken from the Wikipedia page of Python
# text = """
# Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
# Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
# Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.
# Python consistently ranks as one of the most popular programming languages.
# Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL, capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life", a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a five-member "Steering Council" to lead the project.
# Python 2.0 was released on 16 October 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode.
# Python 3.0 was released on 3 December 2008. It was a major revision of the language that is not completely backward-compatible. Many of its major features were backported to Python 2.6.x and 2.7.x version series. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.
# Python 2.7's end-of-life date was initially set at 2015 then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3. No more security patches or other improvements will be released for it. With Python 2's end-of-life, only Python 3.6.x and later are supported.
# Python 3.9.2 and 3.8.8 were expedited as all versions of Python (including 2.7) had security issues, leading to possible remote code execution and web cache poisoning.
# """

 
# extractor = pke.unsupervised.YAKE()
 
# extractor.load_document(input=text,language='en',normalization=None)


 
# stoplist = stopwords.words('english')
# extractor.candidate_selection(n=3)

 
# window = 2
# use_stems = False # use stems instead of words for weighting
# extractor.candidate_weighting(window=window,use_stems=use_stems)

 
# threshold = 0.8
# keyphrases = extractor.get_n_best(n=3, threshold=threshold)

# print(keyphrases)

# with open(r'C:\Users\Kishor Kore\Desktop\learning-python-5th-edition_.PDF',encoding='utf-8' ) as f:
#     print(f.read())
try:
    import numpy
    import pandas as pd
    import pickle as pk
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import re
    from nltk.stem.snowball import SnowballStemmer
    import nltk
    stemmer = SnowballStemmer("english")
    
except ImportError:
    
    print('You are missing some packages! ' \
          'We will try installing them before continuing!')
#     !pip install "numpy" "pandas" "sklearn" "nltk"
    import numpy
    import pandas as pd
    import pickle as pk
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import re
    from nltk.stem.snowball import SnowballStemmer
    import nltk
    stemmer = SnowballStemmer("english")
    print('Done!')

news_articles = pd.read_csv(r"C:\Users\Kishor Kore\Desktop\auto\url_data.csv",
                         encoding='cp1252' )
articles = news_articles['Content'].tolist()

from nltk.stem import WordNetLemmatizer
wnl=WordNetLemmatizer()

def clean_tokenize(document1):
    
    document=""
    for i in document1:
         
        document=document+" "+str(i)+"++++++++++++"
        
    document = re.sub('[^\w_\s-]', ' ',document)       #remove punctuation marks and other symbols
    
    tokens = nltk.word_tokenize(document)
    
    string_word=""
    

    for words in tokens:
        w=wnl.lemmatize(words)
        string_word=string_word+str(w)+" "
    print(string_word)
    return string_word

#     cleaned_article = ' '.join([stemmer.stem(item) for item in tokens])    #Stemming each token
#     return cleaned_article
print("_________________________________")

cleaned_articles = articles
print("++++++++++++++++")
user_articles = "virat kohli"

tfidf_matrix = TfidfVectorizer(stop_words='english', max_df=2)
print("++++++++++++++++1")
article_tfidf_matrix = tfidf_matrix.fit_transform(list(str(cleaned_articles)))
print("++++++++++++++++2")
article_tfidf_matrix  
print("++++++++++++++++3")
user_article_tfidf_vector = tfidf_matrix.transform([user_articles])
print("++++++++++++++++4")
articles_similarity_score=cosine_similarity(article_tfidf_matrix , user_article_tfidf_vector )
print("++++++++++++++++5")
recommended_articles_id = articles_similarity_score.flatten().argsort()[::-1]
print("++++++++++++++++6")
final_recommended_articles_id = [article_id for article_id in recommended_articles_id 
                                 if article_id not in [1,2] ] 

print(final_recommended_articles_id)