# LLM Tutorial at WAW ML 2024

Authors: Diaoule Diallo, Roxanne El Baff, Dominik Opitz, Peer Schütt 

Corresponding Author: Peer Schütt (peer.schuett at dlr.de)

We want to do a hands-on tutorial with you at the WAW, and therefore we require you to install some software beforehand! We will be using a locally running LLM and doing the coding exercises in Jupyter notebooks.

## Local LLM:  
We will be using LM Studio (https://lmstudio.ai/). We provide a PDF with installation instructions [LM_Studio_Install_Instruct.pdf](LM_Studio_Install_Instruct.pdf), a short introduction to LM Studio, and explanations of the model we want to use. Please read the PDF, download the specified LLM model and have LM Studio up and running. For some part of the tutorial you are able to use the Mistral API to get a better performance, but this is an optional choice. If you would like to use that, sign Up here (https://docs.mistral.ai/getting-started/quickstart/#account-setup). But all parts are doable with LM Studio.

## Python Environment:  
We also provide a ``requirements.txt`` with all the necessary Python packages. With that, you can create a conda/mamba environment for the tutorial:

```
conda init powershell  # only for Windows users - requires terminal restart
conda activate 
mamba create -n waw_ml python=3.10  # mamba/conda depending on what you use
conda activate waw_ml
pip install -r requirements.txt
```

## Tutorial notebooks:  
The jupyter notebooks are/will be on Monday in the the respective folders.
