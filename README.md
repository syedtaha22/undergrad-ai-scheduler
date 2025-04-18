# Undergrad-AI-Scheduler

**Undergrad-AI-Scheduler** is an AI-powered web application designed to assist undergraduate students at IBA in generating personalized course schedules based on individual constraints and preferences. It leverages Constraint Satisfaction Problem (CSP) techniques to automate and optimize the course selection and scheduling process.

---

## Project Overview

Course registration often presents challenges when students must consider multiple overlapping constraints, such as:

- Preferred instructors  
- Specific course requirements  
- Time-of-day preferences  
- Desired breaks or compact schedules  
- Conflict-free course combinations  

This project allows students to specify such constraints through an interactive interface, and the backend AI system generates valid and optimized timetables based on those preferences.

Initially, this system is being developed specifically for students of the Institute of Business Administration (IBA), with potential for generalization to other academic institutions in the future.

---

## Features

- Constraint-based course scheduling using CSP  
- User-friendly frontend for specifying preferences  
- Multiple valid scheduling options generated automatically  
- Backend validation to ensure feasibility of generated timetables  
- Extensible architecture for future modules and institutional support  

---

## Technology Stack

| Component        | Technology                        |
|------------------|-----------------------------------|
| Frontend         | React.js                          |
| Backend / API    | Python                            |
| AI Logic         | Python (CSP-based implementation) |
| Deployment       | To be determined                  |

---

## Directory Structure

```
undergrad-ai-scheduler/
│
├── ai_engine/            # AI logic and CSP implementation
├── api/                  # Backend logic and request handlers
├── data_models/          # Python classes for course, teacher, and user constraints
├── frontend/             # React frontend application
├── configs/              # Configuration files
├── scripts/              # One-off scripts (e.g., data preprocessing)
├── tests/                # Unit and integration tests
└── README.md             # Project documentation
```

---

## Development Status

The project is in active development. The AI scheduling engine and frontend interface are being built in parallel. This repository will be updated frequently as modules are developed, tested, and integrated.

---

## Contributing

Please refer to the [Contributing Guidelines](CONTRIBUTING.md) for detailed instructions on how to contribute to this project, including branch naming, commit message formats, directory structure, and code review policies.
