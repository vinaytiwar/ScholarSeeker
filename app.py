import streamlit as st
from paper_search import search_papers
from summarizer import summarize_paper

st.title("📚 ScholarSeeker - Deep Web Research Paper Assistant")

query = st.text_input("Enter your research topic or question:")

if query:
    st.write("🔍 Searching...")
    papers = search_papers(query)
    for paper in papers:
        st.markdown(f"### [{paper['title']}]({paper['url']})")
        st.markdown(f"**Authors:** {paper['authors']}")
        st.markdown(f"**Published:** {paper['published']}")
        summary = summarize_paper(paper['summary'])
        st.markdown(f"**Summary:** {summary}")
        st.markdown("---")