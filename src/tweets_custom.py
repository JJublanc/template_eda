import pandas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk import Counter
from nltk.corpus import stopwords
from wordcloud import WordCloud
import os

# https://neptune.ai/blog/exploratory-data-analysis-natural-language-processing-tools

def get_word(stop_words: list,
             data: pandas.DataFrame,
             column: str) -> list:
    """
    Get the words from texts in a column of a dataframe, without stop words.
    :param stop_words:
    :param data:
    :param column:
    :return:
    """

    # Get words from text
    text = data[column].str.split()
    text = text.values.tolist()

    # Get words without stop words
    corpus = []
    for item in text:
        try:
            for word in item:
                if word not in stop_words:
                    corpus.append(word)
        except:
            pass

    return corpus


def count_words(words: list) -> [list, list]:
    """
    Count the words in a list of words.
    :param words: list of words
    :return: dictionary of words and their count
    """
    counter = Counter(words)
    most = counter.most_common()

    x, y = [], []
    for word, count in most[:40]:
        x.append(word)
        y.append(count)

    return x, y


def get_wordcloud(data: list, stop_words: list) -> WordCloud:
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stop_words,
        max_words=100,
        max_font_size=30,
        scale=3,
        random_state=1)

    return wordcloud.generate(str(data))


if __name__ == "__main__":
    # make a folder in reports to save the plots
    os.makedirs('./reports/tweets_plots', exist_ok=True)

    # Plot text length
    data = pd.read_csv('./data/tweets/final_data.csv', nrows=1000)
    axis = data['tweet_text'].str.len().hist()
    plt.savefig('./reports/tweets_plots/text_length.png')
    plt.cla()

    # download stopwords
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english') + ["{link}", "{user}", "{hashtag}"])

    # Get words from tweets
    words = get_word(stop_words=stop_words,
                     data=data,
                     column='tweet_text')

    # Count words
    x, y = count_words(words)

    # Save freq plot
    most_freq_plot = sns.barplot(x=y[2:100], y=x[2:100])
    fig = most_freq_plot.get_figure()
    fig.savefig("./reports/tweets_plots/most_freq_plot.png")
    plt.cla()

    # Save wordcloud
    wordcloud = get_wordcloud(data=words, stop_words=stop_words)
    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    plt.imshow(wordcloud)
    plt.savefig("./reports/tweets_plots/wordcloud.png")
