<h1 align="center" style="color:#5e54ac; font-weight:bold;">
     <img 
    src="https://user-images.githubusercontent.com/42190754/111989222-42a7a800-8af0-11eb-97cb-e1dc5a79279e.png"
    float="center"
    width="100" height="100"
    />
    <br/>
  Weather API
</h1>

<p align="center">
 <a href="#ℹ%EF%B8%8F-about">About</a> •
 <a href="#-how-it-works">How it works</a> •
 <a href="#-authors">Authors</a> •
 <a href="#-license">License</a>
</p>

## ℹ️ About

API Restful to obtain data temperature and humidity from the website [The Weather Channel](https://weather.com/), using stack with Python and Flask. And send to the [prediction service](https://github.com/BiaChacon/prediction-service).

---

## 🚀 How it works

### 👉 Pre-requisites

Before you begin, you will need to have the following tools installed on your machine: [Git](https://git-scm.com), [python](https://www.python.org/) and [pip](https://pypi.org/project/pip/). In addition, it is good to have an editor to work with the code like [VSCode](https://code.visualstudio.com/).

#### 🏁 Start

```bash
# Clone this repository
$ git clone https://github.com/BiaChacon/weather-api.git

# Access the project folder cmd/terminal
$ cd weather-api
```

#### 🎲 Running the server

```bash
# go to the api folder
$ cd src

# install the dependencies
$ pip install requirements.txt

# Run the application
$ python app.py

# The server will start at port: 5000 - go to http://localhost:5000
```

#### 🌡Get data

```bash
# go to the project folder
$ cd weather-api

#Run the application
$ python send_data.py
```

---

## 👩🏽‍💻 Authors

<table>
  <tr>
    <td align="center"><a href="https://github.com/biachacon"><img src="https://avatars1.githubusercontent.com/u/42190754?s=460&u=a5cbe42a4868b2bac9615226044b9cec15cee418&v=4" width="100px;" alt=""/><br /><sub><b>Bia Chacon</b></sub></a><br /><a href="https://github.com/BiaChacon/weather-api" title="Code">💻</a></td>
  <tr>
</table>

---

## 📝 License

This project is under MIT. See at here [LICENSE](https://github.com/BiaChacon/weather-api/blob/main/LICENSE) for more information.

---
