import streamlit as st
st.title("Welcome to the game")

s1 = st.text_input("Enter first name-")
s2 = st.text_input("Enter second name-")
s1 = list(s1)
s2 = list(s2)

count = 0

for i in range(len(s1)):
  for j in range(len(s2)):
    if s1[i] == s2[j]:
      s1[i] = "0"
      s2[j] = "0"
      break
    
for i in s1+s2:
  if i != '0':
    count += 1

res = ["Friends","Lovers","Affection","Marriage","Enemies","Sisters"]

while len(res) > 1:
  splitIndex = (count % len(res)) - 1
  if splitIndex >= 0:
    right = res[splitIndex + 1:]
    left = res[:splitIndex]
    res = right + left
  else:
    res = res[:len(res) - 1]
    
if(st.button("Submit")):
  st.success(res[0])