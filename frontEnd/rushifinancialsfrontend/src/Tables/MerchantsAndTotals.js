import axios from "axios";
import { useState } from "react";
import { toast, ToastContainer } from "react-toastify";
import { PieChart } from '@mui/x-charts/PieChart';
import Container from "@mui/material/Container";

function Merchants() {
    const [data, setData] = useState([]);
    const [totalSpent, setTotalSpent] = useState() // keep as []
    const pieData = Object.entries(data[0]).map(([store, amount], index) => (
        { id: index, value: amount, label: store }
    ))



    const getMerchants = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:8000/merchants");
            const readTotalSpent = await axios.get("http://127.0.0.1:8000/totals");

            // ✅ Replace old data, don't append
            setData([response.data]);
            setTotalSpent(readTotalSpent.data["Total Expenses"]);

            //console.log("Merchants data fetched:", response.status);
            //console.log("Total spent fetched:", readTotalSpent.status);

            if (response.status === 200 && readTotalSpent.status === 200) {
                // Success
                toast.success("Merchants and totals fetched successfully!");

            }

        } catch (error) {
            console.error("Error fetching merchants:", error);
        }
        console.log("Data state updated:", data[0]);
    };

    console.log(pieData)

    return (
        <div>
            <h2>Merchants and Totals</h2>
            <div>
                <PieChart
                    series={[
                        {
                            data: pieData,
                        },
                    ]}
                    width={200}
                    height={200}
                />
            </div>
            <Container className="col-md-8">

                <p>This section will display the merchants and their totals.</p>
                <button onClick={getMerchants} className="btn btn-primary">
                    Reresh your spend
                </button>
                <table className="table">
                    <thead>
                        <tr>
                            <th>Merchant Name</th>
                            <th>Total Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.length > 0 &&
                            Object.entries(data[0]).map(([store, amount]) => (
                                <tr key={store}>
                                    <td>{store}</td>
                                    <td>{amount.toFixed(2)}</td>
                                </tr>
                            ))}
                    </tbody>
                </table>
                <div>Total amount spent: {totalSpent}</div>


            </Container>




            <ToastContainer />
        </div>
    );
}

export default Merchants;
