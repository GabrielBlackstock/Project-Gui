# -*- coding: utf-8 -*-
import tkinter as tk
import webbrowser
import json
import os
from datetime import datetime, timedelta

# Define projects and their descriptions with associated links
projects = {
    "Software Engineering": {
        "To-Do List Application": {
            "description": "A web-based application to manage daily tasks.",
            "links": [
                ("YouTube Video", "https://youtu.be/G0jO8kUrg-I?si=o5Wg_mdryOvB_Xrw"),
                ("Article for To-Do List App", "https://github.com/topics/todo-list-app"),
                ("Article for To-Do List App", "https://www.w3schools.com/howto/howto_js_todolist.asp"),
            ]
        },
        "Blog Platform": {
            "description": "A platform where users can create, edit, and delete blog posts.",
            "links": [
                ("YouTube Video", "https://www.youtube.com/watch?v=Aj7HLsJenVg&ab_channel=freeCodeCamp.org"),
                ("Article for Blog Platform", "https://levelup.gitconnected.com/setup-project-for-blog-in-fastest-way-part-1-54e6d47e2c44?gi=d68ec345ac8c"),
                ("Article for Blog Platform", "https://www.linkedin.com/pulse/building-simple-blogging-platform-using-python-html-css-corbeel-8fs5e/"),
            ]
        },
        "Weather Dashboard": {
            "description": "A dashboard displaying real-time weather information.",
            "links": [
                ("YouTube Video", "https://youtu.be/MIYQR-Ybrn4?si=_wH2qp9f2IAFWfnU"),
                ("Article for Weather Dashboard", "https://github.com/topics/weather-dashboard"),
                ("Article for Weather Dashboard", "https://medium.com/@yosami14/creating-a-weather-dashboard-using-html-css-and-javascript-217f80229fb"),
            ]
        },
    },
    "AI Engineering": {
        "Handwritten Digit Recognition": {
            "description": "A model to recognize handwritten digits using the MNIST dataset.",
            "links": [
                ("YouTube Video", "https://youtu.be/bte8Er0QhDg?si=99g_kZ_MXbkT1Ntt"),
                ("Article for Handwritten Digit Recognition", "https://www.analyticsvidhya.com/blog/2021/11/newbies-deep-learning-project-to-recognize-handwritten-digit/"),
                ("Article for Handwritten Digit Recognition", "https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html"),
            ]
        },
        "Spam Email Filter": {
            "description": "A classifier to detect spam emails.",
            "links": [
                ("YouTube Video", "https://www.youtube.com/watch?v=FkF2jhaRJIs&ab_channel=Simplilearn"),
                ("Article for Spam Email Filter", "https://github.com/topics/email-spam-filter"),
                ("Article for Spam Email Filter", "https://blog.logrocket.com/email-spam-detector-python-machine-learning/"),
            ]
        },
        "Movie Recommendation System": {
            "description": "A system that suggests movies to users based on their preferences.",
            "links": [
                ("YouTube Video", "https://www.youtube.com/watch?v=n3RKsY2H-NE&ab_channel=ArtoftheProblem"),
                ("Article on Label Your Data", "https://labelyourdata.com/articles/movie-recommendation-with-machine-learning"),
                ("Article on FreeCodeCamp", "https://www.freecodecamp.org/news/how-to-build-a-movie-recommendation-system-based-on-collaborative-filtering/"),
            ]
        },
    },
    "ML Engineering": {
        "Iris Flower Classification": {
            "description": "A model that classifies iris flowers into one of three species.",
            "links": [
                ("YouTube Video", "https://youtu.be/2yvE2z-cTi4?si=cIP4om25riCG8oz1"),
                ("Article for Iris Flower Classification", "https://data-flair.training/blogs/iris-flower-classification/"),
                ("Article for Iris Flower Classification", "https://github.com/amberkakkar01/IRIS-Flower-classification"),
            ]
        },
        "Stock Price Prediction": {
            "description": "Predicts stock prices using historical data.",
            "links": [
                ("YouTube Video", "https://www.youtube.com/watch?v=1O_BenficgE&ab_channel=Dataquest"),
                ("Article for Stock Price Prediction", "https://paperswithcode.com/task/stock-price-prediction"),
                ("Article for Stock Price Prediction", "https://neptune.ai/blog/predicting-stock-prices-using-machine-learning"),
            ]
        },
        "Sentiment Analysis on Movie Reviews": {
            "description": "Determines if a movie review is positive or negative.",
            "links": [
                ("YouTube Video", "https://www.youtube.com/watch?v=yK9Ya6KzVg&ab_channel=TheAI%26DSChannel"),
                ("Article for Sentiment Analysis", "https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews"),
                ("Article for Sentiment Analysis", "https://towardsdatascience.com/sentiment-analysis-a-how-to-guide-with-movie-reviews-9ae335e6bcb2"),
            ]
        },
    },
    "Quantitative Development": {
        "Algorithmic Trading Bot": {
            "description": "A bot that executes trades based on predefined algorithms.",
            "links": [
                ("YouTube Video", "https://www.youtube.com/watch?v=c9OjEThuJjY&ab_channel=NicholasRenotte"),
                ("Article for Algorithmic Trading Bot", "https://www.investopedia.com/articles/active-trading/081315/how-code-your-own-algo-trading-robot.asp"),
                ("Article for Algorithmic Trading Bot", "https://www.qmr.ai/examples-of-algorithmic-trading-strategies-trading-bots/"),
            ]
        },
        "Portfolio Optimizer": {
            "description": "A tool that optimizes the allocation of assets in an investment portfolio.",
            "links": [
                ("YouTube Video", "https://www.youtube.com/watch?v=OYrDkK5q5Lw&list=PLcFcktZ0wnNnqefRpFMS1k9_VlhVw7bzc&ab_channel=SigmaCoding"),
                ("Article for Portfolio Optimizer", "https://github.com/PyroQuant/Portfolio-Optimizer"),
                ("Article for Portfolio Optimizer", "https://builtin.com/data-science/portfolio-optimization-python"),
            ]
        },
        "Risk Management System": {
            "description": "A system that assesses and mitigates financial risks.",
            "links": [
                ("YouTube Video", "https://www.youtube.com/watch?v=-E4QMeCNvIE&list=PLgCR5H4IzggHyHw8dalrVHqHAqZfmTeWa&ab_channel=TheLogicofRisk"),
                ("Article for Risk Management System", "https://www.oreilly.com/library/view/machine-learning-for/9781492085249/ch01.html"),
                ("Article for Risk Management System", "https://wire.insiderfinance.io/risk-management-with-python-862eb4b885f8"),
            ]
        },
    }
}

# Define the colors and path to the JSON file
bg_color = '#D6EAF8'  # Light blue
text_color = '#1C2833'  # Dark blue
button_bg = '#AED6F1'  # Softer blue
button_fg = '#1C2833'  # Dark blue

status_file = "project_status.json"

def load_project_status():
    if os.path.exists(status_file):
        with open(status_file, 'r'):
            return json.load(file)
    return {}

def save_project_status(status):
    with open(status_file, 'w'):
        json.dump(status, file)

def calculate_deadlines(start_date, projects):
    deadlines = {}
    days_ahead = 7 - start_date.weekday()
    if days_ahead <= 0, days_ahead += 7
    next_monday = start_date + timedelta(days=days_ahead)
    current_date = next_monday
    for category in projects:
        for project in projects[category]:
            deadlines[project] = current_date.strftime("%d/%m/%Y")
            current_date += timedelta(weeks=1)
    return deadlines

current_date = datetime.strptime("11/04/2024", "%d/%m/%Y")
deadlines = calculate_deadlines(current_date, projects)

class ProjectListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Project List Display')
        self.geometry('800x600')
        self.configure(bg=bg_color)
        self.checked_projects = load_project_status()
        self.create_widgets()

    def toggle_completion(self, project_name, label):
        self.checked_projects[project_name] = not self.checked_projects.get(project_name, False)
        label.config(fg='green' if self.checked_projects[project_name] else text_color, text=f"{project_name} {'✔' if self.checked_projects[project_name] else ''}")
        save_project_status(self.checked_projects)

    def create_widgets(self):
        main_label = tk.Label(self, text="Gabriel's Project To-Do List", bg=bg_color, fg=text_color, font=('Helvetica', 20))
        main_label.pack(pady=20)

        for category, project_details in projects.items():
            frame = tk.LabelFrame(self, text=f"{category} Projects", bg=bg_color, fg=text_color, padx=10, pady=10)
            frame.pack(fill="both", expand=False, padx=50, pady=20)

            for project_name, details in project_details.items():
                project_frame = tk.Frame(frame, bg=bg_color)
                project_frame.pack(fill=tk.X, padx=20, pady=5)

                project_label = tk.Label(project_frame, text=project_name, bg=button_bg, fg=text_color, font=('Helvetica', 14))
                project_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

                check_var = tk.BooleanVar(value=self.checked_projects.get(project_name, False))
                chk_btn = tk.Checkbutton(project_frame, variable=check_var, bg=bg_color, 
                                         command=lambda project_name=project_name, project_label=project_label: self.toggle_completion(project_name, project_label))
                chk_btn.pack(side=tk.LEFT)

                btn = tk.Button(project_frame, text="Details", 
                                bg=button_bg, fg=button_fg, font=('Helvetica', 12), 
                                command=lambda name=project_name, details=details, deadline=deadlines[project_name]: self.open_project_detail(name, details["description"], deadline, details["links"]))
                btn.pack(side=tk.RIGHT, padx=10)

    def open_project_detail(self, name, description, deadline, links):
        detail_window = tk.Toplevel(self)
        detail_window.title(name)
        detail_window.configure(bg=bg_color)
        tk.Label(detail_window, text=f"{name} (Deadline: {deadline})", 
                  bg=bg_color, fg=text_color, font=('Helvetica', 16)).pack(pady=10)
        tk.Label(detail_window, text=description, 
                  bg=bg_color, fg=text_color, wraplength=400, justify="left").pack(pady=10)
        
        for text, url in links:
            link_label = tk.Label(detail_window, text=text, fg="blue", 
                                  cursor="hand2", bg=bg_color, font=('Helvetica', 12))
            link_label.pack()
            link_label.bind("<Button-1>", lambda e, url=url: webbrowser.open_new(url))

if __name__ == '__main__':
    app = ProjectListApp()
    app.mainloop()
