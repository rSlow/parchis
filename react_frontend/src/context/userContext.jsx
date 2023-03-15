import {createContext, useEffect, useState} from 'react';
import axios from "axios";

export const UserContext = createContext(null);

export function UserProvider(props) {
    const [userToken, setUserToken] = useState(
        localStorage.getItem("userToken") === "null"
            ? null
            : localStorage.getItem("userToken")
    );
    const [user, setUser] = useState({
        username: "",
        email: "",
        id: ""
    })

    useEffect(() => {
        async function getMe() {
            if (userToken !== null) {
                try {
                    const response = await axios.get(
                        "/api/users/me/",
                        {
                            headers: {
                                Authorization: `Bearer ${userToken}`
                            }
                        }
                    )
                    setUser({...response.data})
                } catch (e) {
                    await setUserToken(null)
                    console.log(e.response)
                }
            }
        }

        getMe()
    }, [userToken])

    useEffect(() => {
        localStorage.setItem("userToken", userToken)
    }, [userToken])


    return <UserContext.Provider value={{userToken, setUserToken, user}}>
        {props.children}
    </UserContext.Provider>
}


