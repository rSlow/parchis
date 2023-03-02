import {useEffect, useState} from "react";
import axios from 'axios';

function App() {
    const [message, setMessage] = useState("")

    async function getWelcomeMessage() {
        const response = await axios.get("/api")
        setMessage(response.data["message"])

    }

    useEffect(() => {
        getWelcomeMessage()
    }, [])

    return (
        <div>
            <button onClick={getWelcomeMessage}>
                {message}
            </button>
        </div>
    );
}

export default App;
