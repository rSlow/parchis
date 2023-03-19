import {createContext, useEffect, useState} from 'react';
import axios from "axios";

export const UserContext = createContext(null);

export function UserProvider(props) {
    const localUserToken = localStorage.getItem("userToken")
    const [userToken, setUserToken] = useState(localUserToken === "null" ? null : localUserToken);
    const [user, setUser] = useState({
        username: "",
        email: "",
        id: ""
    })
    const [isAuth, setIsAuth] = useState(false)

    function logout() {
        setUserToken(null)
        setIsAuth(false)
    }

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
                    setIsAuth(true)
                    localStorage.setItem("userToken", userToken)
                } catch (e) {
                    logout()
                    console.log(e.response)
                }
            }
        }

        getMe()
    }, [userToken])


    return <UserContext.Provider value={{userToken, setUserToken, logout, user, isAuth}}>
        {props.children}
    </UserContext.Provider>
}


