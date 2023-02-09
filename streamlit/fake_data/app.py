# Core Pkgs
import streamlit as st 
# Data Pkgs
import pandas as pd 
from faker import Faker
fake = Faker()
#Utils
import base64
import time 
timestr = time.strftime("%Y%m%d-%H%M%S")
#Fxn to Download Into A Specified Format
def make_downloadable_df_format(data,format_type="csv"):
    if format_type == "csv":
        datafile = data.to_csv(index=False)
    elif format_type == "json":
        datafile = data.to_json()
    b64 = base64.b64encode(datafile.encode()).decode()  # B64 encoding
    st.markdown("### ** Download File  📩 ** ")
    new_filename = "fake_dataset_{}.{}".format(timestr,format_type)
    href = f'Click Here!'
    href = '<a href="data:application/octet-stream;base64,%s" download="%s">Download %s</a>' % (b64,new_filename,new_filename) # decode b'abc' => abc

    st.markdown(href, unsafe_allow_html=True)

# Generate A Simple Profile
def generate_profile(number,random_seed=200):
    Faker.seed(random_seed)
    data = [fake.simple_profile() for i in range(number)]
    df = pd.DataFrame(data)
    return df 
# Generate A Customized Profile Per Locality
def generate_locale_profile(number,locale,random_seed=200):
    locale_fake = Faker(locale)
    Faker.seed(random_seed)
    data = [locale_fake.simple_profile() for i in range(number)]
    df = pd.DataFrame(data)
    return df 

# number_to_gen = st.sidebar.number_input("Number",10,5000)
# locale = st.sidebar.multiselect("Select Locale",localized_providers,default="en_US")
# dataformat = st.sidebar.selectbox("Save Data As",["csv","json"])

def main():
  st.title("Fake Data Generator")
  menu = ["Home","Customize","About"]
  localized_providers = ['ja_JP','en_US','es_MX']

  choice = st.sidebar.selectbox("Menu",menu)
  if choice == "Home":
      st.subheader("Home")
      number_to_gen = st.sidebar.number_input("Number",10,5000)
      locale = st.sidebar.multiselect("Select Locale",localized_providers,default="en_US")
      dataformat = st.sidebar.selectbox("Save Data As",["csv","json"])

      df = generate_locale_profile(number_to_gen,locale)
      st.dataframe(df)

      st.write(df['sex'].value_counts())
      with st.expander("📩: Download"):
          make_downloadable_df_format(df,dataformat)

  elif choice == "Customize":
      st.subheader("Select Your Fields")

      locale = st.sidebar.multiselect("Select Locale",localized_providers,default="en_US")

      profile_options_list = ['username', 'name', 'sex' , 'address', 'mail' , 'birthdate''job', 'company', 'ssn', 'residence', 'current_location', 'blood_group', 'website'] 
      profile_fields = st.sidebar.multiselect("Fields",profile_options_list,default='username')

      number_to_gen = st.sidebar.number_input("Number",10,10000)
      dataformat = st.sidebar.selectbox("Save Data As",["csv","json"])

      custom_fake = Faker(locale)
      data = [custom_fake.profile(fields=profile_fields) for i in range(number_to_gen)]
      df = pd.DataFrame(data)


      st.dataframe(df)


      with st.expander("🔍: View JSON "):
          st.json(data)

      with st.expander("📩: Download"):
          make_downloadable_df_format(df,dataformat)


  else:
      st.subheader("About")
      st.success("Built with Streamlit")
      st.info("Jesus Saves @JCharisTech")
      st.text("By Jesse E.Agbe(JCharis)")

if __name__ == '__main__':
	main()