![PhotoShow](images/Logo.png)

Welcome to PhotoShow, your go-to Tkinter-based photo manager app! 📸

### Table of Contents 📋

- [About PhotoShow](#about-photoshow-💡)
- [Key Features](#key-features-🔑)
- [Data Architecture](#data-architecture-📊)
- [Getting Started](#getting-started-🚀)
- [Dependencies](#dependencies-📦)

### About PhotoShow 💡

PhotoShow is a user-friendly desktop application developed with Tkinter, designed to simplify and enhance your photo management experience. This lightweight yet powerful app allows you to organize, view, and cherish your memories right from your desktop.

### Key Features 🔑

`User-Friendly Interface`: Enjoy a clean and intuitive Tkinter interface, making navigation and photo management a breeze.

`Album Creation`: Easily organize your photos into personalized albuns, keeping your memories neatly sorted.

`Themed Collections`: Discover themed collections such as Travel Adventures, Nature, Sports, and Art, intelligently categorized for a more enjoyable browsing experience.

`Threaded Comments`: Engage with others and share your thoughts on photos. The threaded comment feature allows for meaningful discussions, turning your memories into shared experiences.

### Data Architecture 📊

![Data Architecture](images/modelo_dados.png)

The data architecture of PhotoShow is based on the relational database, with the following entities:

`users`: stores the user's data, such as username, password, and email.

`photos`: stores the photo's data, such as the photo's name, path, and date.

`comments`: stores the comment's data, such as the comment's text, date, and the user who made the comment.

`categories`: stores the category's data, such as the category's name and description.

`favorites`: stores the user's favorite albums.

`albuns`: stores the album's data, such as the album's name and the user who created the album.

`notifications`: stores the notification's data, by is type , content and the user who receive(d) the notification.

### Getting Started 🚀

- To get started, simply clone this repository to your machine
  in your terminal using the following command:

```bash
git clone
```

- Ensure that you have the py version updated to Python `3.11.5` or higher.

```bash
python --version
```

if not then update the python version using the following command:

```bash
python -m pip install --upgrade pip
```

#### Dependencies 📦

PhotoShow requires only one dependency, `Pillow`, which can be installed using the following command:

```bash
pip install Pillow
```

`!! Note`: Without the `Pillow` dependency, the app may crash when trying to display images.

- Then run the following command in the `terminal` to start the app:

```bash
python main.py
```
## Remember that you should run the terminal inside the directory of the app, atleast to run the app.

### THAT'S IT! 🎉 Now you can enjoy PhotoShow and all its features!

Author: [Pedro Teixeira](https://github.com/pedromst2000)
