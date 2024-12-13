<a id="readme-top"></a>
<!-- README TEMPLATE -->
<!--
*** https://github.com/othneildrew/Best-README-Template
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]


<h3 align="center">Raspberry Pi Game Project</h3>

  <p align="center">
    a Raspberry Pi Game with GPIO support created by Yanic and Nils for school
    <br />
    <a href="https://github.com/Blitzyanic/RaspberryPi-Game-Project/tree/main/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Blitzyanic/RaspberryPi-Game-Project/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Blitzyanic/RaspberryPi-Game-Project/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

this repo is a pygame [TODO: arcade game] clone for the raspberry pi with GPIO controls 

```
- made for school
- fork but not push to base project
- some elements might be in german
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
<img src="https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python&logoColor=yellow" />
<img src="https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white" />
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python
* virtualenv (for python)
* raspberry pi 4 B or 5 B
* jump wires
* 3x LED
* 3x 220 Ohm resistor
* 1x Button module
* 1x Joystick module
* 1x Breadboard
* 1x PCF8591 ADC module
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/Blitzyanic/RaspberryPi-Game-Project.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] add Game
- [ ] add Raspberry Pi GPIO support
  - [ ] add Joystick support
  - [ ] add Button support
  - [ ] add LED support

Optional:
- [ ] add title screen

See the [open issues](https://github.com/Blitzyanic/RaspberryPi-Game-Project/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Top contributors:

<a href="https://github.com/Blitzyanic/RaspberryPi-Game-Project/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Blitzyanic/RaspberryPi-Game-Project" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the GNU GENERAL PUBLIC LICENSE V3. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Yanic - yanic.dev@gmail.com - https://github.com/Blitzyanic

Nils  - [@puckiiOLykos](https://x.com/puckiiOLykos) - https://github.com/derpuckii

Project Link: [https://github.com/Blitzyanic/RaspberryPi-Game-Project](https://github.com/Blitzyanic/RaspberryPi-Game-Project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Blitzyanic/RaspberryPi-Game-Project.svg?style=for-the-badge
[contributors-url]: https://github.com/Blitzyanic/RaspberryPi-Game-Project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Blitzyanic/RaspberryPi-Game-Project.svg?style=for-the-badge
[forks-url]: https://github.com/Blitzyanic/RaspberryPi-Game-Project/network/members
[stars-shield]: https://img.shields.io/github/stars/Blitzyanic/RaspberryPi-Game-Project.svg?style=for-the-badge
[stars-url]: https://github.com/Blitzyanic/RaspberryPi-Game-Project/stargazers
[issues-shield]: https://img.shields.io/github/issues/Blitzyanic/RaspberryPi-Game-Project.svg?style=for-the-badge
[issues-url]: https://github.com/Blitzyanic/RaspberryPi-Game-Project/issues
[license-shield]: https://img.shields.io/github/license/Blitzyanic/RaspberryPi-Game-Project.svg?style=for-the-badge
[license-url]: https://github.com/Blitzyanic/RaspberryPi-Game-Project/blob/master/LICENSE.txt
[product-screenshot]: docs/img/sample.png
