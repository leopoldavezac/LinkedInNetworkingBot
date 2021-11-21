# NetworkingBot

![GitHub repo size](https://img.shields.io/github/repo-size/leopoldavezac/LinkedInNetworkingBot)
![GitHub contributors](https://img.shields.io/github/contributors/leopoldavezac/LinkedInNetworkingBot)
![GitHub stars](https://img.shields.io/github/stars/leopoldavezac/LinkedInNetworkingBot?style=social)
![GitHub forks](https://img.shields.io/github/forks/leopoldavezac/LinkedInNetworkingBot?style=social)

NetworkingBot is a bot to let you expand your network while you sleep. It send requests for you to your school's alumnis that work in your sector.  

## Prequistes

- Google Chrome installed
- Linkedin Account
- Python 3 or higher

## Installation

```bash

$ path/to/this/dir pip install -e .

```

## Using NetworkingBot


- Download a [chromedriver](https://chromedriver.chromium.org/downloads), and place the .exe file in your clone version of this repo. Make sure the version match your browser version.
- Find your school code (cf. bellow).
- Update the config.yaml with your linkedin li_at cookie (cf. bellow), school code and job title.
- Run the script once a day. Due to linkedin scrapping restrictions you can only send 80 connections a day.

```bash

$ path/to/this/dir network

```

### Getting LI_AT

1.  Navigate to www.linkedin.com and log in
2.  Open browser developer tools (Ctrl-Shift-I or right click -> inspect
    element)
3.  Select the appropriate tab for your browser (**Application** on Chrome,
    **Storage** on Firefox)
4.  Click the **Cookies** dropdown on the left-hand menu, and select the
    `www.linkedin.com` option
5.  Find and copy the li_at **value**

### How to find your school code

1. Open Linkedin & log in
2. Click enter in the search bar (left it empty)
3. Click on "All filters"
4. Scroll down to the School section
5. Click on "Add a school"
6. Type in your school name
7. Click Show results
8. You can find your school code in the page url 
(ex: https:<area>//www<area>.linkedin.com/search/results/people/?origin=FACETED_SEARCH&schoolFilter=%5B%"**12434**"%5D&sid=FW2, school code is 12434)

## Contact

If you want to contact me you can reach me at leopoldavezac@gmail.com.

## Licence

This project use the following licence, [MIT](./LICENCE)


