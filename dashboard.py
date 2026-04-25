import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit.components.v1 as components
from sklearn.ensemble import GradientBoostingRegressor
# Import your ML libraries
import joblib 

@st.cache_resource
def load_my_model():
    # Ensure rank_model.pkl dashboard file ke saath wale folder mein ho
    return joblib.load("rank_model.pkl")

model = load_my_model()
# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="JEE Advanced Analytics & Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CSS TO REMOVE TOP SPACE AND SIDEBAR ---
st.markdown("""
    <style>
        /* 1. Top padding aur Header ko remove karne ke liye */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 5rem;
            padding-right: 5rem;
        }
        
        /* 2. Sidebar ko poora hide karne ke liye agar zaroorat nahi hai */
        [data-testid="stSidebar"] {
            display: none;
        }

        /* 3. Sidebar toggle button ko hide karne ke liye */
        [data-testid="stSidebarNav"] {
            display: none;
        }
        
        /* 4. Streamlit header (deploy button etc) ko thoda clean karne ke liye */
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- CUSTOM CSS FOR DARK MODE & STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION (The Ribbon) ---
# --- TOP NAVIGATION RIBBON ---
# 'orientation="horizontal"' ise top ribbon banata hai
# --- TOP NAVIGATION RIBBON ---
selection = option_menu(
    menu_title=None,  # No title for the ribbon
    options=[
        "Home", 
        "Difficulty Level", 
        "Gender Wise Analysis", 
        "Parent Occupation",
        "Category Analysis",
        "Fee Analysis", 
        "Rank Predictor", 
        "College Predictor"
    ],
    # Har option ke liye ek unique aur sahi icon (Bootstrap Icons)
    icons=[
        "house",           # Home
        "bar-chart-line",  # Difficulty Level
        "gender-ambiguous",# Gender Wise
        "people", 
        "tags",             # Parent Occupation
        "cash-stack",      # Fee Analysis
        "graph-down",      # Rank Predictor
        "mortarboard"      # College Predictor
    ], 
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important", 
            "background-color": "#0e1117",
            "border-radius": "0px"
        },
        "icon": {
            "color": "#ff4b4b", 
            "font-size": "18px"
        }, 
        "nav-link": {
            "font-size": "14px", # 7 options hain toh size thoda chota rakha hai taaki fit ho jaye
            "text-align": "center", 
            "margin": "0px", 
            "--hover-color": "#262730",
            "color": "white"
        },
        "nav-link-selected": {
            "background-color": "#ff4b4b",
            "font-weight": "bold"
        },
    }
)
# --- 1. HOME SECTION ---
if selection == "Home":
    st.title("JEE Advanced Analysis")
    
    # Updated parameter to avoid the deprecation warning
    st.image("image/iit.jpg", caption="Do you know? IIT Roorkee :Has been Renowned College, specially for Civil Engg. Known as Thomson College of Civil Engineering in Older Times", use_container_width=True)

    st.subheader("Brief Description of previous 10+ years")
    
    st.write("""
    JEE Advanced is one of the toughest engineering entrance exams globally. 
    Through this analysis, the analyst wants to acknowledge viewers with 
    the various hidden statistical inferences of the exam. Whether it is:
    
    * **Cut-off trends** over the years.
    * **Female Participation** over the years.
    * **Registration fee** evolution.
    * **Parental Occupation** of selected students.
    
    And many more...
    """)

    st.markdown("### 🛠️ Integrated Tools")
    col1, col2 = st.columns(2)
    with col1:
        st.success("**1. Rank Predictor**")
    with col2:
        st.success("**2. College Predictor**")
             
    st.write("Whether you are researching or surfing, just give it a try!")
    st.info("Explore more using the Menu Bar above.")

   
# --- 2. DIFFICULTY LEVEL ANALYSIS ---
elif selection == "Difficulty Level":
    st.title("Difficulty Level Analysis")
    # List of details (Aap yahan apni headings aur paths change kar sakte hain)
    # Maine isse list mein rakha hai taaki code neat rahe
    analysis_items = [
    {
        "heading": "1. Total Marks Pattern (Exam Structure Changes)",
        "type": "image", 
        "file": "image/01_total_marks.png", 
        "text": "It can be inferred that JEE Advanced is highly volatile in terms of maximum marks. The year 2015 (IIT Bombay) was an extreme outlier with 504 marks. Interestingly, the exam has stayed constant at 360 marks for the last 5 years."
    },
    {
        "heading": "2. Cutoff % vs Highest Score % vs Avg Score % (Static View)",
        "type": "image", 
        "file": "image/02_score_percentages.png", 
        "text": "It is not strange to note that, in the exam where the topper is scoring marks greater than 80 percent approx. every year, the cutoff for the open-general category is prone to being below 40 percent. This shows the real level and toughness of the examination. It is the exam, where the average score of the candidates is not even 20 percent."
    },
    {
        "heading": "3. Interactive Score Distribution Dashboard", 
        "type": "html", 
        "file": "html/02_score_percentages_dark.html", 
        "text": "I would like to draw your attention to the curious point, In year 2024 for the first time someone scored the score of greater than 98 percent in such a examination. The student who scored is Chidvilas Reddy"
    },
    {
        "heading": "4. Subject-wise Average Marks Trend using z-scores", 
        "type": "image",
        "file": "image/03_subject_avg_trend.png",
        "text": '''Chemistry:\n
1. Peak (~ +1.3 in 2014) → Chemistry was relatively easier that year\n
2. Consistent positive (2015–2018) → Stable, scoring-friendly phase\n
3. Sharp dip (~ -1.7 in 2020) → clearly tougher paper\n
4. Recovery (2023–2024) → back to above-average scoring\n
5. 2025 drop again → slight increase in difficulty\n
Physics:\n
1. Peak (~ +1.8 in 2017–18) → easiest phase for Physics\n
2. Major drop (~ -1.9 in 2022) → toughest year in entire dataset\n
3. Frequent swings → up-down pattern more than Chemistry\n
Maths:\n
1. Highest peak (~ +2.1 in 2017) → extremely scoring year\n
2. Deep dip (~ -1.8 in 2022) → very tough year\n
3. Post-2022 recovery → gradually improving\n
'''
    },
    {
        "heading": "5. Subject-wise Cutoff Evolution", 
        "type": "image",
        "file": "image/04_subjectwise_cutoff.png",
        "text": '''The Plot shows steady decrease in the individual subject Cut-off's.\n
        One possible reason apart from toughness:
         The IIT system have gradually increased the total number of seats in the IIT's which could result in this
        behaviour.\n
          Another Point to note, Initially the Individual cutoff's for the subject differed significantly form each other,
        but from 2016 onwards they have been publishing the report stating the constant cutoff percentage in each
             subject. However, overall cut-off thrives varying.
            The equal subject cutoff percentage sometimes seems really benificial, beacause, If in a year a particular subject
            like Math in 2017, might increase subject cutoff making qualifying difficult for student weak in Math'''
    },
    {
        "heading": "6. Toughness Index (Composite Analysis)",
        "type": "image", 
        "file": "image/05_toughness_index.png", 
        "text": "2022 Set By IIT Bombay Tested the student's mind on complex math and physics concepts. While in 2017, IIT Madras Served as the Easied Year in JEE Advanced History."
    },
    {
        "heading": "7. Topper vs Cutoff Gap (Zenith vs Minimum)",
        "type": "image", 
        "file": "image/06_topper_vs_cutoff.png", 
        "text": "The difference between the topper and the General cutoff is between 200-300 range for max of the year, but the year 2015 served as the year with highest maximum marks 504, along with the fact that difference between topper and cutoff is extreme outlier, definitely the topper has exceptional talent to score such high. That candidate :  Satvat Jagwani"
    },
    {
        "heading": "8. Bonus Marks Impact & Distribution", 
        "type": "image",
        "file": "image/07_bonus_marks.png",
        "text": "In addition to the fact that JEE Advanced 2015 was the easiest in all, It contained wrong questions under many sections, which resulted in awarding highest bonus marks till now.\n Having this level of error prone paper is not acceptable in such national exam hence, the organizer must have taken lesson not to repeat it again\n but Minimal errors continued in susequent years."
    }
]

    # Loop to render all 7 sections
    for item in analysis_items:
        st.subheader(item["heading"])
        
        if item["type"] == "image":
            # Image render karne ka logic
            try:
                st.image(item["file"], use_container_width=True)
            except:
                st.warning(f"Image '{item['file']}' nahi mili.")
        
        elif item["type"] == "html":
            # HTML Plotly render karne ka logic
            try:
                with open(item["file"], 'r', encoding='utf-8') as f:
                    html_data = f.read()
                # Height aap apne plot ke hisaab se set kar sakte hain (e.g., 500)
                components.html(html_data, height=500, scrolling=True)
            except:
                st.error(f"HTML file '{item['file']}' load nahi ho payi.")

        # Common Interpretation Box
        st.markdown(f"""
        <div style="background-color: #1e1e30; padding: 15px; border-left: 5px solid #ff4b4b; border-radius: 5px; margin-bottom: 30px;">
            <p style="margin: 0; color: #ffffff;"><strong>💡 Interpretation:</strong> {item['text']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
    # --- FINAL CONCLUSION SECTION ---
    st.markdown("## 🏁 Final Conclusion: Difficulty Level")
    st.success(
    "So far we can conclude that, the exam where the highest score is even above 90 percent in almost years.\n")
    st.success("But, the students are struggling in even scoring 20 percent of total marks.\n")
    st.success("This really highlights how much strong preparation is required to ace the exam.\n")
    st.success( "The paper tests every aspect of subject at deep level which requires consistent effort.\n")
    st.success("Also, neglecting a particular subject results in disqualification since individual cutoff plays a vital role.\n")
    st.success("Among the three, Maths is the most effort and deep analytical thought process demanding subject.")
    
    st.write("Reached to End of Difficulty Analysis.")

elif selection == "Gender Wise Analysis":
    st.title("Gender-wise Analysis")
    st.markdown("### Trends of Gender-wise Participation (2011 - 2025)")
    st.markdown("---")

    # Gender-specific list
    gender_analysis_items = [
        {
            "heading": "Female Percentage In Total Students",
            "type": "image", 
            "file": "image/09_female_pct_trend.png", 
            "text": "The plot speaks that Participation of Female in India Most Premier Institutions has been considerably low since inception of the exam. "
            "Mainly the things that could be held accountable is The thinking that girls should not get involved in the Engineering fields. One should definitely not doubt on the brains of female, Because the same girl performs extreamely Outstanding in NEET Examination"
        },
        {
            "heading": "Male vs Female Participation",
            "type": "image", 
            "file": "image/10_stacked_male_female.png", 
            "text": "Male Participation have increased significantly Year on Year"
        },
        {
            "heading": "Female Admission % over Years - Major IITs",
            "type": "html", 
            "file": "html/female.html", 
            "text": '''Till 2018 all IIT's had extremely low participation, But, one would be feel strange to know that Most female preferred the IIT's in southern part of country.
              It could have possible reason, they belong to southern part i.e literacy rates have been
                significantly higher in southern states of the country.
                In 2018, Government Decided to give 20% reservation to the female (supernumerary seats) to promote inclusion in engineering-Technology.
                It indeed increased participation, can be admired as the good initiative taken towards inclusive education.'''
        },
        {
            "heading": "Year wise Female admission per IIT",
            "type": "image", 
            "file": "image/11_iit_year_heatmap.png", 
            "text": "A seperation between two era pre 2018 and post 2018"
        },
        {
            "heading": "Top -5 and Bottom - 5 IIT Based On female Admissions",
            "type": "image", 
            "file": "image/12_top_bottom_iits.png", 
            "text": "One Could go interpreting that The IIT's in the Eastern, and Northern India are less opted by females. But, Before that one should be aware of the fact that they are older IIT's with yearly intake of 1000+ and in that the percentage of girls seems very less. Also, they have some really core branches like Mining, Petroleum, Metallurgy which are generally avoided by females"
        },
       
    ]

    # Parsing Loop (Same logic as Difficulty section)
    for item in gender_analysis_items:
        st.subheader(item["heading"])
        
        if item["type"] == "image":
            try:
                st.image(item["file"], use_container_width=True)
            except:
                st.warning(f"Image '{item['file']}' nahi mili.")
        
        elif item["type"] == "html":
            try:
                with open(item["file"], 'r', encoding='utf-8') as f:
                    html_data = f.read()
                import streamlit.components.v1 as components
                components.html(html_data, height=550, scrolling=True)
            except:
                st.error(f"HTML file '{item['file']}' load nahi ho payi.")

        # Interpretation Box
        st.markdown(f"""
        <div style="background-color: #1e1e30; padding: 15px; border-left: 5px solid #ff4b4b; border-radius: 5px; margin-bottom: 30px;">
            <p style="margin: 0; color: #ffffff;"><strong>💡 Insight:</strong> {item['text']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")

    # Gender Section Conclusion
    st.markdown("## 🏁 Conclusion: Gender Diversity")
    st.info("Gender-neutral seats Along with Supernumerary seats made IITs more Inclusive.")

elif selection == "Parent Occupation":
    st.title("Parent's Occupation Analysis")
    st.markdown("### Socio-Economic Background vs Success Trends")
    st.markdown("---")

    # Occupation-specific list
    occupation_analysis_items = [
        {
            "heading": "1. Parent Occupation — All-time Share of JEE Advanced Students\n(2011–2018)",
            "file": "image/15_occupation_alltime_share.png", 
            "text": "Analysis tells us that Government Service aur Business background students are more in number, but Agriculture background is also showing steady growth."
        },
        {
            "heading": "2. Students by Top 5 Parent Occupation",
            "file": "image/17_top5_trend.png", 
            "text": "It Probably means that Students with parents working in Agriculture or small private sectors are try hard to improve their livelihood, such students have been increasing since 2015. One of the reason could be in 2015 the digitalization in India started flourishing which connected people with various information that wasn't available earlier. Hence, students from agricultural families showed significant selection"
        },
        {
            "heading": "3. students with parent working in Agri-Business-Govt.",
            "file": "image/18_govt_agri_biz.png", 
            "text": "Though the Business and Govt. sector occupation parent's child have significant stake in selection. But, selection from agriculture sector-student is relatively lower"
        }
    ]

    # Parsing Loop (Images only, no HTML logic needed here)
    for item in occupation_analysis_items:
        st.subheader(item["heading"])
        
        try:
            st.image(item["file"], use_container_width=True)
        except:
            st.warning(f"Image '{item['file']}' nahi mili. Check path!")

        # Interpretation Box
        st.markdown(f"""
        <div style="background-color: #1e1e30; padding: 15px; border-left: 5px solid #ff4b4b; border-radius: 5px; margin-bottom: 30px;">
            <p style="margin: 0; color: #ffffff;"><strong>💡 Interpretation:</strong> {item['text']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")

    # Section Conclusion
    st.markdown("## 🏁 Final Conclusion: Socio-Economic Impact")
    st.success("""
    Data suggests that despite of urban background and service-class families dominance, 
    rural and farming backgrounds students rank improvement rate has improved over years.
    """)
    st.write("End of the section")



elif selection == "Fee Analysis":
    st.title("Fee Analysis")
    st.markdown("### Analysing how the registeration fee and IIT fee changed over Time")
    st.write("The absolute Inflation in premier higher Education Institution")
    st.markdown("---")

    # Occupation-specific list
    fee_analysis = [
        {
            "heading": "1. Registration Fee Trend","type":"image",
            "file": "image/regfee.png", 
            "text": "If it continue to grow at the current rate then Future Predictions: 2026 -> ₹ 3462.85,  2027 -> ₹ 3598.21, 2028 -> ₹ 3733.57"
        },
        {
            "heading": "2. Year On Year Growth curve","type":"image",
            "file": "image/yoy.png", 
            "text": "The most of all hikes occurred during 2011 to 2012 of 60% hike from previous registration fee"
        },
        {
            "heading": "3. Inflation in Fee per sem in IIT's","type":"html",
            "file": "html/21_applicants_qualifiers_fee.html", 
            "text": "The most of all fee hikes was the hike in 2017 of 122 % till date"
        }
    ]

    # Parsing Loop (Images only, no HTML logic needed here)
    for item in fee_analysis:
        st.subheader(item["heading"])
        
        if item["type"] == "image":
            try:
                st.image(item["file"], use_container_width=True)
            except:
                st.warning(f"Image '{item['file']}' nahi mili.")
        
        elif item["type"] == "html":
            try:
                with open(item["file"], 'r', encoding='utf-8') as f:
                    html_data = f.read()
                import streamlit.components.v1 as components
                components.html(html_data, height=550, scrolling=True)
            except:
                st.error(f"HTML file '{item['file']}' load nahi ho payi.")

        # Interpretation Box
        st.markdown(f"""
        <div style="background-color: #1e1e30; padding: 15px; border-left: 5px solid #ff4b4b; border-radius: 5px; margin-bottom: 30px;">
            <p style="margin: 0; color: #ffffff;"><strong>💡 Insight:</strong> {item['text']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")

    # Section Conclusion
    st.markdown("## 🏁 Final Conclusion: Financial Dimension")
    st.success("""
In 2011–2012, the applicant pool was massive (around 250,000–280,000) because there was no JEE Main filter—students could directly attempt JEE Advanced. In 2013, JEE Main became compulsory, which reduced the number of applicants to around 48,000–50,000.
At the same time, the fee structure increased in three stages: ₹25,000 (2011–2013) → ₹45,000 (2014–2016) → ₹100,000 (2017 onward). Despite these fee hikes, there was no significant drop in the number of applicants. This indicates that demand is inelastic—aspirants targeting IITs are not significantly discouraged by higher fees.
    """)

elif selection == "Category Analysis":
    st.title("Category-wise Trend Analysis")
    st.markdown("### Analysis of Cut-offs & Seat Distribution across Categories")
    st.write("Performance of students from different categories")
    st.markdown("---")

    category_items = [
        {
            "heading": "Applicants vs Qualifiers — Category-wise Deep Dive (2013–2025)",
            "file": "image/24_category_deepdive.png", 
            "text": '''\nGeneral Category : The No. of students appearing in examination have always been higher in numbers,that is held accountable by the fact that most of general candidates are well aware of the examination. Since, good chunk of general population have atleast one parent educated in the family, execeptions are excused.The advantage is clearly visible through the selection rate in various years.
            \nOBC Category : The number of students taking the examination though comparable enough with general students. But, the selection rate is relative lower than as compared to general students.The difference is probably due to the unavailability of mentorship and guidance. Since, a good chunk of OBC student have both parents not even completed high school education.
            \nSC Category : The participation from these students have been comparatively on lower side. But, the slection ratio has changed abrupty showing increasing selection rates.
            \nST Category : The most vulnerable students in the examination. Though government gave reservation to the ST students but the participation from them stood on extreme lower side.
            The possible reason could be their social and economical condition are highly unstable, which creates the difficulty for student to even pursue studying.\n'''
        }
    ]

    for item in category_items:
        st.subheader(item["heading"])
        try:
            st.image(item["file"], use_container_width=True)
        except:
            st.warning(f"Image '{item['file']}' nahi mili.")

        st.markdown(f"""
        <div style="background-color: #1e1e30; padding: 15px; border-left: 5px solid #ff4b4b; border-radius: 5px; margin-bottom: 30px;">
            <p style="margin: 0; color: #ffffff;"><strong>💡 Insight:</strong> {item['text']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("---")

# --- 4. RANK PREDICTOR TOOL ---
elif selection == "Rank Predictor":
    st.title("📉 JEE Advanced Rank Predictor")
    st.write("Enter your details to predict your CRL rank based on Gradient Boosting model.")

    # Input Fields
    mmarks = st.number_input("Maximum Marks of the Paper", min_value=1, max_value=1000, value=360)
    marks = st.number_input("Your Marks Received", min_value=0, max_value=1000, value=150)
    candidates = st.number_input("Estimated Total Candidates", min_value=10000, value=180000)
    
    if st.button("Predict Rank"):
        try:
            # 1. Feature Engineering (Training ke logic ke hisaab se)
            pct = marks / mmarks
            
            # 2. DataFrame banana padega varna "Feature Names Mismatch" error aayega
            X_pred = pd.DataFrame([[pct, pct**2, pct**3, candidates, mmarks]], 
                                   columns=['pct_score', 'pct2', 'pct3', 'no of candidates', 'max marks'])
            
            # 3. Prediction (Aapne training me log(Rank) liya tha, toh exp() lagana zaroori hai)
            log_rank = model.predict(X_pred)[0]
            final_rank = int(np.round(np.exp(log_rank)))

            # 4. Result display
            if final_rank <= 30000:
                st.success(f"### Predicted CRL Rank: {final_rank}")
            else:
                st.success("Not Qualified to be in CRL")
            
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Check karo ki model load hua hai ya nahi aur features wahi hain ya nahi.")

# --- 5. COLLEGE PREDICTOR TOOL ---
elif selection == "College Predictor Tool":
    st.title("🏛️ IIT College Predictor")
    st.write("Find the best IIT and Branch for your rank.")
    
    user_rank = st.number_input("Enter your JEE Advanced Rank", min_value=1)
    category = st.selectbox("Category", ["General", "OBC-NCL", "SC", "ST", "EWS"])
    gender = st.selectbox("Gender", ["Gender-Neutral", "Female-only"])

    if st.button("Find My College"):
        # prediction_logic(user_rank, category, gender)
        st.table(pd.DataFrame({
            "IIT Name": ["IIT Bombay", "IIT Delhi", "IIT Madras"],
            "Branch": ["Mechanical", "Civil", "Chemical"],
            "Closing Rank (Prev Year)": [1500, 2200, 3100]
        }))

# --- FOOTER ---
st.sidebar.markdown("---")
if st.sidebar.button("Reached to End"):
    st.balloons()
    st.sidebar.success("Dhanyawad! Hope this helps your preparation.")
