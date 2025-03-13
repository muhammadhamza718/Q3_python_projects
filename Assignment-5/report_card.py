import streamlit as st
import pandas as pd 

def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "F"
    else:
        return "Fail"


st.title("📚 Student Report Card Generator")
st.write("Enter student details and generate their report cards.")

if "students" not in st.session_state:  # Ye if ki condition check kregi ke st.session_state ke andar students ke name ka vaiable hai ya nahi
    # agar nahi hai to hum st.session_state ko ek empty list bana denge
    st.session_state.students = []

# st.form() ko ek unique key chahiye hoti hai warna streamlit error deta hai form_key key generate krega dynamically
form_key = f"student_form_{len(st.session_state.students)}"

# len(st.session_state.students) count karega karega or ek key assign kr dega like student_form_0 | student_form_1 aur aage bhi naye students keliye bhi

with st.form(form_key):  # Mene ek form banaya hai jiska unique identifier Form_key hai kiuke form_key har student keliye unique hai
    
    name = st.text_input("Student Name") # student apna name input me likhga to wo name ke variable me save hojaye
    
    roll_number = st.text_input("Roll Number") # student apna roll number input me likhga to wo roll_number ke variable me save hojaye
    # Ye dono variables baad me report card generate karne ke liye use honge

    st.subheader("Enter Marks (out of 100)") # st.subheader ek title display kr wayega
    # st.number_input ye sirf numbers accept karega text ya negative values accept nahi karega or phir usko ussi subjects ke variable me store kr dega isme min_value 0 or max_value 100 hogi matlab user only 1 to 100 takke number input me likh sakhta hai 

    math = st.number_input("Math", min_value=0, max_value=100, step=1)
    physics = st.number_input("Physics", min_value=0, max_value=100, step=1)
    urdu = st.number_input("Urdu", min_value=0, max_value=100, step=1)
    english = st.number_input("English", min_value=0, max_value=100, step=1)
    computer = st.number_input("Computer", min_value=0, max_value=100, step=1)

    submit = st.form_submit_button("⚙️ Generate Report Card") # Agar user is button ko click karega, to submit variable true ho jayega warna ye false hi rahega
    if submit:
        total_marks = math + physics + urdu + english + computer # Ye har subject ke numbers ko pluse krega or usse total_marks ke variable me store krdega

        percentage = total_marks / 5 # total_marks me se average marks nikalne keliye 5 se divide kar ke percentage ke variable me store kardiya
        grade = calculate_grade(percentage) # ye Function call karega jo percentage ke basis pe grade return karega
        student = { # ek dictionary banayi hai student ke name se jo ek student ka pura data store karega 
            "Name": name,
            "Roll Number": roll_number,
            "Math": math,
            "Physics": physics,
            "Urdu": urdu,
            "English": english,
            "Computer": computer,
            "Total Marks": total_marks,
            "Percentage": f"{percentage:.2f}%", # Percentage ko 2 decimal places tak round off kiya 
            "Grade": grade
        }
        st.session_state.students.append(student) # Ab append ke method ko use krke student ke data ko st.session_state.students(student) me store kardiya

        if st.success:
            st.success(f"✅ Record of {name} has been inserted successfully!") # Form ko submit karne ke bad success ka message show kiya hai or success ke message me dynamically user ka name bhi show kiya hai f ka method use krke
        else:
            st.error("Please fill all the fields correctly.")

if st.session_state.students:
    st.subheader("📄 Generated Report Cards")
    df = pd.DataFrame(st.session_state.students) # Pandas DataFrame ek liberary hai jo students ka data convert karega table format me or phir usse df ke variable me store kardiya
    st.dataframe(df) # df ke variable me jo students ka data hai usko table format me show kardiya streamlit ka use krke



