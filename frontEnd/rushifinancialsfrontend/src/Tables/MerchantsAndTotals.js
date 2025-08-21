import axios from "axios";
import { useState } from "react";

function Merchants() {
    const [data, setData] = useState([]);   // keep as []


    const getMerchants = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:8000/merchants");

            // ✅ Replace old data, don't append
            setData([response.data]);

        } catch (error) {
            console.error("Error fetching merchants:", error);
        }
    };

    return (
        <div>
            <h2>Merchants and Totals</h2>
            <p>This section will display the merchants and their totals.</p>
            <button onClick={getMerchants} className="btn btn-primary">
                Fetch Merchants
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
        </div>
    );
}

export default Merchants;
