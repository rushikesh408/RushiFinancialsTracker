import { useState } from "react";
import axios from 'axios';
//import http from "http-common";

function Home() {

    const [file, setFile] = useState(null);

    const handleFileUpload = (event) => {
        //console.log("File selected");

        setFile(event.target.files[0]);

        //console.log("inside handlefileupload");
        //console.log(event.target.files[0]);

        //console.log("inside mkfqw");


    };

    /*const upload = (file, onUploadProgress) => {

        return http.post("/upload", formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
            onUploadProgress,
        });
    };*/

    const handleUploadButton = async (event) => {

        //console.log(file);
        let formData = new FormData();

        formData.append("file", file);

        const resp = await axios.post("http://127.0.0.1:8000/upload", formData,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                }
            })
        console.log(resp)
    }
    return (

        <div>
            <h1>Welcome to Rushi Financials</h1>

            <p>Upload here <br />

                <input type="file" onChange={e => handleFileUpload(e)} />

                <button onClick={e => handleUploadButton(e)}>Upload</button>
            </p>
        </div>



    );
}

export default Home;