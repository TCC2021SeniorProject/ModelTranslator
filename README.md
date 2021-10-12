
<!-- PROJECT LOGO -->
<br /></br>
<div align="center">
  <img src="img/title.png">  
</div>
<div align="center">  
  <!-- PROJECT SHIELDS -->
  <p align="center">
    </br>
    <img alt="Carthage compatible" src="https://img.shields.io/badge/Status-Under_development-blue" />
    <img alt="Carthage compatible" src="https://img.shields.io/badge/Stability-Unstable-red" />
    <img alt="Carthage compatible" src="https://img.shields.io/badge/Documentation-not ready-red" />
  </p>
  
  <h3 align="center">MODEL TRANSLATOR</h3>
  <div align="center">
     <a href="">
      <img src="img/icon/translatorColorIcon.png" alt="Logo" width="80" height="80">
    </a>
  </div>
  </br>
  <p align="center">
    Translate XML model into Python code
    <br />
    <a href="https://tcc2021seniorproject.github.io/"><strong>Visit our website for full documentation »</strong></a>
    <br />
    <br />
    <a href="https://docs.google.com/document/d/e/2PACX-1vRTo8ReSNkiQpujZEZgLHO4aHVmF3FWq7vQh247OKN9kj_EMBtQf2SMMnxD8Yfgk-3zjVv4AAqBx-2o/pub">View current process</a>
    ·
    <a href="https://github.com/TCC2021SeniorProject/ModelTranslator/issues">Report Bug</a>
    ·
    <a href="https://github.com/TCC2021SeniorProject/ModelTranslator/issues">Request Feature</a>
  </p>
</div>
</br>
</br>


## TABLE OF CONTENTS
<ol>
  <li>
    <a href="#about-the-project">About The Project</a>
  </li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a>
      </li>
    </ul>
  </li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#roadmap">Roadmap</a></li>
  <li><a href="#testing-schedules">Testing Schedules</a></li>
  <li><a href="#license">License</a></li>
  <li><a href="#contact">Contact</a></li>
</ol>

<!-- ABOUT THE PROJECT -->
## About The Project

This project will assist developers on establishing IoT system.

Here's why you should use this:
* Users who wants to design automata with UPPAAL but has no idea what to do with the generated XML file.
* Users who wants their modeled diagrams runs on RaspPi device.
* Users who wants to test out IoT environment with the modeling tool(UPPAAL).


<p align="right">(<a href="#top">back to top</a>)</p>


### Tools Used With


* [UPPAAL](https://uppaal.org/)
* [Python](https://www.python.org/)
* [VS CODE](https://code.visualstudio.com/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Knowledgement of UPPAAL model diagram is required.
* npm
  ```sh
  
  ```

### Demo Installation

1. Clone the repo
   ```sh
   git clone https://github.com/TCC2021SeniorProject/ModelTranslator.git
   ```
2. Download XML examples
   ```sh
   
   ```
3. Run Main.py program
   ```sh
   
   ```

### Result of running XML_parser.py

0. When you produce a model such like this in UPPAAL
  <div align="center">
    <img width="500" src="img/UPPAAL_simple_model.png">  
  </div>

1. Suppose there is a XML file given like this

   ```
   <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE nta PUBLIC '-//Uppaal Team//DTD Flat System 1.1//EN' 'http://www.it.uu.se/research/group/darts/uppaal/flat-1_2.dtd'>
    <nta>
      <declaration>// Place global declarations here.</declaration>
      <template>
        <name x="5" y="5">Template</name>
        <declaration>// Place local declarations here.</declaration>
        <location id="id0" x="-85" y="-76">
          <name x="-95" y="-110">Start</name>
        </location>
        <location id="id1" x="153" y="-76">
          <name x="143" y="-110">Do</name>
        </location>
        <location id="id2" x="374" y="-76">
          <name x="364" y="-110">End</name>
        </location>
        <init ref="id0"/>
        <transition>
          <source ref="id1"/>
          <target ref="id2"/>
        </transition>
        <transition>
          <source ref="id0"/>
          <target ref="id1"/>
        </transition>
      </template>
      <system>// Place template instantiations here.
    Process = Template();
    // List one or more processes to be composed into a system.
    system Process;
        </system>
      <queries>
        <query>
          <formula></formula>
          <comment></comment>
        </query>
      </queries>
    </nta>
   ```

2. After running XML_parser, this will parse crutial data to graph objects. Below image is output lines as a result of conversion

</br>
<div align="center">
  <img src="img/XML_to_graph.png">  
</div>

3. Then the parser automatically checks all the required data such as a starting state, an end state, infinity, and connectionless transitions.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


_For more examples, please refer to the [Design Documentation](https://docs.google.com/document/d/e/2PACX-1vQ0GhSxaPt2g3zVoJ4P_tEIz-wvtw0bt5sdaG9b234H0Y10dJu01ctV5YPrfZKCXZp57UvUPH7nJ3qQ/pub)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

_For more plans, please see the [plan documentation](https://drive.google.com/file/d/1UHxCx8l3Wgu_6PQxfjx6K0d7gkP5ybov/view)_

### Task 1 check list - Due October 16.
- [x] Update mark down documentation.
- [x] Make UPPAAL parser.
- [ ] Program is able to traverse all the nodes through tranistion objects.
- [ ] Program is able to identify the validity of the model.
- [ ] Program is able to validate the node function (e.g. starting node, termination node, logic node, process node, etc)
- [ ] Make Python code generator/converter.
- [ ] Test simple diagram.


### Task 2 check list - Due October 23.
- [ ] Make complex diagram 1
- [ ] Update(enhance) UPPAAL parser
- [ ] Update(enhance) Python code generator/converter
- [ ] Test complex diagram 1

### Task 3 check list - Due October 23.
- [ ] Make complex diagram 2
- [ ] Update(enhance) UPPAAL parser
- [ ] Update(enhance) Python code generator/converter
- [ ] Test complex diagram 2

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

</br>

## Testing Schedules

</br>
<div align="elft">
  <img width="500px" src="img/testSchedule.png">  
</div>
</br>

To view the specific testing details, **[click here](https://docs.google.com/document/d/e/2PACX-1vQC5scu0DfEu0nLqPVWZzML1m6oMh8Q2Oo86GEyt_GFx_NB7BA3BZWF44hMv6tEFyhgTrATsf8TUQL3/pub)**

*MCCD* refers to Main Control Center Device.

- [ ] Task case 1 (Due Oct  9): Produce code from a simple model
- [ ] Task case 2 (Due Oct 17): Model comparatively massive size diagram
- [ ] Task case 3 (Due Oct 23): Build infinite loops / Redundant transitions.
- [ ] Task case 4 (Due Nov 21): Change models to python codes that MCCD accepts.
- [ ] Task case 5 (Due Oct 10): Simple signalling to the device
- [ ] Task case 6 (Due Oct 24): Complex signalling to the device
- [ ] Task case 7 (Due Dec 12):	Handling devices via web application on MCCD
- [ ] Task case 8 (Due Dec 12): MCCD can be postponed until the device finishes its current job


<p align="right">(<a href="#top">back to top</a>)</p>


## Coding Style Convention

**See the following link: [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)**

**Follow rules for better readability: [Clean Code by Robert C. Martin](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29)**
</br>


<!-- LICENSE -->
## License

Currently there is no license for this repo meaning our team retain all rights to the source code and no one may reproduce, distribute, or create derivative works from our work.

This will not be permanent until the completion of the project.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

#### Director
>  Dr. Siddhartha Bhattacharyya </br>
email:[sbhattacharyya@fit.edu](sbhattacharyya@fit.edu)

#### Developers
> Sung-Jun Baek </br>
email:[roni2006@hanmail.net](roni2006@hanmail.net) </br>
GitHub Link: [https://github.com/MarcoBackman](https://github.com/MarcoBackman)

> Caelan Shoop </br>
email:[cshoop2018@my.fit.edu](cshoop2018@my.fit.edu)

> Cameron Wright </br>
email:[cameron2018@my.fit.edu](cameron2018@my.fit.edu)


<p align="right">(<a href="#top">back to top</a>)</p>
