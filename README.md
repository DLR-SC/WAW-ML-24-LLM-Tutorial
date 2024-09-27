# Techniques for Using LLMs Effectively: An Introduction to Prompt Engineering, Retrieval Augmented Generation, and Toolformer

Authors: Diaoule Diallo, Roxanne El Baff, Dominik Opitz, Peer Schütt 

Corresponding Author: Peer Schütt (peer.schuett at dlr.de)

In this hands-on tutorial, you'll learn the latest techniques in Prompt Engineering, how to steer Large Language Models (LLMs) efficiently using Retrieval Augmented Generation (RAG), and Toolformer, a recent method to enrich LLMs with information from external tools. You'll be able to set up your own local LLM model and apply these techniques to sample tasks. Ideally, you can use this knowledge straight away to tackle your own challenges, whether in research or administration.

This tutorial was prepared for the WAW ML 2024.

## Plan for the tutorial:  

Each of the three tutorial parts has a dedicated folder with instructions. The tutorial is planned to be completed in four steps:      
1) LM Studio & Python Setup
2) Prompt Engineering
3) Retrieval Augmented Generation (RAG)
4) Toolformer

## LM Studio Setup:  
We will be using LM Studio (https://lmstudio.ai/). We provide a PDF with installation instructions [LM_Studio_Install_Instruct.pdf](LM_Studio_Install_Instruct.pdf), a short introduction to LM Studio, and explanations of the model we want to use. **Please read the PDF, download the specified LLM model and have LM Studio up and running**. For some part of the tutorial you are able to use the Mistral API to get a better performance, but this is an optional choice. If you would like to use that, sign Up here (https://docs.mistral.ai/getting-started/quickstart/#account-setup). But all parts are doable with LM Studio.

## Python Setup:  
We also provide a ``requirements.txt`` with all the necessary Python packages. With that, you can create a conda/mamba environment for the tutorial:

```
conda init powershell  # only for Windows users - requires terminal restart
conda activate 
mamba create -n waw_ml python=3.10  # mamba/conda depending on what you use
conda activate waw_ml
pip install -r requirements.txt
```

