# Unsupervised learning for [running-in](https://en.wikipedia.org/wiki/Break-in_(mechanical_run-in)) detection in hermetic alternative compressors



## Description

Data exploration and application of an unsupervised learning method to aid in the detection of the running-in state in hermetic alternative refrigerant compressors. 

The KMeans algorithm was used to group test data with samples of new and already operated compressors, searching for magnitudes whose division matched the expected running-in condition. The "Elbow" method was used to define 3 as the number of groups for clustering, and 120 combinations of preprocessing parameters were evaluated, looking for patterns that indicate detection of the phenomenon.

Translated with www.DeepL.com/Translator (free version)

## Getting Started

### Pre-requisites

* Anaconda
* Git



### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/nicolasantero/compressor-breakin-kmeans-clustering.git
   ```
2. Create a virtual environment (optional)
   ```sh
   conda create -n name
   ```
3. Activate Virtual Environment (optional) 
   ```sh
   conda activate name
   ```
 4. Installing Packages
   ```sh
   pip install requirements.txt
   ```
   
<p align="right">(<a href="#top">Início</a>)</p>

### Running the notebooks
```
jupyter notebook
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">Início</a>)</p>
