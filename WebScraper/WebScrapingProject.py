import streamlit as st
from tofler import tofler_func
from zauba import zauba_func
file=open('auto_data.txt','r+')
data=file.readlines()
all_stocks=[i.title().replace(" Pvt.","").replace(" Ltd.","").replace(" Ltd","").replace(" Pvt","").strip() for i in data]
all_stocks.append("")
all_stocks=list(sorted(set(all_stocks)))
st.set_page_config("Data Scraper Project")
st.markdown("""
<style>
.css-d1b1ld.edgvbvh6
{
  visibility:hidden;
}
.css-1v8iw7l.eknhn3m4
{
  visibility:hidden;
}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stMainBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.stForm.st-emotion-cache-4uzi61.e10yg2by1 > div > div > div > div:nth-child(2) > div > div > div > div > svg
{
  visibility:hidden;
}

</style>
""",unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;'>Data Scraping Website</h1>",unsafe_allow_html=True)
form1 = st.form("Details",clear_on_submit=True)
comp = form1.radio("From which site do you want to access the data?",["Tofler","Zauba"])
data = form1.selectbox("Enter the company name : ",options=all_stocks,placeholder="Type Here...")
submit = form1.form_submit_button("Submit")
process1=st.empty()
process2=st.empty()
process1.markdown("<h3 style='text-align:center;'>Demo of How The Website Works</h3>",unsafe_allow_html=True)
process2.video("demo.webm")
if submit:
  process2.text("")
  process1.text("")
  if comp=="Tofler":
    st.write("Fetching details from "+comp)
    try:
      tofler_func(data)
    except Exception:
      st.write("""The site landed onto an error while handling the request.
                  Kindly search again.
                  If still the error pertains, then the company might not be listed on the particular website.
                  Try searching for some other company.
               """)
  elif comp=="Zauba":
    st.write("Fetching details from "+comp)
    try:
      zauba_func(data)
    except Exception:
      st.write("""The site landed onto an error while handling the request.
                  Kindly search again.
                  If still the error pertains, then the company might not be listed on the particular website.
                  Try searching for some other company.
               """)