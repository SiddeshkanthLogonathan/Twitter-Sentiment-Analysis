import matplotlib.pyplot as plt
from wordcloud import WordCloud
plt.style.use('fivethirtyeight')

def plot_word_cloud(df):
    all_words = ''.join([twts for twts in df['Tweets']])
    word_cloud = WordCloud(width=500, height=300, random_state=21, max_font_size=119).generate(all_words)

    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()

def plot_polarity_vs_subjectivity(df):
    plt.figure(figsize=(8,6))
    for i in range(0, df.shape[0]):
        plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Blue')

        plt.title('Sentiment Analysis')
        plt.xlabel('Polarity')
        plt.ylabel('Subjectivity')
    plt.show()

def show_value_counts(df):
    df.Analysis.value_counts()

    plt.title('Sentiment Analysis')
    plt.xlabel('Sentiment')
    plt.ylabel('Counts')
    df.Analysis.value_counts().plot(kind='bar')
    plt.show()

