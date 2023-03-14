import {createContext, useEffect, useState} from 'react';
import axios from "axios";

export const UserContext = createContext(null);

export function UserProvider(props) {
    const [token, setToken] = useState(localStorage.getItem("userToken"));

    useEffect(() => {
        async function getUser() {
            try {
                await axios.get(
                    "/api/users/me/",
                    {
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    }
                )
            } catch (e) {
                if (e.response.status === 401) {
                    setToken(null)
                }
            }
            localStorage.setItem("userToken", token)
        }

        // getUser()
    }, [token])

    return <UserContext.Provider value={[token, setToken]}>
        {props.children}
    </UserContext.Provider>
}


