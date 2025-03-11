from django.shortcuts import render

def resume(request):
    context = {
        "name": "Aravapalli Nagaraja Meenakshi",
        "phone": "+91 9177855335",
        "email": "aravapallimeenakshi@gmail.com",
        "linkedin": "https://www.linkedin.com/in/aravapalli-meenakshi-122b34299",
        "codechef": "https://www.codechef.com/users/meenu_9701",
        "leetcode": "https://leetcode.com/u/Meenu_27/",
        "hackerrank": "https://www.hackerrank.com/profile/23b01a1208",
        
        'university': 'Shri Vishnu Engineering College for Women',
        'location': 'Vishnupur,Bhimavaram,West Godavari,India',
        'degree': 'B.Tech in Information Technology',
        'duration': '2023-2027','btech_cgpa': 8.79,

        'intermediate_school': 'Narayana Junior College',
        'intermediate_location': 'Ongole,Prakasam,India',
        'intermediate_degree': 'Higher Secondary',
        'intermediate_duration': '2021-2023',
        'intermediate_percentage': 96,
        
        'school': 'Guntur Oxford School',
        'school_location': 'Ongole,Prakasam,India',
        'school_degree': '10th Grade',
        'school_duration': '2020-2021',
        'school_percentage': 98,

        "languages": "Python, Java, C",
        "web_development": "HTML, CSS, Bootstrap, Django",
        "databases": "MySQL,SQL Developer",
        "tools": " VS Code",
        "projects": [
            {
                "name": "Portfolio Website",
                "description": "A personal portfolio website showcasing my projects and skills.",
                "features": [
                    "Built using Django and Bootstrap.",
                    "Includes a blog section and project showcase.",
                    "Hosted on GitHub Pages with custom domain."
                ]
            },
            {
                "name": "Weather App",
                "description": "A web application to check real-time weather updates.",
                "features": [
                    "Uses OpenWeather API to fetch real-time weather data.",
                    "Built with Flask and JavaScript.",
                    "Displays temperature, humidity, and weather conditions."
                ]
            }
        ],
        "certifications": [
            "Python for Fundamentals - Infosys Springboard",
            "Advanced Data structur using python -Infosys Springboard ",
            "Java Foundation Certificate - Infosys Springboard"
        ],
        "hobbies": [
            "Competitive Coding (LeetCode, Codeforces, HackerRank)",
            "Building Web Applications",
            "Problem Solving and Debugging"
        ]
    }
    return render(request, "resume/resume_templates.html", context)