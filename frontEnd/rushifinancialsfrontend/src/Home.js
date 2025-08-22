import { useRef, useState } from "react";
import axios from 'axios';
import Header from "./commons/Header";
import Merchants from "./Tables/MerchantsAndTotals";
import { ToastContainer, toast } from 'react-toastify';


//import http from "http-common";

function Home() {

    const [file, setFile] = useState(null);
    const ref = useRef()

    const handleFileUpload = (event) => {
        setFile(event.target.files[0]);
    };



    const handleUploadButton = async (event) => {

        toast("File upload in progress...");
        //console.log(file);
        let formData = new FormData();

        formData.append("file", file);

        const resp = await axios.post("http://127.0.0.1:8000/upload", formData,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                }
            })
        console.log(resp.status)

        if (resp.status === 200) {
            toast.success("File uploaded successfully!");
        } else {
            toast.error("File upload failed. Please try again.");
        }

        ref.current.value = "";

    }
    return (

        <div>
            <Header />


            <div className="container">
                <div className="centered-div">
                    <p>Upload here

                        <input type="file" onChange={e => handleFileUpload(e)} ref={ref} />

                        <button onClick={e => handleUploadButton(e)}>Upload</button>
                    </p>
                </div>


            </div>

            <ToastContainer />
            <Merchants />
        </div>



    );
}

export default Home;