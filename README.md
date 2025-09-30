

# NLP_COMS_579

RAG - Natural Language Processing Project for the COMS_579 in Spring 2024

<br/>

This project demonstrates how to upload and index PDF files in a Weaviate vector database using LlamaIndex. The project includes a script (upload.py) that chunks the content of PDF files, embeds them using a pre-trained language model, and stores the resulting vectors in Weaviate.

<br/>

## Final Video Link

<a href="https://www.youtube.com/watch?v=6wr_hAHiYNs" target="_blank">RAG System User Interface</a>

## Final Video Link

[![RAG System User Interface](https://img.youtube.com/vi/6wr_hAHiYNs/maxresdefault.jpg)](https://www.youtube.com/watch?v=6wr_hAHiYNs)


## Dockerization of the Project
The initial step involved containerizing the project using Docker to ensure consistency across different development and production environments.

<img width="416" alt="image" src="https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/0dbd709a-f6b9-4359-9848-b8f6c11b45c9">
<img width="408" alt="image" src="https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/0f28a51a-3af6-4120-b73d-d636b0658fcd">


## Server Acquisition and Deployment
  - Purchased a Ubuntu VPS (Virtual Private Server).
  - Deployed the Dockerized project on this server for testing and production.
<img width="468" alt="image" src="https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/ced8e6a9-4c14-4289-85f7-bddaecabb1fa">


## CI/CD Integration
  - Set up Continuous Integration and Continuous Deployment (CI/CD) pipelines on GitHub.
  - Configured automated deployments to streamline development workflows and enhance deployment efficiency.

<img width="468" alt="image" src="https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/f02124f5-4b84-44c1-a7de-824715138796">
<img width="468" alt="image" src="https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/2a0cb538-995d-4ee3-91db-c41fc78b0364">

## Docker Hub Integration
  - Created a new repository on Docker Hub to store Docker images.
  - Linked this repository to our VPS using secret variables in GitHub, which included Docker Hub credentials (username, password) and URL.
<img width="468" alt="image" src="https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/9d26c6f7-994d-489a-bc96-c1cde303b7cd">

## Security and Access Configuration
  - Configured additional repository secrets on GitHub to establish a secure SSH connection to the VPS, enabling safe access and management of the server directly from GitHub workflows.
<img width="468" alt="image" src="https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/47dd3bec-d00f-4e2c-bd20-a71bc475029f">



## Setup
1. Copy the `.env.example` file to a new file named `.env`.
2. Fill in the `WCS_CLUSTER_URL` and `WCS_API_KEY` values in the `.env` file with your own Weaviate cluster URL and API key.


## Running the Container

To run the Docker container with the default settings, use the following command:

```bash
docker-compose up --build
```

If you want to specify a different PDF file, you can set the PDF_FILE environment variable when running the container. For example, to use a file named Documents/SAM.pdf, use the following command:

```bash
PDF_FILE=Documents/SAM.pdf docker-compose up --build
```


## Demo 1 Video Link

<a href="https://www.youtube.com/watch?v=EDFlHy-BuIw" target="_blank">Watch the Demo 1 Video</a>

## Set up a virtual environment OpenAI
Running the command below will create a virtual environment named "openai-env" inside the current folder you have selected in your terminal / command line:
```bash
python -m venv openai-env
```

Once you’ve created the virtual environment, you need to activate it. On Windows, run:

```bash
openai-env\Scripts\activate
```

On Unix or MacOS, run:
```bash
source openai-env/bin/activate
```


## Running the Query
To run the Query part and ask question, use the following command:
```bach
python -W ignore  query.py --question="What is SAM?"
```
or
```bash
python -W ignore  query.py --question="What is Mask ambiguity? write the answer in 10 words"
```

## Demo 2 Video Link

<a href="https://www.youtube.com/watch?v=2Qbox0ks6fA/" target="_blank">Watch the Demo 2 Video</a>

<br/>
<br/>

### Contributors

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/banisharifm>
            <img src=https://avatars.githubusercontent.com/u/41099498?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=BanisharifM/>
            <br />
            <sub style="font-size:14px"><b>Mahdi Banisharif</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Sadegh-Jafari>
            <img src=https://avatars.githubusercontent.com/u/155206906?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Sadegh-Jafari Harrington/>
            <br />
            <sub style="font-size:14px"><b>Sadegh Jafari</b></sub>
        </a>
    </td>
</tr>
</table>
