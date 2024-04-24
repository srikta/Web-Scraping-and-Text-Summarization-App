import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import newspaper

def summarize_text(text, num_sentences=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    summarized_text = " ".join(str(sentence) for sentence in summary)
    return summarized_text

def scrape_and_summarize(url, num_sentences=2):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    text = article.text
    summarized_text = summarize_text(text, num_sentences)
    return summarized_text

def main():
    st.title("Web Scraping and Text Summarization App")

    # Text input box for the user to enter URL
    url = st.text_input("Enter URL of the News Article:")

    # Slider to select the number of sentences in the summary
    num_sentences = st.slider("Number of Sentences in Summary:", min_value=1, max_value=10, value=2)

    # Button to scrape and summarize the article
    if st.button("Summarize"):
        if url:
            summarized_text = scrape_and_summarize(url, num_sentences)
            st.subheader("Summary:")
            st.write(summarized_text)
        else:
            st.warning("Please enter the URL of the news article.")


main()
