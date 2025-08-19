import { useState } from "react";
import axios from 'axios';
import Header from "./commons/Header";
import Merchants from "./Tables/MerchantsAndTotals";

//import http from "http-common";

function Home() {

    const [file, setFile] = useState(null);

    const handleFileUpload = (event) => {


        setFile(event.target.files[0]);



    };



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
            <Header />



            <p>Upload here <br />

                <input type="file" onChange={e => handleFileUpload(e)} />

                <button onClick={e => handleUploadButton(e)}>Upload</button>
            </p>

            <Merchants />
        </div>



    );
}

export default Home;