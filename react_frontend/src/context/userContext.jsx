import {createContext, useEffect, useState} from 'react';
import axios from "axios";

export const UserContext = createContext(null);

export function UserProvider(props) {
    const [userToken, setUserToken] = useState(localStorage.getItem("userToken"));

    useEffect(() => {
        async function getUser() {
            try {
                const response = await axios.get(
                    "/api/users/me/",
                    {
                        headers: {
                            Authorization: `Bearer ${userToken}`
                        }
                    }
                )
                console.log(response.data)
            } catch (e) {
                if (e.response.status === 401) {
                    setUserToken(null)
                }
            }
            localStorage.setItem("userToken", userToken)
        }

        getUser()
    }, [userToken])

    useEffect(() => {
        localStorage.setItem("userToken", userToken)
    }, [userToken])

    return <UserContext.Provider value={{userToken, setUserToken}}>
        {props.children}
    </UserContext.Provider>
}


