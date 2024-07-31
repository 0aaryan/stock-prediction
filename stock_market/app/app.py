import streamlit as st
from stock_market.scrapers.twitter import TwitterScraper
def main():
    st.title('Stock Market App')
    st.write('Welcome to the Stock Market App!')
    words = st.text_input('Enter the words you want to search for ( comma separated )') 
    from_date = st.date_input('Enter the start date (yyyy-mm-dd)')
    until = st.date_input('Enter the end date (yyyy-mm-dd)')
    interval = st.text_input('Enter the interval (number of days)')

    if st.button('Scrape Tweets'):
        scraper = TwitterScraper(words, from_date.strftime('%Y-%m-%d'), until.strftime('%Y-%m-%d'), int(interval))
        data = scraper.scrape_tweets()
        st.write(data)

if __name__ == '__main__':
    main()
