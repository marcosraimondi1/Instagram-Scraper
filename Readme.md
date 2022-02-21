<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/marcosraimondi1/Instagram-Scraper">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Instagram Web Scraper</h3>

  <p align="center">
    Instagram Web Scraper y procesamiento de datos
    <br />
    <a href="https://github.com/marcosraimondi1/Instagram-Scraper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#getting-started">View Demo</a>
    ·
    <a href="https://github.com/marcosraimondi1/Instagram-Scraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/marcosraimondi1/Instagram-Scraper/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#question-about-the-project">About The Project</a>
      <ul>
        <li><a href="#-built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#checkered_flag-getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites-triangular_flag_on_post">Prerequisites</a></li>
        <li><a href="#installation-wrench">Installation</a></li>
      </ul>
    </li>
    <li><a href="#fire-usage">Usage</a></li>
    <li><a href="#two_men_holding_hands-contributing">Contributing</a></li>
    <li><a href="#page_facing_up-license">License</a></li>
    <li><a href="#phone-contact">Contact</a></li>
    <li><a href="#sparkles-acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## :question: About The Project

![Product Name Screen Shot][product-screenshot]

Este es un proyecto de web scraping con python. El objetivo del programa es loguearse en instagram y obtener información acerca de los seguidores y seguidos del usuario. Crea dos archivos .csv donde se guarda la información. De los seguidores nos interesa saber si el usuario los sigue también; y de los seguidos si ellos también siguen al usuario.

### ⚙ Built With

- [Python](https://www.python.org)
- [Selenium](https://www.selenium.dev)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## :checkered_flag: Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites :triangular_flag_on_post:

This project was developed with Python 3.8.5, make shure you have python updated.

- version
  ```sh
  python --version
  ```

### Installation :wrench:

1. Clone the repo

   ```sh
   git clone https://github.com/marcosraimondi1/Instagram-Scraper.git
   ```

2. Create a virtual environment

   ```sh
   python -m venv c:\path\to\myenv
   ```

3. Activate Virtual Environment

   ```sh
   c:</path/to/myenv>/Scripts/activate
   ```

4. Install required packages
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## :fire: Usage

After installing all requirements follow this steps:

1. Start Program

   ```sh
   py scraper.py <username> <password>
   ```

   Where username is your instagram's username and password is your instagram's password

2. Chrome browser will initialize and the scraping will begin.

![Product Name Screen Shot][product-screenshot]

If the program fails to login or doesn't finish scraping, restart it.

3. The process may take a few minutes depending of the amount of followers/following. After it's done running, the browser will close and you should see 2 files generated with the data stored.

![Product Name Screen Shot2][product-screenshot2]

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## :two_men_holding_hands: Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## :page_facing_up: License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## :phone: Contact

Marcos Raimondi - [@marcos-raimondi](https://www.linkedin.com/in/marcos-raimondi/) - marcosraimondi1@gmail.com

Project Link: [https://github.com/marcosraimondi1/Instagram-Scraper](https://github.com/marcosraimondi1/Instagram-Scraper)

<!-- ACKNOWLEDGMENTS -->

## :sparkles: Acknowledgments

- [Selenium](https://www.selenium.dev)
- [Pandas](https://pandas.pydata.org)
- [Tutorial](https://youtu.be/Z8jhFLpk_S4)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/marcosraimondi1/Instagram-Scraper.svg?style=for-the-badge
[contributors-url]: https://github.com/marcosraimondi1/Instagram-Scraper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/marcosraimondi1/Instagram-Scraper.svg?style=for-the-badge
[forks-url]: https://github.com/marcosraimondi1/Instagram-Scraper/network/members
[stars-shield]: https://img.shields.io/github/stars/marcosraimondi1/Instagram-Scraper.svg?style=for-the-badge
[stars-url]: https://github.com/marcosraimondi1/Instagram-Scraper/stargazers
[issues-shield]: https://img.shields.io/github/issues/marcosraimondi1/Instagram-Scraper.svg?style=for-the-badge
[issues-url]: https://github.com/marcosraimondi1/Instagram-Scraper/issues
[license-shield]: https://img.shields.io/github/license/marcosraimondi1/Instagram-Scraper.svg?style=for-the-badge
[license-url]: https://github.com/marcosraimondi1/Instagram-Scraper/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/marcos-raimondi
[product-screenshot]: images/main.jpg
[product-screenshot2]: images/files.jpg
