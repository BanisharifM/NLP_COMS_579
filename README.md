

# NLP_COMS_579

RAG - Natural Language Processing Project for the COMS_579 in Spring 2024

<br/>

This project demonstrates how to upload and index PDF files in a Weaviate vector database using LlamaIndex. The project includes a script (upload.py) that chunks the content of PDF files, embeds them using a pre-trained language model, and stores the resulting vectors in Weaviate.

<br/>

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


## Demo 1 Video Link:


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
