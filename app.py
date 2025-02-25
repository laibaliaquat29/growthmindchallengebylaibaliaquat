#streamlit
import streamlit as st
st.set_page_config(page_title= "growth mindset project")
st.title("growth mindset challenge:web app with streamlit")

st.header("✈️ welcome to your growth journey!")
st.write("embarace challenges, learn from mistakes and unlock your full potential. this AI powerd app helps you build growth mindset with reflection, challenges, and achivements!")

#quote section
st.header("today's growth mindset quote")
st.write("Success is the sum of small efforts, repeated day in and day out Success is not a good  start. failure makes you humble")


st.header("🔧 what's your challenge today?")
user_input =("describe a challenge you're facing:")


#condition
if user_input:
    st.success(f"💪🏻you're facing: {user_input}. keep pushing forward your goal✈️.") 

else:
    st.warning("tell usabout your challenge to get started")

 #reflexing
st.header("reflect on your learning")
reflection = st.text_area("write your reflection here")

if reflection:
  st.success (f"✨great insight! yourreflection:")
else:
 st.info("reflecting on past experiance help you grow! share yor difficulties")
 
 #achievements
st.header("🏆 celebrate your wins")
achievements = st.text_input("share something you've recently accomplished:")


if achievements:
   st.success(f"⭐ amazing! you achieved: {achievements}")
else:
    st.info("big or small every achievement counts, share on now🌟🏆🎯")

    #footer 
    st.write("- - -")
    st.write("✈️keep beliving in your self.growth is a journey not a destination")
    st.write("**created by laiba liaquat**")