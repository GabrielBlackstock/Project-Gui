# Project List Display Application

## Overview
This is a Python-based GUI application built with Tkinter. It serves as a simple project management tool where users can view and track the progress of various software engineering, AI engineering, machine learning, and quantitative development projects. It allows users to mark projects as completed, see project details, and find relevant resources for each project.

## Features
- **Project Organisation**: Projects are categorised by discipline, allowing users to easily navigate through them.
- **Completion Tracking**: Users can mark projects as completed by ticking a checkbox.
- **Project Details**: Provides detailed information about each project, including a brief description, deadlines, and links to additional resources.
- **Interactive GUI**: The application has a user-friendly interface, with clickable links and buttons for detailed project information.

## Dependencies
- Python 3
- Tkinter (comes pre-installed with most Python installations)
- JSON (used to save and load project statuses)
- Webbrowser (for opening project-related links in a web browser)

## Installation
1. Clone the repository or download the source code.
2. Ensure you have Python 3 installed on your system.
3. Open a terminal in the project directory and run the application with `python project_list.py`.

## Usage
1. Launch the application.
2. View the project categories and individual projects within each category.
3. Tick the checkbox next to a project to mark it as complete.
4. Click the "Details" button to view more information about a project, including relevant resources like YouTube videos and articles.
5. To view additional resources, click on the link text, which will open in your default web browser.

## Customisation
- You can modify the list of projects in the `projects` dictionary to add, remove, or update projects.
- The colour scheme and other GUI-related attributes can be adjusted by changing the relevant variables in the code (e.g., `bg_color`, `text_color`, `button_bg`, `button_fg`).
- If you wish to change the default deadline calculation logic, modify the `calculate_deadlines` function.
