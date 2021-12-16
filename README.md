# Aprendizado não supervisionado para detecção de amaciamento em compressores herméticos alternativos



## Descrição

Método de aprendizado não supervisionado para detecção do estado de amaciamento em compressores herméticos alternativos para refrigeração. O algoritmo KMeans foi usado para agrupar dados de ensaios com compressores novos e já operados, buscando grandezas cuja divisão se adequasse à esperada devido ao amaciamento. O método "Elbow" foi utilizado para definir 3 como o número de grupos para agrupamento, e 120 combinações de parâmetros de pré-processamento foram avaliadas, buscando padrões que indiquem a detecção do fenômeno.

## Getting Started

### Pré-requisitos

* Anaconda



### Instalação

1. Clone o repositório
   ```sh
   git clone https://github.com/nicolasantero/compressor-breakin-kmeans-clustering.git
   ```
2. Crie um ambiente virtual (opcional)
   ```sh
   conda create -n name
   ```
3. Ativar ambiente virtual (opcional) 
   ```sh
   conda activate name
   ```
 4. Instalar os pacotes
   ```sh
   pip install requirements.txt
   ```
   
<p align="right">(<a href="#top">back to top</a>)</p>

### Executando os notebooks

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
