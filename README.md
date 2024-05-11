

# NLP_COMS_579

RAG - Natural Language Processing Project for the COMS_579 in Spring 2024

<br/>

This project demonstrates how to upload and index PDF files in a Weaviate vector database using LlamaIndex. The project includes a script (upload.py) that chunks the content of PDF files, embeds them using a pre-trained language model, and stores the resulting vectors in Weaviate.

<br/>

## Final Video Link

<a href="https://www.youtube.com/watch?v=6wr_hAHiYNs" target="_blank">RAG System User Interface</a>

## Dockerization of the Project
The initial step involved containerizing the project using Docker to ensure consistency across different development and production environments.![image](https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/8b6444dd-2ced-49bd-97a6-cc2d055b12d1)
<img width="408" alt="image" src="https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/54f32606-045d-45f7-8ec5-2ed4443df5d8">

## erver Acquisition and Deployment
  - Purchased a Ubuntu VPS (Virtual Private Server).
  - Deployed the Dockerized project on this server for testing and production.
![image](https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/bd7961ae-f933-453e-ad23-34ad5df449b8)

## CI/CD Integration
  - Set up Continuous Integration and Continuous Deployment (CI/CD) pipelines on GitHub.
  - Configured automated deployments to streamline development workflows and enhance deployment efficiency.

![image](https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/80fa774a-a96e-46e8-b85d-480bc3585e72)
![image](https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/02b33119-248e-485f-b81d-393793ca1e26)

## Docker Hub Integration
  - Created a new repository on Docker Hub to store Docker images.
  - Linked this repository to our VPS using secret variables in GitHub, which included Docker Hub credentials (username, password) and URL.
![image](https://github.com/BanisharifM/NLP_COMS_579/assets/155206906/b05d8290-624e-48e1-ae2d-c75f9148057a)

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
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/Ali-Deris>
            <img src=https://avatars.githubusercontent.com/u/161876358?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Ali_Adibifar/>
            <br />
            <sub style="font-size:14px"><b>Ali Adibifar</b></sub>
        </a>
    </td>
</tr>
</table>
