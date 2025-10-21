# Uno-Reverse: Hackathon Winning Prediction 🏆

A machine learning project designed to forecast the success potential of hackathon ideas using historical data and predictive modeling.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-Required-green.svg)](https://nodejs.org/)

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Repository Structure](#repository-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

Uno-Reverse leverages machine learning to help hackathon teams make data-driven decisions about their project ideas. By analyzing historical hackathon data, the model predicts the winning potential of ideas, enabling teams to select high-impact concepts and optimize their strategies.

| Detail | Description |
|--------|-------------|
| **Role** | ML Developer |
| **Technologies** | Python, Node.js, JavaScript, VS Code |
| **Date** | March 2024 |
| **Model Accuracy** | 87% on validation data |

## ✨ Key Features

- **🤖 Predictive Modeling**: Linear regression model trained to identify high-potential hackathon ideas
- **📊 High Accuracy**: Achieved 87% accuracy on validation dataset
- **📈 Comprehensive Analysis**: Analyzed 5,000+ past hackathon entries to extract success patterns
- **🎯 Scoring Algorithm**: Custom scoring system (0-100 scale) for strategic decision-making
- **🌐 Web Interface**: User-friendly interface for submitting ideas and viewing predictions
- **⚡ Real-time Predictions**: Fast API-based prediction serving

## 🛠 Technologies Used

### Backend
- **Python 3.x** - Machine learning model development
- **scikit-learn** - Linear regression implementation
- **pandas** - Data analysis and preprocessing
- **Node.js** - API server

### Frontend
- **HTML/CSS** - User interface
- **JavaScript** - Client-side logic and API integration

## 📁 Repository Structure

```
Uno-reverse/
├── py files/              # Python scripts for ML model
│   ├── script2.py
│   ├── script3.py
│   └── industrylabel.py
├── js/                    # JavaScript files
│   └── fetch.js
├── server.js              # Node.js API server
├── index2.html            # Main web interface
├── demo-seo-agency-*.html # Additional frontend pages
├── frequent.json          # Configuration data
├── googlesearch.json      # Search data
├── test2.json             # Test data
├── requirements.txt       # Python dependencies
├── package.json           # Node.js dependencies
├── LICENSE                # Project license
└── README.md              # This file
```

## 🚀 Installation & Setup

### Prerequisites

Ensure you have the following installed:
- Python 3.x ([Download](https://www.python.org/downloads/))
- Node.js ([Download](https://nodejs.org/))
- pip (Python package manager)
- npm (Node package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Agamdeep555/Uno-reverse
cd Uno-reverse
```

### Step 2: Backend Setup (Python ML Model)

Install required Python dependencies:

```bash
pip install -r requirements.txt
```

Run initial data processing scripts:

```bash
python industrylabel.py
# Run other necessary scripts as needed
```

### Step 3: Server Setup (Node.js API)

Install Node.js dependencies:

```bash
npm install
```

Start the server:

```bash
node server.js
```

The server should now be running on `http://localhost:3000` (or configured port).

### Step 4: Access the Web Interface

Open your browser and navigate to:
```
http://localhost:3000/index2.html
```

Or directly open `index2.html` in your browser if configured for static serving.

## 💻 Usage

1. **Input Your Idea**: Enter your hackathon project details through the web interface
2. **Get Prediction**: The ML model analyzes your submission against historical data
3. **Review Score**: Receive a score (0-100) indicating winning potential
4. **Make Decisions**: Use insights to refine your idea or pivot to alternatives

## 📊 Model Performance

- **Training Dataset**: 5,000+ historical hackathon entries
- **Algorithm**: Linear Regression
- **Validation Accuracy**: 87%
- **Scoring Range**: 0-100 (higher scores indicate better winning potential)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Areas for Contribution
- Improving model accuracy with advanced algorithms
- Expanding the dataset
- Enhancing the user interface
- Adding visualization features
- Performance optimization

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

This project was developed by a collaborative team:

- **Agamdeep Singh** - [@Agamdeep555](https://github.com/Agamdeep555)
- **Vedant Anand**
- **Arpit Goyal**
- **Manpreet Singh**
- **Dhwani**

## 🙏 Acknowledgments

- Thanks to all hackathon organizers who made their data available
- Inspired by the need for data-driven decision making in hackathons

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
